import sqlite3

# Read Function
def read():
	db=sqlite3.connect("Database.db")
	cursor=db.cursor()
	cursor.execute('select * from info3')
	mult=cursor.fetchall()
	for i in mult:
		print(i)


def printImage():
	uid=input("Enter ID to Take The printOut : ")
	db=sqlite3.connect("Database.db")
	cursor=db.cursor()
	cursor.execute('select * from info3 where id=?',[uid])
	mult=cursor.fetchall()
	for row in mult:
		print(row)


#Create Database
db=sqlite3.connect('Database.db')
cur=db.cursor()
#Create Table
cur.execute("create table IF NOT EXISTS info3(id int,name text,imagelocation text)")
db.commit()

print("Welcome To Admin Console")
print("Press 1 for Pending Images to print:")
cond=input("Enter Your Choice :")


if cond=='1':
	read()
	printImage()
