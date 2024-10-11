from socket import *

serverName = "127.0.0.1"
serverPort = 4188

# Creating the UDP socket (AF_INET and SOCK_DGRAM are swapped)
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Creating username
userName = raw_input("Enter username in format: <Name><ws><ID>: ")
clientSocket.sendto(userName, (serverName, serverPort))

# Constructing a request string
numofbit = raw_input("Enter your bet in format: <Bet><WS><Prediction>: ")
clientSocket.sendto(numofbit, (serverName, serverPort))

# Receiving instruction from server and print
receivedInfo = clientSocket.recv(4096)
print("Server Response: " + receivedInfo)

# closing the connection
clientSocket.close()
