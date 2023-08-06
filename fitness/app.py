
from flask import jsonify, request, render_template
import flask
import sqlite3

app = flask.Flask(__name__)

@app.route('/user')
def user():
    conn = None
    try:
        conn = sqlite3.connect('fitness.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        user = cursor.fetchall()
        return jsonify(user)
    except sqlite3.Error as e:
        return 'Database error: {}'.format(e)

@app.route('/user_table')
def user_table():
    conn = None
    try:
        conn = sqlite3.connect('fitness.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        user = cursor.fetchall()
        return render_template('user.html', users=user)
    except sqlite3.Error as e:
        return 'Database error: {}'.format(e)

@app.route('/userlogin', methods=['GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    data = request.form
    username = data.get('username')
    password = data.get('password')

    conn = None
    try:
        conn = sqlite3.connect('fitness.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE user_id=? AND user_pswd=?', (username, password))
        user = cursor.fetchone()
        conn.close()

        if user is not None:
            return jsonify({'message': 'Login successful.'})
        else:
            return jsonify({'message': 'Login failed. Invalid username or password.'})
    except sqlite3.Error as e:
        return 'Database error: {}'.format(e)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/reward')
def reward():
    return render_template('reward.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

def get_fitness_score(username):
    conn = sqlite3.connect('fitness.db')
    cursor = conn.cursor()
    cursor.execute('SELECT fitness_points FROM users WHERE user_id=?', (username,))
    fitness_score = cursor.fetchone()
    conn.close()

    if fitness_score is None:
        return 0
    else:
        return fitness_score[0]

def get_user_id(username, password):
    conn = sqlite3.connect('fitness.db')
    cursor = conn.cursor()
    cursor.execute('SELECT user_id FROM users WHERE user_id=? AND user_pswd=?', (username, password))
    user_id = cursor.fetchone()
    conn.close()

    if user_id is None:
        return None
    else:
        return user_id[0]

def render_trial_page(username, fitness_score):
    data = {
        'username': username,
        'fitness_score': fitness_score,
    }
    return render_template('trial.html', **data)

@app.route('/trial', methods=['GET'])
def trial():
    username = request.args.get('username')
    password = request.args.get('password')

    if username is None or password is None:
        return 'Please enter your username and password.'

    user_id = get_user_id(username, password)

    if user_id is None:
        return 'Invalid username or password.'

    fitness_score = get_fitness_score(username)

    return render_trial_page(username, fitness_score)

if __name__ == '__main__':
    app.run()
