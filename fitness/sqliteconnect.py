import sqlite3

conn=sqlite3.connect("fitness.db")

conn.execute('''
    Create table users(
        user_id INT PRIMARY KEY,
        user_pswd VARCHAR(10),
        fitness_points FLOAT   
    )
''')
conn.close()