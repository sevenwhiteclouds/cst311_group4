#!env python

"""Chat client for CST311 Programming Assignment 3"""
__author__ = "[team name here]"
__credits__ = [
  "Your",
  "Names",
  "Here"
]

# Import statements
import socket as s
import threading

# Configure logging
import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# Set global variables
server_name = "keldin.me"
server_port = 12000

def get_mssgs(client_socket):
  while True:
    print(f"{client_socket.recv(1024).decode()}")

def main():
  # Create socket
  client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
  
  try:
    # Establish TCP connection
    client_socket.connect((server_name,server_port))
  except Exception as e:
    log.exception(e)
    log.error("***Advice:***")
    if isinstance(e, s.gaierror):
      log.error("\tCheck that server_name and server_port are set correctly.")
    elif isinstance(e, ConnectionRefusedError):
      log.error("\tCheck that server is running and the address is correct")
    else:
      log.error("\tNo specific advice, please contact teaching staff and include text of error and code.")
    exit(8)
    
  threading.Thread(target = get_mssgs, args = (client_socket, )).start()

  # Wrap in a try-finally to ensure the socket is properly closed regardless of errors
  while True:
    # Get input from user
    user_input = input()
    print("\033[A\033[A")

    if user_input == "bye":
      break
    # Set data across socket to server
    #  Note: encode() converts the string to UTF-8 for transmission
    client_socket.send(user_input.encode())
    
  client_socket.close()

# This helps shield code from running when we import the module
if __name__ == "__main__":
  main()
