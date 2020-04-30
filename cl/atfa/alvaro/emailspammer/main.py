#  Copyright (c) [ 2020 ] This code is purely educational, the rights of use are
#   reserved, the owner of the code is Alvaro Castillo Calabacero,
#   contact alvaro.castillo@alumnos.ucn.cl
#   Do not use in production.

# SMTP and SSL modules
import smtplib
import ssl

smtpServer = "smtp.gmail.com"
port = 587  # For starttls

# user and password for sender mail
fromEmail = "tstspamm@gmail.com"
password = input("Type your password and press enter: ")

# Victim email test
toEmail = "pcastanedarivera.940807@gmail.com"

# Message
msg = """
 Test message from tstspamm@gmail.com
"""
# SSL context
sslContext = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtpServer, port)
    server.starttls(context=sslContext) # Secure the connection
    server.login(fromEmail, password)

    for i in range(10):
        server.sendmail(fromEmail, toEmail, msg)

except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()