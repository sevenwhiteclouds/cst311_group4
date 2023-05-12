import socket

# server will always be on mininet h1
IP = "10.0.0.1"
PORT = 12000
socket.setdefaulttimeout(1)

if __name__ == "__main__":
  print("Pinging mininet h1 [" + IP + "] on port [" + str(PORT) + "]:")
  udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  
  ping_num = 0

  for i in range(10):
    ping_num += 1

    try:
      udp_socket.sendto(("Ping " + str(ping_num)).encode(), (IP, PORT))

      echoed_ping = udp_socket.recv(4096)
      print(echoed_ping.decode() + ": Success")
    except:
      print("Ping " + str(ping_num) + ": Request timed out")
