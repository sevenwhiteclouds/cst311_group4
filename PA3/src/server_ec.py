#!env python

"""Chat server for CST311 Programming Assignment 3"""
__author__ = "Team 4"
__credits__ = ["Keldin M.", "Stacy K.", "Steven C", "Samuel U."]

import socket
import threading
import time
import logging


logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

PORT = 12002

def spawn_thread(connections, client, address, queue, client_num):
    # Shows where the server is connected to the client at
    log.info("Connected to client at " + str(address))

    while True:
        # Idenifies the client's index in the list of connections
        num = connections.index(client)
        # Receives the message from the client and decodes it from UTF-8 bytestream
        mssg = client.recv(1024).decode()

        if not mssg:
          # If no message, the client has left
          queue.append(f"Client{client_num} has left")
          # Removes the connection from the list of connections
          connections.pop(num)
          break
        else:
          # Adds the message to the list of messages
          queue.append(f"Client{client_num}: {mssg}")

        time.sleep(.5)

def msg_send(queue, connections):
    while True:
        # Wait until there is a message
        while len(queue) < 1:
            time.sleep(.5)
        # Sends the messages to both client connections
        for i in connections:
            i.send(queue[0].encode())

        log.info("Received Query Test \"" + queue[0] + "\"")
        # Removes the message from the list of messages
        queue.pop(0)

if __name__ == "__main__":
    # Creates a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Assign IP address and port number to socket, and bind to chosen port
    server_socket.bind(('', PORT))
    # Configure how many requests can be queued on the server at once
    server_socket.listen(1)

    # Alerts the user the server is online
    log.info("The server is ready to receive on port " + str(PORT))

    # Initializes lists to store messages and messages
    queue, connections = [], []
    client_num = 1

    # Creates a thread that send messages to the client
    threading.Thread(target=msg_send, args=(queue, connections)).start()

    while True:
        client, address = server_socket.accept()
        connections.append(client)
        # Spawn a new thread that handles each client's messages
        threading.Thread(target=spawn_thread, args=(connections, client, address, queue, client_num)).start()
        client_num += 1

    # Closes the server socket
    server_socket.close()
