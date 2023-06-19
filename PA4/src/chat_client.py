#!env python
"""Chat client for CST311 Programming Assignment 3"""
__author__ = "Team 4"
__credits__ = ["Keldin M.", "Stacy K.", "Steven C", "Samuel U."]

# Import statements
import sys
import ssl
import time
import socket as s

# Configure logging
import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# Set global variables
server_name = sys.argv[1]
server_port = 12000

def main():
  context = ssl.create_default_context()
  # Create socket
  client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

  secure_client_socket = context.wrap_socket(client_socket, server_hostname = server_name)

  for i in range(3):
    time.sleep(2)

    try:
      # Establish TCP connection
      secure_client_socket.connect((server_name,server_port))
    except Exception as e:
      #log.exception(e)
      #log.error("***Advice:***")
      if isinstance(e, s.gaierror):
        log.error("\tCheck that server_name and server_port are set correctly.")
      elif isinstance(e, ConnectionRefusedError):
        log.error("\tCheck that server is running and the address is correct")
      else:
        log.error("\tNo specific advice, please contact teaching staff and include text of error and code.")
    else:
      break

    if i < 2:
      log.error(f"\tTrying {3 - (i + 1)} more time(s) in 2 seconds")
    else:
      log.error("\tAborting. No connection was ever found")
      exit(8)

  # Get input from user
  user_input = input("Input lowercase sentence: ")

  # Wrap in a try-finally to ensure the socket is properly closed regardless of errors
  try:
    # Set data across socket to server
    #  Note: encode() converts the string to UTF-8 for transmission
    secure_client_socket.send(user_input.encode())

    # Read response from server
    server_response = secure_client_socket.recv(1024)
    # Decode server response from UTF-8 bytestream
    server_response_decoded = server_response.decode()

    # Print output from server
    print("From Server:")
    print(server_response_decoded)

  finally:
    # Close socket prior to exit
    client_socket.close()

# This helps shield code from running when we import the module
if __name__ == "__main__":
  main()
