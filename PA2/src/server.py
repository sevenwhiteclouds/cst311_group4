#!env python
import os.path
import socket as s
import sys

serverSocket = s.socket(s.AF_INET,s.SOCK_STREAM)
# todo: Prepare a server socket

while True:
  #Establish the connection
  print('Ready to serve...')
  connection_socket, addr = None, None # todo: Accept a connection

  message = None # todo: accept message from socket
  file_name = message.split()[1]
  if os.path.exists(file_name):
    # File exists so read it and send it
    with open(file_name[1:]) as fid:
      output_data = None # todo: read file to prepare to send over the network
    
    # todo: Send HTTP header file
    
    #Send the content of the requested file to the client
    for i in range(0, len(output_data)):
      connection_socket.send(output_data[i].encode())
      connection_socket.send("\r\n".encode())
  else:
    # File does not exist on server
    pass
    # todo: Send appropriate response message for file not found
  
  # Close the connection socket
  connection_socket.close()
  

