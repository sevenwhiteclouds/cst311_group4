import socket
import threading
import time
import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

PORT = 12000

def spawn_thread(i, client, address, queue1, queue2):
  log.info("Connected to client at " + str(address))

  while True:
    mssg = client.recv(1024).decode()
    log.info("Recieved query test \"" + mssg + "\"")

    if i == 0:
      queue1.append(mssg)

      while len(queue2) == 0:
        time.sleep(1)

      client.send(queue2.pop(0).encode())
    else:
      queue2.append(mssg)

      while len(queue1) == 0:
        time.sleep(1)

      client.send(queue1.pop(0).encode())

if __name__ == "__main__":
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind(('', PORT))
  server_socket.listen(1)
  
  log.info("The server is ready to receive on port " + str(PORT))
  
  queue1, queue2 = [], []

  for i in range(2):
    client, address = server_socket.accept()
    threading.Thread(target = spawn_thread, args = (i, client, address, queue1, queue2)).start()

  server_socket.close()
