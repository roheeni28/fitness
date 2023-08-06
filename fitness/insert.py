import sqlite3
conn=sqlite3.connect("fitness.db")

ins='''
    INSERT INTO users(user_id, user_pswd) VALUES
    ('1', 'pass1'),
    ('2', 'pass2'),
    ('3', 'Pass4'),
    ('4', 'Pass5'),
    ('5', 'Pass6'),
    ('6', 'Pass7'),
    ('7', 'Pass8'),
    ('8', 'Pass9'),
    ('9', 'Pass10'),
    ('10', 'Pass11'),
    ('11', 'Pass12'),
    ('12', 'Pass12'),
    ('13', 'Pass13'),
    ('14', 'Pass14'),
    ('15', 'Pass15'),
    ('16', 'Pass16'),
    ('17', 'Pass17'),
    ('18', 'Pass18'),
    ('19', 'Pass19'),
    ('20', 'Pass20'),
    ('21', 'Pass11'),
    ('22', 'Pass12'),
    ('23', 'Pass12'),
    ('24', 'Pass13'),
    ('25', 'Pass14'),
    ('26', 'Pass15'),
    ('27', 'Pass16'),
    ('28', 'Pass17'),
    ('29', 'Pass18'),
    ('30', 'Pass19');
'''
conn.execute(ins)
conn.commit()
conn.close()