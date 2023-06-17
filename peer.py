import socket
import threading

#This file sets up a peer to peer connection so that each peer could both send and recieve messages

#Function to send messages
def send_msg(sock, host, port):
    while True:
        #send the message to the specified host and port
        msg = input("Enter message to send : ")
        sock.sendto(msg.encode(), (host, port))

#Function to recieve messages
def receive_msg(sock):
    while True:
        #Recieve message
        msg, addr = sock.recvfrom(1024)
        print('Received message from', addr, ':', msg.decode())
#######################################################################################################
######################################################################################################
#Main Function for peer to peer communication
def peer_program():
    #The IP address or hostname of the current machine
    host = '127.0.0.1' #Listen on local host. Change based one where you want to listen.
    #The port that will be used to listen for connections or messages coming in
    port = int(input('Enter port to listen : '))

    ###########################################################################################
    #Create a IPv4 UDP socket

    #Create a new socket using AF_INET for IPv4
    #Specify the socket type as SOCK_DGRAM for UDP
    peer_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #Bind the socket to the address and port
    peer_socket.bind((host, port))
    #########################################################################################

    #IP address of machine the peer wants to connect to
    host_to_connect = input('Enter host to connect : ')
    #The port on the machine the peer wants to connect to
    port_to_connect = int(input('Enter port to connect : '))

    #########################################################################################
    #Use threads so that you can send and recieve messages at the same time
    #The way I understand threading is it will begin executing instructions in parallel (send_msg and recieve_msg)

    #Create seperate threads for sending and recieving messages
    send_thread = threading.Thread(target=send_msg, args=(peer_socket, host_to_connect, port_to_connect))
    receive_thread = threading.Thread(target=receive_msg, args=(peer_socket,))

    #Start the threads
    send_thread.start()
    receive_thread.start()
    ###############################################################################################

#Call the peer program function
if __name__ == '__main__':
    peer_program()

