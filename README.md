# Overview

In this project, as a software engineer, I am trying to further my understanding and skills in the networking side of software development. I created some Python based applications that allow one computer to communicate with another through a network.

The software is constructed to demonstrate both Client-Server and Peer to Peer models. The client or peer can send requests, and the server or other peer responds accordingly. The purpose of writing this software is to gain practical experience in netwrok programming, understanding how different communication models work, and how systems can exchange data effectively over a network. 


[Software Demo Video](https://www.youtube.com/watch?v=jmYU7mNzDCE)

# Network Communication

In this project, both Client-Server and Peer-Peer architectures are demonstrated. The ssh_cmd.py script follows the Client-Server artchitecture. The Peer_to_Peer.py follows the peer to peer architecture. The project utilizes UDP as the transport layer protocol. For the Peer to Peer example, you can specify custom port numbers while running the scripts. In the Client-Server model, typically port 22 is used for SSH communication. Messages between peers or between clients and server are formatted as plain text, with special prefixes or files or commands. 

# Development Environment

This software was developed using Python. The libraries used were socket, threading, and paramiko. Socket is a tools for creating sockets for network communication. Threading is used for parralel execution. Paramiko is for SSH tools like in the Client-Server example.

I used Virtual Studio Code as my IDE. Be sure to download paramiko with pip install paramiko.

# Useful Websites

* [Python](https://docs.python.org/3/)
* [Paramiko](https://docs.paramiko.org/en/stable/)

# Future Work

* Add encryption to secure communication between peers or client-server.
* Implement a GUI for a more user friendly experience.
