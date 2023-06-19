import ssl
import sys
import http.server

SERVER_PORT = 443
SERVER_ADDR = sys.argv[1]
CERT_FILE = './ca_cert/webpa4.test-cert.pem'
KEY_FILE = './ca_cert/webpa4.test-key.pem'

if __name__ == '__main__':
  # TLS protocol
  context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
  context.load_cert_chain(CERT_FILE, KEY_FILE)

  handler = http.server.SimpleHTTPRequestHandler

  # Starts the server
  httpd = http.server.HTTPServer((SERVER_ADDR, SERVER_PORT), handler)
  httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
  print('The server is ready to receive')
  httpd.serve_forever()
