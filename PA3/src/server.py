#!env python

"""Chat server for CST311 Programming Assignment 3"""
__author__ = "Team 4 - Byte Builders"
__credits__ = [
    "Steven C.",
    "Keldin M.",
    "Stacy K.",
    "Sam U."
]

import socket as s
from threading import Thread
import time

# Configure logging
import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

server_port = 12000
message_list = []
response = False


def main():
    # Create a TCP socket
    # Notice the use of SOCK_STREAM for TCP packets
    server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

    # Assign IP address and port number to socket, and bind to chosen port
    server_socket.bind(('', server_port))

    # Configure how many requests can be queued on the server at once
    server_socket.listen(1)

    # Alert user we are now online
    log.info("The server is ready to receive on port " + str(server_port))

    # Creates threads for connection. Currently set to 2 connections. While True loop makes this infinite.
    for i in range(2):
        connection_socket, address = server_socket.accept()
        t = Thread(target=thread_process, args=(connection_socket, address))
        t.start()


def thread_process(connection_socket, address):

    log.info("Connected to client at " + str(address))

    global response
    message = connection_socket.recv(1024)

    # Gets localtime of the delivered message. msg_timestamp places it into readable format
    lt = time.localtime()

    msg_timestamp = str(lt.tm_mon) + "/" \
                    + str(lt.tm_mday) + "/" \
                    + str(lt.tm_year) + " " \
                    + str(lt.tm_hour) + ":" \
                    + str(lt.tm_min) + ":" \
                    + str(lt.tm_sec)

    # Decode data from UTF-8 bytestream
    message_decoded = message.decode()
    # Adds message to list
    message_list.append(message_decoded)

    log.info("Received Message: \"" + str(message_decoded) + "\"" + " at " + msg_timestamp)

    # Waits for both responses before creating response
    while not response:
        if len(message_list) == 2:
            # Perform some server operations on data to generate response
            response = "X:" + "\'" + message_list[0] + "\'," \
                       + " Y:" + "\'" + message_list[1] + "\'"

            # Sent response over the network, encoding to UTF-8
            connection_socket.send(response.encode())

    # Close client socket after response has been sent
    connection_socket.close()


if __name__ == "__main__":
    main()
