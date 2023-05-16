#!env

import random
import socket as s

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

def main():
  # Create a UDP socket
  # Notice the use of SOCK_DGRAM for UDP packets
  serverSocket = s.socket(s.AF_INET, s.SOCK_DGRAM)
  # Assign IP address and port number to socket
  serverSocket.bind(('', 12000))
  pingnum = 0
  while True:
    # Count the pings received
    pingnum += 1
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    # Receive the client packet along with the
    # address it is coming from
    message, address = serverSocket.recvfrom(1024)
    # If rand is less is than 4, and this not the
    # first "ping" of a group of 10, consider the
    # packet lost and do not respond

    # the message that is being sent from the client is "echo"
    # printing whether or not the server will return the message
    if rand < 4 and pingnum % 10 != 1:
      print("Client [" + address[0] + "]: refused!")
      continue
    # Otherwise, the server responds
    print("Client [" + address[0] + "]: echoed")
    serverSocket.sendto(message, address)

if __name__ == "__main__":
  main()
