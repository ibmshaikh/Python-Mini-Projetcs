#Libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imaplib


#Send Mail Function
def send_mail():
	myEmail=input("Enter Your Email : ")
	password=input("Enter Your password : ")
	toAdd=input("Enter receiver Email :")
	message=input("Enter You Message :")
	#Library to Make the object to body subject atachment 
	msg = MIMEMultipart()
	msg['From'] = myEmail
	msg['To'] = toAdd
	msg['Subject'] = "Send From Python"
	msg.attach(MIMEText(message, 'plain'))
	email_content = msg.as_string()
	
	#call the smtp server 
	server=smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	
	#Check wheather the Login Details is Correct or Not
	log=False
	while log==False: #to loop until a correct password is aqquired
	    try:
	    	
	        server.login(myEmail, password) #attempt to log into smtp server
	        log=True #sets to true if log in is successful
	        
	    except:
	    	#Incorrect Password Loop
	        print('Incorrect Emai; or Password:\n')
	        myEmail=input('Enter Email again :') 
	        password=input('Enter Password again :')
	
	if (log==True):
		server.sendmail(myEmail,toAdd,email_content)
		server.quit()
		print("Mail Sent")
#Send Mail Function End 


#Read Emails
def read_emails():
	myEmail=input("Enter Your Email : ")
	password=input("Enter Your password : ")
	
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login(myEmail, password)
	

	print(mail.select("inbox"))
	print(mail.list())
	mail.quit()
#Read Email ENDS



#Main Function
print("Welcome to Simple Email Client Console")
print("Press 1 to Send Email")
print("Press 2 to Read Email")

cond=input("Enter yout Choice : ")
if cond=='1':
#	Send Mail Function
	send_mail()
elif cond=='2':
	read_emails()






