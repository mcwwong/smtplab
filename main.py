from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp-relay.gmail.com'
mailPort = 587#Fill in start #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, mailPort))
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')


# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: <matthew.c.wong@sjsu.edu>\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
# Fill in start
rcptTo = "RCPT TO: <matthewcwwong01@gmail.com> \r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '250':
    print('250 reply not received from server.')


# Send message data.
mailSubject = "Subject: SMTP Test \r\n\r\n"
clientSocket.send(mailSubject.encode())
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())


recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')
# Message ends with a single period.
clientSocket.send(".\r\n".encode())

# Send QUIT command and get server response.
clientSocket.send("QUIT\r\n".encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '250':
    print('250 reply not received from server.')
clientSocket.close()
