#password of google: mjwa lajv xpoo ybre

#importing libraries
from email.message import EmailMessage
#↑ that librari help to shape the messages sended by email.

import ssl #<- ssl let create a secure connection to send the emails.

import smtplib #<- will help to send emails by the protocol SMTP

email_reciever = ["andres2410020@hybridge.education","prueba1@yopmail.com","prueba2@yopmail.com"]

subject = "Notification of Amazon"

compose = """
Congrats you a special discount in an Iphone 15 just follow the link below...

https://Iphonediscount.amazon.com
"""

def send_email(message, subject, reciever):
    email_sender = "mailbotamazon@gmail.com"
    email_sender_password = "mjwalajvxpooybre"
    
    #Creating a copy of EmailMessage
    email = EmailMessage()

    #Setting who are going to send the message
    email["From"] = email_sender

    #Setting who are going to recieve the message
    email["To"] = ','.join(reciever)

    email['Subject'] = subject

    email.set_content(message)

    #this is useful to send in a secure way the email
    context = ssl.create_default_context()

    #that method allow to send a secured email through a server
    #1.- the server that will be useful to send the email
    #2.- the server port
    #3.- A secured context
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    #login in the sender account
        smtp.login(email_sender, email_sender_password) 

        smtp.sendmail(email_sender,reciever, email.as_string())

send_email(compose, subject, email_reciever)