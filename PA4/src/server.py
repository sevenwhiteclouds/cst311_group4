import socket
import threading
import time
import logging
import ssl

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

PORT = 12000

def spawn_thread(secure_client, address, mssgs):
  log.info(f"Connected to client at {address}")

  recv_mssg = secure_client.recv(1024).decode()
  log.info(f"Recieved query test \"{recv_mssg}\"")

  thread_name = threading.current_thread().name

  if thread_name == "Thread-1" or thread_name == "Thread-1 (spawn_thread)":
    mssgs.append(f"X : \"{recv_mssg}\"")
  elif thread_name == "Thread-2" or thread_name == "Thread-2 (spawn_thread)":
    mssgs.append(f"Y : \"{recv_mssg}\"")

  while len(mssgs) < 2:
    time.sleep(1)
  
  secure_client.send(f"{mssgs[0]}, {mssgs[1]}".encode())
  secure_client.close()

if __name__ == "__main__":
  context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
  context.load_cert_chain("/etc/ssl/demoCA/newcerts/cst311.test-cert.pem", "/etc/ssl/demoCA/private/cst311.test-key.pem")

  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server_socket.bind(('', PORT))
  server_socket.listen(1)
  
  log.info(f"The server is ready to receive on port {PORT}")
  
  mssgs = []

  for i in range(2):
    client, address = server_socket.accept()
    secure_client = context.wrap_socket(client, server_side = True)

    threading.Thread(target = spawn_thread, args = (secure_client, address, mssgs)).start()

  server_socket.close()
