import socket
import server

import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

server_host = "10.0.0.1"
server_port = server.PORT_NUMBER
pings = 10

socket.setdefaulttimeout(1)


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for x in range(pings):
        message = "Ping " + str(x + 1) + ": "
        server_socket.sendto(message.encode(), (server_host, server_port))

        try:
            response_msg, _ = server_socket.recvfrom(5005)
        except:
            print("Ping " + str(x + 1) + " timed out")
        else:
            print(response_msg.decode() + "Successfully pinged server " + "(" + server_host + ", " + str(server_port) + ")")

    server_socket.close()


if __name__ == "__main__":
    main()
