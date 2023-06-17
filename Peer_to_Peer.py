import socket
import threading
import os

def send_msg(sock, host, port):
    while True:
        option = input("Enter '1' for message, '2' for file name, or '3' for command: ")
        if option == '1':
            msg = 'MSG:' + input("Enter message to send : ")
        elif option == '2':
            msg = 'FILE:' + input("Enter file name : ")
        elif option == '3':
            msg = 'CMD:' + input("Enter command : ")
        else:
            print("Invalid option, try again")
            continue
        sock.sendto(msg.encode(), (host, port))

def receive_msg(sock):
    while True:
        msg, addr = sock.recvfrom(1024)
        print(f"Received message from {addr} : {msg.decode()}")

def peer_program():
    # host and port for this peer to listen on
    host_to_listen = input("Enter host to listen : ")
    port_to_listen = int(input("Enter port to listen : "))
    
    # host and port to connect to
    host_to_connect = input("Enter host to connect : ")
    port_to_connect = input("Enter port to connect : ")  # Change this to input first

    # create two sockets: one for sending and one for receiving
    receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # bind the receiving socket to the host and port this peer should listen on
    receive_socket.bind((host_to_listen, port_to_listen))
    print(f"Listening on {host_to_listen}:{port_to_listen}")

    #Create separate threads for sending and receiving messages
    receive_thread = threading.Thread(target=receive_msg, args=(receive_socket,))
    receive_thread.start()

    # only start send thread if a host and port to connect to were provided
    if host_to_connect and port_to_connect:  # check if these are not empty
        port_to_connect = int(port_to_connect)  # convert port to int here
        send_thread = threading.Thread(target=send_msg, args=(send_socket, host_to_connect, port_to_connect))
        send_thread.start()

peer_program()
