# PythonSocketProgrammingLab
Socket programming lab assignment involving client-server interactions using TCP and UDP in Python

## Python Socket Programming Lab

This project implements a client-server application using Python sockets (TCP and UDP) as part of a university lab assignment.

### Lab Overview
The project involves:
- A TCP client to register for a Casino Game.
- A UDP client to play the game using credentials.
- A simple TCP server to manage multiple client connections using threading.

### Python Socket Programming Lab
Socket programming lab assignment involving client-server interactions using TCP and UDP in Python.

### Project Overview
This project demonstrates the implementation of a client-server architecture using Python sockets with both TCP and UDP protocols. The main goal is to create a TCP server that handles multiple client connections using threading, along with TCP and UDP clients for user registration and interaction.

### Technologies Used
Languages and Tools: Python, TCP/UDP Sockets, Multithreading
Key Concepts: Client-server architecture, socket communication, multithreading for handling multiple connections.
Components

1. TCP Client - Registration System
Description: A TCP client that registers a user for a game by connecting to a server.
Key Features:
Establishes a TCP connection on port 8814.
Sends user credentials and receives a port to join the game server.

2. UDP Client - Game Interaction
Description: A UDP client for playing a betting game after successful registration.
Key Features:
Connects to a UDP server to place bets and make predictions.
Communicates results based on game logic using UDP protocols.

3. Multithreaded TCP Server
Description: A TCP server that handles multiple client connections simultaneously.

### Key Features:
Listens on port 8815 and manages up to 5 clients concurrently.
Implements multithreading to allow clients to communicate independently.
Sends welcome messages and responds to client inputs.


  
