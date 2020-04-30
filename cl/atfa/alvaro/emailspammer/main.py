#  Copyright (c) [ 2020 ] This code is purely educational, the rights of use are
#   reserved, the owner of the code is Alvaro Castillo Calabacero,
#   contact alvaro.castillo@alumnos.ucn.cl
#   Do not use in production.

# @author Alvaro Castillo Calabacero

import socket
# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("www.python.org", 80))
#print(s)