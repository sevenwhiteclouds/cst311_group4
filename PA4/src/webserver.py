import http.server
import socket as s
import ssl


serverPort = 12000
serverAddr = '10.0.0.2'

#needs to be updated to correct location
certfile = '/etc/ssl/demoCA/newcerts/chatserver-cert.pem'
keyfile = '/etc/ssl/demoCA/private/chatserver-key.pem'

# TLS protocol
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile, keyfile)

handler = http.server.SimpleHTTPRequestHandler


serverSocket = s.socket(s.AF_INET, s.SOCK_STREAM)
serverSocket.bind((serverAddr, serverPort))
serverSocket.listen(5)
# Sets up TLS
wrappedSocket = context.wrap_socket(serverSocket, server_side=True)
print('The server is ready to receive')

# Starts the server
httpd = http.server.HTTPServer((serverAddr, serverPort), handler)
httpd.socket = wrappedSocket
httpd.serve_forever()