import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="**********",
    database="aicamera"
)

mycursor = db.cursor()

# mycursor.execute("SELECT * FROM Users")
# mycursor.execute("INSERT INTO Users VALUES (%s,%s,%s,%s)",(2,"Tony","ironman","prince friend"))
# db.commit()
# mycursor.execute("SELECT * FROM Users")
# for i in mycursor:
#     print(i)
# for i in mycursor:
#     print(i)

# mycursor.execute("INSERT INTO Users VALUES(%s,%s,%s,%s)",(3, "caption america", "shield", "caption of avanger"))
# db.commit()
# mycursor.execute("SELECT * FROM Users")
# for i in mycursor:
    # print(i)

# mycursor.execute("CREATE TABLE TEST (name varchar(50) NOT NULL, created datetime , gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
# db.commit()

# mycursor.execute("INSERT INTO TEST(name, created, gender) VALUES (%s,%s,%s)",("KK",datetime.now(),"M"))
# db.commit() 

# mycursor.execute("SELECT * FROM TEST WHERE gender='M' ORDER BY idDESC")
# for i in mycursor:
#     print(i)

# mycursor.execute("DESCRIBE TEST")
# print(mycursor.fetchone())
# for i in mycursor:
#     print(i)


# users = [("jack","kala"),
#          ("billi","hargrove"),
#          ("steve","heringthon")]
# score = [
#     (34,55),
#     (66,77),
#     (99,66)
# ]

# q1 = "CREATE TABLE Players (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50))"
# q2 = "CREATE TABLE Scores (pl_id PRIMARY KEY, FOREIGN KEY (pl_id) REFERENCES Players(id), game1 int , game2 int )"
# mycursor.execute(q1)
# mycursor.execute(q2)

# mycursor.execute("SELECT * FROM Players")
# mycursor.execute("DESCRIBE Scores")
# for i in mycursor:
#     print(i)

# a = mycursor.executemany("INSERT INTO (name, passwd) VALUES (%s, %s)")
# b = mycursor.executemany("")

# a = "INSERT INTO Players (name, passwd) VALUES (%s,%s)"
# b = "INSERT INTO Scores (pl_id, game1, game2) VALUES (%s,%s,%s)"

# for i, us in enumerate(users):
#     mycursor.execute(a, us)
#     k = mycursor.lastrowid
#     mycursor.execute(b, (k,)+ score[i])

# mycursor.execute("SELECT * FROM Players")
# for i in mycursor:
#     print(i)
