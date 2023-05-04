#!env python

import socket as s
import sys
import os

if len(sys.argv) <= 1:
  print('Usage : "python ProxyServer.py [server_ip]"\n[server_ip : It is the IP Address Of Proxy Server')
  sys.exit(2)

# Create a server listening socket, bind it to a port and start listening
proxy_listening_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
# todo: bind the port appropriately

# Create a socket to our backing server (e.g. server.py), and bind it to a port for when we need it
proxy_backing_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
# todo: bind the port appropriately

while True:
  # Start receiving data from the client
  print('Ready to serve...')
  proxy_client_socket, addr = proxy_listening_socket.accept()
  print('Received a connection from:', addr)
  message = None # todo: add an appropriate message
  print(message)
  
  # Extract the filename from the given message
  print(message.split()[1])
  filename = message.split()[1].partition("/")[2]
  print(filename)
  
  if not os.path.exists(filename):
    # File not found in cache so we retrieve it from the remote server

    # Try to get copy of file from backing server
    try:
      # Create a file object for this socket and ask port 80 for the file requested by the client
      socket_file_obj = c.makefile('r', 0)
      socket_file_obj.write("GET "+"http://" + filename + " HTTP/1.0\n\n")
      
      # todo: Check response and fail gracefully if file wasn't on backing server
      #  If response was bad, craft an appropriate HTTP response and continue
      
      # todo: Read the response into buffer
      # todo: Create a new file in the cache for the requested file.
    except Exception as e:
      print(e)
      exit(8)
  
  # If we make it here, then the file should exist locally
  # ProxyServer finds a cache hit and generates a response message
  with open(filename, "r") as fid:
    output_data = fid.readlines()

  proxy_client_socket.send("HTTP/1.0 200 OK\r\n")
  proxy_client_socket.send("Content-Type:text/html\r\n")
  # todo: generate response using found file
  
