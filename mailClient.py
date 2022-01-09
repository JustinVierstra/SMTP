from socket import *
msg = "\r\nI love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
#Fill in start 
mailServer = ('gaia.ecs.csus.edu', 25)
#mailServer = ''
#serverPort = 25
#Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer))
#clientSocket.connect((mailServer))
#Fill in end
recv = clientSocket.recv(1024).decode()
print (recv)
if recv[:3] != '220':
    print ('220 reply not received from server.')

# Send HELO command and print server response.
#print("Sending Hello")
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print (recv1)
if recv1[:3] != '250':
    print ('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
mailFromCommand = "MAIL FROM: " + "<gaia@ecs.csus.edu>" + "\r\n"
clientSocket.send(mailFromCommand.encode())
recv1 = clientSocket.recv(1024)
# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
rcptToCommand = 'RCPT TO: ' + "justinvierstra@csus.edu" + '\r\n'
clientSocket.send(rcptToCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print (recv1)
if recv1[:3] != '250':
    print ('250 reply not received from server.')
# Fill in end
# Send DATA command and print server response.
# Fill in start
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv2 = clientSocket.recv(1024).decode()
# Fill in end
print (recv2)
if recv2[:3] != '354':
  print ('354 reply not received from server.')
# Send message data.
# Fill in start
clientSocket.send(msg.encode())
# Fill in end 
# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv3 = clientSocket.recv(1024).decode()
print (recv3)
if recv3[:3] != '250':
  print ('250 reply not received from server.')
# Fill in end
# Send QUIT command and get server response.
# Fill in start
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv4 = clientSocket.recv(1024).decode()
# Fill in end
print (recv4)
if recv4[:3] != '221':
  print ('221 reply not received from server.')
 
clientSocket.close()