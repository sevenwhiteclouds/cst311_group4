#!env python

"""Chat server for CST311 Programming Assignment 3"""
__author__ = "Team 4"
__credits__ = ["Keldin M.", "Stacy K.", "Steven C", "Samuel U."]
# Multithreading is needed for this program because each client that connects to the server is a thread. Since there
# are multiple clients, there needs to be multiple threads. Multithreading allows these threads to be run concurrently,
# This helps improves the efficiency since  both clients can communicate with the server without waiting for the
# other thread to finish, which prevents delays. To attain multithreading for this program each client needs a thread
# and each thread will allow for the communication between that client and the server. By each client having its own
# thread, no client will be prevented from sending communication to the server. Threading can be implemented in Python
# by using the threading library and creating a function that allows for a new thread to be created each time the
# function is called. In this program the spawn_thread function creates a new thread each time it passes through the
# loop in main.
#

import socket
import threading
import time
import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

PORT = 12000

def spawn_thread(thread_num, client, address, data):
  # Shows where the server is connected to the client at
  log.info("Connected to client at " + str(address))

  # Receives the message from the client and decodes it from UTF-8 bytestream
  mssg = client.recv(1024).decode()

  # Determines if the first thread should be X or Y by checking the thread number and appends to the data list
  if thread_num == 0:
    data.append(f"X : \"{mssg}\"")
  else:
    data.append(f"Y : \"{mssg}\"")

  log.info("Received query test \"" + mssg + "\"")

  # Waits until both of the messages are received
  while len(data) < 2:
    time.sleep(1)

  # Combines the two messages into a single response
  response = f"{data[0]}, {data[1]}"

  # Sends the messages back to the client
  client.send(response.encode())
  # Closes the client connection
  client.close()

if __name__ == "__main__":
  # Creates a TCP socket
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # Assign IP address and port number to socket, and bind to chosen port
  server_socket.bind(('', PORT))
  # Configure how many requests can be queued on the server at once
  server_socket.listen(1)

  # Alerts the user the server is online
  log.info("The server is ready to receive on port " + str(PORT))

  # Initializes a list to store the messages
  data = []

  # Allows for two client connections
  for i in range(2):
    client, address = server_socket.accept()
    # Spawn a new thread that handles each client connection
    threading.Thread(target = spawn_thread, args = (i, client, address, data)).start()

  # Closes the server socket
  server_socket.close()
