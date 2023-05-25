import socket
import threading
import time
import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

PORT = 12000

def spawn_thread(client, address, lock, data):
  log.info("Connected to client at " + str(address))

  mssg = client.recv(1024).decode()

  lock.acquire()
  data.append(mssg)
  lock.release()

  log.info("Recieved query test \"" + mssg + "\"")

  while len(data) < 2:
    time.sleep(1)
  
  response = "X : \"" + data[0] + "\", Y : \"" + data[1] + "\""

  client.send(response.encode())
  client.close()

if __name__ == "__main__":
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind(('', PORT))
  server_socket.listen(1)
  
  log.info("The server is ready to receive on port " + str(PORT))
  
  lock, data = threading.Lock(), []

  for i in range(2):
    client, address = server_socket.accept()
    threading.Thread(target = spawn_thread, args = (client, address, lock, data)).start()

  server_socket.close()
