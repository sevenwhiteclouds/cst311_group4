import http.server
import ssl


serverPort = 12000
serverAddr = "www.webpa4.test"

#needs to be updated to correct location
certfile = '/home/mininet/ca-cert/webpa4.test-cert.pem'
keyfile = '/home/mininet/ca-cert/webpa4.test-key.pem'

# TLS protocol
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile, keyfile)

handler = http.server.SimpleHTTPRequestHandler

# Starts the server
httpd = http.server.HTTPServer((serverAddr, serverPort), handler)
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
print('The server is ready to receive')
httpd.serve_forever()