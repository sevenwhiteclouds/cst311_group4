import socket as s
import logging
import server

logging.basicConfig()
log=logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

server_host = "10.0.0.1"
server_post = 12000
ping_nums = 10

def main():
    client_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)
    client_socket.settimeout(1)

    for i in range(ping_nums):
        message = "Ping #".format(i+1)
        client_socket.sendto(message.encode(),(server_host,server_port))
    try:
        msg_reply,_ = client_socket.recvfrom(1024)
        print(msg_reply.decode())
    except s.timeout:
        print("Request #".format(i+1) + "timed out")

if __name__ == "__main__":
    main()
