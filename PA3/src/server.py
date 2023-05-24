import socket
import threading
import time
import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

server_port = 12000

def spawn_thread(connection_socket, address, lock, data):
  log.info("Connected to client at " + str(address))

  mssg = connection_socket.recv(1024).decode()

  lock.acquire()
  data.append(mssg)
  lock.release()

  log.info("Recieved query test \"" + mssg + "\"")

  while len(data) < 2:
    time.sleep(1)
  
  response = 'X : "' + data[0] + '", Y : "' + data[1] + '"'

  connection_socket.send(response.encode())
  connection_socket.close()

if __name__ == "__main__":
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind(('', server_port))
  server_socket.listen(1)
  
  log.info("The server is ready to receive on port " + str(server_port))
  
  connections = {}
  data = []
  lock = threading.Lock()
  i = 0
  try:
    while True:
      if len(connections) > 1:
        break
        
      client = server_socket.accept()
      connections[i] = [client[0], client[1]]
      threading.Thread(target = spawn_thread, args = (connections[i][0], connections[i][1], lock, data)).start()

      i += 1
  finally:
    server_socket.close()
