import socket
import threading
import time
import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

PORT = 12000

def spawn_thread(client, address, queue, client_num):
    log.info("Connected to client at " + str(address))

    while True:
        try:
          mssg = client.recv(1024).decode()
          queue.append(f"Client{client_num}: {mssg}")
        except:
          client.close()
          break

        time.sleep(.5)

def msg_send(queue, connections):
    while True:
        while len(queue) < 1:
            time.sleep(.5)


        num = 0

        for i in range(len(connections)):
          try:
            connections[num].send(queue[0].encode())
            num += 1
          except:
            connections.pop(num)
            num -= 1
            print("it popped")

            i += 1

            continue

        log.info("Received Query Test \"" + queue[0] + "\"")
        queue.pop(0)

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', PORT))
    server_socket.listen(1)

    log.info("The server is ready to receive on port " + str(PORT))

    queue, connections = [], []
    client_num = 1

    threading.Thread(target=msg_send, args=(queue, connections)).start()

    while True:
        client, address = server_socket.accept()
        connections.append(client)
        threading.Thread(target=spawn_thread, args=(client, address, queue, client_num)).start()
        client_num += 1

    server_socket.close()


    """
    for i < 4
    i = 0
    i = 1
    i = 2
    i = 3
    """
    """
    for i < 4
    i = 0
    i = 1 - pop
    i = 1
    i = 2
    i = 3
    """
    """
    for i < 4
    i = 0
    i = 1 - pop
    i = 3
    """

