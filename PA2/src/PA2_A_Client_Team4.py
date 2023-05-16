# Server-Client Ping: Project 2
# Author: Team 4
# Credits: Keldin M., Stacy K., Samuel U., Steven C.

import socket
import time

# globals, server ip, port, dec place, socket timeout
SERVER = "10.0.0.1"
PORT = 12000
REQUESTS = 10
BUFFER_SIZE = 1024
PRECISION = 3
socket.setdefaulttimeout(1)

if __name__ == "__main__":
  print("Pinging server [" + SERVER + "] on port [" + str(PORT) + "] " + str(REQUESTS) + " times:")

  # Creates a UDP socket
  udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  min_rtt = max_rtt = est_rtt = avg_rtt = requests_ok = dev_rtt = 0.0

  for i in range(REQUESTS):
    # Starts timer on packet send
    timer_start = time.time()
    udp_socket.sendto("echo".encode(), (SERVER, PORT))

    # Checks for response from server
    try:
      udp_socket.recvfrom(BUFFER_SIZE)
    except socket.timeout:
      # No server response
      print("Ping " + str(i + 1) + ": Request timed out")
    else:
      # Successful server response
      requests_ok += 1
      # Subtracts timestamp from first call with this call
      sample_rtt = time.time() - timer_start

      # Checks for previous ping values, if not, initializes variables
      if avg_rtt == 0.0:
        min_rtt = max_rtt = sample_rtt
      elif sample_rtt > max_rtt:
        max_rtt = sample_rtt
      elif sample_rtt < min_rtt:
        min_rtt = sample_rtt

      # if first ping, initialize variables est_rtt dev_rtt
      if i == 0:
        est_rtt = sample_rtt
        dev_rtt = sample_rtt / 2
      else:
        est_rtt = (0.875 * est_rtt) + (0.125 * sample_rtt)
        dev_rtt = (0.75 * dev_rtt) + (0.25 * abs(sample_rtt - est_rtt))

      avg_rtt += sample_rtt

      print("Ping " + str(i + 1)
      + ": sample_rtt = " + str(round(sample_rtt, PRECISION))
      + " ms, estimated_rtt = " + str(round(est_rtt, PRECISION))
      + " ms, dev_rtt = " + str(round(dev_rtt, PRECISION)))

  # Closes socket
  udp_socket.close()

  if avg_rtt > 0.0:
    print("Summary values:\n"
          "min_rtt = " + str(round(min_rtt, PRECISION))
    + " ms\nmax_rtt = " + str(round(max_rtt, PRECISION))
    + " ms\navg_rtt = " + str(round(avg_rtt / requests_ok, PRECISION))
    + " ms\nPacket loss: " + str(round(100 - (requests_ok / REQUESTS) * 100, PRECISION)) + "%\n"
    + "Timeout Interval: " + str(round(4 * dev_rtt + est_rtt, PRECISION)) + " ms")
  else:
    print("The server did not respond at all!") 
