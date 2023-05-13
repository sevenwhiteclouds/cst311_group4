import socket
import server

import logging

# logging which is not used yet
logging.basicConfig()
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)

# const variables
SERVER_HOST = "10.0.0.1"
SERVER_PORT = server.PORT_NUMBER
PINGS = 10

# default timeout much too long - this reduces it
socket.setdefaulttimeout(1)


def main():
    # closes socket after use
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:

        # pings x times (reliant on PING variable)
        for x in range(PINGS):
            message = "Ping " + str(x + 1) + ": "
            server_socket.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))

            # Try-Catch block. Failure == timeout exception
            try:
                response_msg, _ = server_socket.recvfrom(5005)
            except:
                # Failed
                print("Ping " + str(x + 1) + " timed out")
            else:
                # Success
                print(response_msg.decode() + "Successfully pinged server " + "(" + SERVER_HOST + ", " + str(
                    SERVER_PORT) + ")")


if __name__ == "__main__":
    main()
