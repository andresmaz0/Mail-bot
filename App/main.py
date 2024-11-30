#password of google: mjwa lajv xpoo ybre

#importing libraries
from email.message import EmailMessage
#↑ that librari help to shape the messages sended by email.

#will help to decoded the message which comes in bytes
import email

#will help to decoded the header of the email
from email.header import decode_header

import ssl #<- ssl let create a secure connection to send the emails.

import smtplib #<- will help to send emails by the protocol SMTP

import imaplib #<- will help to reply emails by the protocol IMAP

email_sender = "mailbotamazon@gmail.com"

email_sender_password = "mjwalajvxpooybre"

email_reciever = ["andres2410020@hybridge.education","prueba1@yopmail.com","prueba2@yopmail.com"]

subject = "Notification of Amazon"

compose = """
Congrats you a special discount in an Iphone 15 just follow the link below...

https://Iphonediscount.amazon.com
"""

#That function use IMAP protocol
def reply_email(reply_message):
    imap_server = "imap.gmail.com" # server url
    imap_port = 993 # server port

    # Creating a secure connection to our server of IMAP
    imap_connection = imaplib.IMAP4_SSL(imap_server, imap_port)

    #Login with user and password
    imap_connection.login(email_sender,email_sender_password)

    #Selecting inbox section
    imap_connection.select("inbox")

    #Searching the unseen emails
    status, data = imap_connection.search(None, "UNSEEN")

    #spliting the bytes of the data variable
    unseen_emails = data[0].split()

    for byte in unseen_emails:
        #decoding the data recieve(bytes) into list [0]->tuples and [1]-> bytes with protocol RFC822
        #decoded_data has a in the position[0] has a tuple of message and in the potion[1] has bytes of the message
        #'(RFC822)': Requests the entire message body in raw email format (including headers and body).
        status, decoded_data = imap_connection.fetch(byte, '(RFC822)')

        for reply in decoded_data:
            """I have to filter the tuple data type because some data is no always a tuple
            Example: (b'1 (RFC822 {1024}', b'<raw email bytes here>'), b')'
            And if the data type is no a tuple it give me a traceback"""
            if isinstance(reply, tuple):
                #reply[1] has the body of the message and [0] has metadata as identifiers or protocol information
                msg = email.message_from_bytes(reply[1])

                subject, encoding = decode_header(msg["Subject"])[0]

                #It helps to know if the email has a second layer
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding or 'utf-8')

                sender = msg.get("From")

                #replying the message
                send_email(reply_message, subject, sender)



def send_email(message, subject, reciever):
    #Creating a copy of EmailMessage
    email = EmailMessage()

    #Setting who are going to send the message
    email["From"] = email_sender

    #Setting who are going to recieve the message
    email["To"] = ','.join(reciever)
    #IMPORTANT IF YOU WANT A Bcc reciber, you have to delete email["To"] and just send email

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

#send_email(compose, subject, email_reciever)

reply_email("")