import socket
import threading
import time
import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

PORT = 12000
lock = threading.Lock()

def spawn_thread(connections, client, address, queue, client_num):
    log.info("Connected to client at " + str(address))

    num = 0
    while True:
        num = connections.index(client)
        try:
          mssg = client.recv(1024).decode()
        except:
          lock.acquire()
          client.close()
          connections.pop(num)
          lock.release()
          return

        queue.append(f"Client{client_num}: {mssg}")
        time.sleep(1)

def msg_send(queue, connections):
    while True:
        while len(queue) < 1:
            time.sleep(.5)

        lock.acquire()
        for i in connections:
          i.send(queue[0].encode())

        log.info("Received Query Test \"" + queue[0] + "\"")
        queue.pop(0)
        lock.release()

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
        threading.Thread(target=spawn_thread, args=(connections, client, address, queue, client_num)).start()
        client_num += 1

    server_socket.close()
