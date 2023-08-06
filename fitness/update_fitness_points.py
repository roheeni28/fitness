
import pandas as pd
import sqlite3

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('dataset_updated.csv')

# Fetch user IDs and fitness points from the DataFrame
user_data = df[['User ID', 'Fitness Points']]

# Connect to the SQLite database
conn = sqlite3.connect('fitness.db')
cursor = conn.cursor()

# Create the fitness_points column in the user table
# cursor.execute('''ALTER TABLE users ADD COLUMN fitness_points REAL;''')

# Update the "fitness_points" column in the "user" table
for index, row in user_data.iterrows():
    user_id = int(row['User ID'])
    fitness_points = float(row['Fitness Points'])

    # Check if the user exists in the user table
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()

    # If the user exists, update the fitness_points column
    if result is not None:
        cursor.execute('UPDATE users SET fitness_points = ? WHERE user_id = ?', (fitness_points, user_id))

    # Otherwise, insert a new row into the user table
    else:
        cursor.execute('INSERT INTO users (user_id, fitness_points) VALUES (?, ?)', (user_id, fitness_points))

# Commit the changes and close the connection
conn.commit()
conn.close()
