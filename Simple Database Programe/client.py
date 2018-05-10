from tkinter import Tk
import sqlite3
from tkinter.filedialog import askopenfilename

#Image Selecting Function 
def selectImages():
	pass
	root = Tk()
	ftypes = [('jpg file',"*.jpg")]
	ttl  = "Title"
	dir1 = 'C:\\'
	root.fileName = askopenfilename(filetypes = ftypes, initialdir = dir1, title = ttl)
	#print(root.fileName)
	print(root.fileName)
	return root.fileName

#Data Storing Function
def storeinDatabase(UserName,UserId,fileName):
	db=sqlite3.connect('Database.db')
	cursor=db.cursor()
	cursor.execute('insert into info3 (id,name,imagelocation) values(?,?,?)',(UserName,UserId,fileName))
	db.commit()
	print("Data Stored Successfully")
	print("Your Request Has Been Sent")
	


#Main Function
print("Welcome To Console")
UserName=input("Enter Yout Name : ")
UserId=input("Enter Your ID in integers : ")
print("Select Imagelocation")
fileName=selectImages()
storeinDatabase(UserName,UserId,fileName)

