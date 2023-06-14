import socket
import threading
import time
import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

PORT = 12000

def spawn_thread(client, address, mssgs):
  log.info(f"Connected to client at {address}")

  recv_mssg = client.recv(1024).decode()
  log.info("Recieved query test \"" + recv_mssg + "\"")

  thread_name = threading.current_thread().name

  if thread_name == "Thread-1 (spawn_thread)":
    mssgs.append(f"X : \"{recv_mssg}\"")
  elif thread_name == "Thread-2 (spawn_thread)":
    mssgs.append(f"Y : \"{recv_mssg}\"")

  while len(mssgs) < 2:
    time.sleep(1)
  
  response = f"{mssgs[0]}, {mssgs[1]}"

  client.send(response.encode())
  client.close()

def main():
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server_socket.bind(('', PORT))
  server_socket.listen(1)
  
  log.info(f"The server is ready to receive on port {PORT}")
  
  mssgs = []

  for i in range(2):
    client, address = server_socket.accept()
    threading.Thread(target = spawn_thread, args = (client, address, mssgs)).start()

  server_socket.close()

if __name__ == "__main__":
  main()
