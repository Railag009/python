import sqlite3
# import cgi
con = sqlite3.connect('HH.db')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS Architect')
cur.execute('DROP TABLE IF EXISTS Order')
cur.execute('DROP TABLE IF EXISTS Work')
cur.fetchall()
cur.execute('''CREATE TABLE Architect(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(30),
            surname VARCHAR(30),
            WorkExperience   INTEGER,
            phone VARCHAR(30))''')
cur.execute('''CREATE TABLE IF NOT EXISTS Order(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Style VARCHAR(30),
            Materials VARCHAR(30),
            Price INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Work(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ArchitectId INTEGER,
            OrderId INTEGER)''')

architect=[
    ("Alvaro","Siza","35","+19243641488"),
    ("Antonio","Predock","24","+99146181337"),
    ("Andre","Diakonov","3","+79283572648")
]
order=[
    ("Modern","Polypropylene","1200000"),
    ("Gotic","Stone","850000"),
    ("Loft","Brick","120000")
]
work=[
    (2,1),
    (1,2),
    (3,3)
]

sqlE='''INSERT INTO Architect(name,surname,WorkExperience,phone) VALUES (?,?,?,?)'''
sqlA='''INSERT INTO Order(style,materials,price) VALUES (?,?,?)'''
sqlC='''INSERT INTO Work(ArchitectId,OrderId) VALUES (?,?)'''

cur.executemany(sqlE,architect)
cur.executemany(sqlA,order)
cur.executemany(sqlC,work)

con.commit()

cur.execute('SELECT * FROM architect ORDER BY name ASC')
print(cur.fetchall())
cur.execute('SELECT * FROM order WHERE salary>700000')
print(cur.fetchall())
cur.execute('SELECT * FROM work')
print(cur.fetchall())
