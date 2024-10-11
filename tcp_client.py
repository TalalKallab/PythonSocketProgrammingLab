from socket import *

serverName = "127.0.0.1"
serverPort = 8814

clientSocket = socket(AF_INET, SOCK_STREAM)

# Connecting to the server
clientSocket.connect((serverName, serverPort))

# Receiving the initial instructions from the server
receivedText = clientSocket.recv(4096)
print "Server Instructions: " + receivedText

#user input in the required format
userName = raw_input("Enter username in format <user><ws><ID>: ")

# Sending the registration request to the server
clientSocket.send(userName)

# Receive the server's response
receivedText = clientSocket.recv(4096)
print "Server Response: " + receivedText

# closing the connection
clientSocket.close()
