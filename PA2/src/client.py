import socket

# server will always be on mininet h1
SERVER = "10.0.0.1"
PORT = 12000
REQUESTS = 10
socket.setdefaulttimeout(1)

if __name__ == "__main__":
  print("Pinging server [" + SERVER + "] on port [" + str(PORT) + "] " + str(REQUESTS) + " times:")
  udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  
  ping_count = 0

  for i in range(REQUESTS):
    ping_count += 1
    udp_socket.sendto(("Ping " + str(ping_count)).encode(), (SERVER, PORT))

    try:
      echoed_ping = udp_socket.recv(4096)
    except TimeoutError:
      print("Ping " + str(ping_count) + ": Request timed out")
    else:
      print(echoed_ping.decode() + ": Success")

  udp_socket.close()
