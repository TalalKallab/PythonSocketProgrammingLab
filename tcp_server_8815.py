from socket import *

serverPort = 8815

#TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind
serverSocket.bind(('', serverPort))  # Bind to all available interfaces

# listening to a maximum 5 incoming connections (messages)
serverSocket.listen(5)
print("The server is ready to receive a connection...")

while True:
    # Accept incoming connections
    connectionSocket, addr = serverSocket.accept()
    print("Connected to:", addr)

    #sending a message to the client
    hello_message = "Hello from server!"
    connectionSocket.send(hello_message.encode())

    # receiving the message from the client
    message = connectionSocket.recv(1024).decode()
    print("Received from client:", message)


    response = "Thank you for your message!"
    connectionSocket.send(response.encode())

    # closing the connection with the client
    connectionSocket.close()
    print("Connection with", addr, "closed.")
