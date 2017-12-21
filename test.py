import sqlite3

cnn = sqlite3.connect("data")
cur = cnn.cursor()
#cur.execute("CREATE TABLE Data (Type INT, Cmt1 nvarchar(1000), Cmt2 nvarchar(1000))")
for el in cur.execute("select * from Data").fetchall():
    print(el)
#f = open("T.txt", "r")
#tech = f.readline().split()
#print(tech)
#gum = f.readline().split()
#print(gum2)
cnn.commit()
cnn.close()