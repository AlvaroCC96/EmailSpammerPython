#  Copyright (c) [ 2020 ] This code is purely educational, the rights of use are
#   reserved, the owner of the code is Alvaro Castillo Calabacero,
#   contact alvaro.castillo@alumnos.ucn.cl
#   Do not use in production.

# SMTP and SSL modules
import smtplib
import ssl
import mysql.connector
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# smtp server
smtpServer = "smtp.gmail.com"
port = 587  # For starttls

# user and password for sender mail
fromEmail = "tstspamm@gmail.com"
password = input("Type your password for your email and press enter: ")

# Message
msg = """
 Test message from tstspamm@gmail.com
"""

# SSL context
sslContext = ssl.create_default_context()

# Try to log in to server and database for send email
try:
    # connect to server
    server = smtplib.SMTP(smtpServer, port)
    server.starttls(context=sslContext)  # Secure the connection
    server.login(fromEmail, password)

    # connect to database, change user and the other data
    connection = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='test')

    # raise Exception
    if not connection.is_connected():
        raise Exception

    # get table and users
    cursor = connection.cursor()
    query = "Select * from user"
    cursor.execute(query)

    # the email in table user is in the position '5', this is a victim email
    for user in cursor:
        emailTo = user[5]
        message = MIMEMultipart()
        message['From'] = fromEmail
        message['To'] = emailTo
        message['Subject'] = "This is a TEST SUBJECT"
        message.attach(MIMEText(msg, 'plain'))

        # for each email, send message
        server.send_message(message)
        del message

        print("Message Sent to: "+emailTo)

    server.close()

except Exception as e:
    # Print any error message
    print(e)
finally:
    server.quit()