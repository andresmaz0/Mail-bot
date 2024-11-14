#password of google: mjwa lajv xpoo ybre

#importing libraries
from email.message import EmailMessage
#↑ that librari help to shape the messages sended by email.

import ssl #<- ssl let create a secure connection to send the emails.

import smtplib #<- will help to send emails by the protocol SMTP

email_sender = "mailbotamazon@gmail.com"
email_sender_password = "mjwalajvxpooybre"
email_reciever = "andres2410020@hybridge.education"

subject = "Notification of Amazon"

compose = """
Congrats you a special discount in an Iphone 15 just follow the link below...
"""

#Creating a copy of EmailMessage
email = EmailMessage()

#Setting who are going to send the message
email["From"] = email_sender

#Setting who are going to recieve the message
email["To"] = email_reciever

email['Subject'] = subject

email.set_content(compose)

#this is useful to send in a secure way the email
context = ssl.create_default_context()

