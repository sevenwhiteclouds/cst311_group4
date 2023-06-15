import http.server
import ssl


serverPort = 12000
serverAddr = '10.0.0.2'

#needs to be updated to correct location
certfile = '/etc/ssl/demoCA/newcerts/cst311.test-cert.pem'
keyfile = '/etc/ssl/demoCA/private/cst311.test-key.pem'

# TLS protocol
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile, keyfile)

handler = http.server.SimpleHTTPRequestHandler

# Starts the server
httpd = http.server.HTTPServer((serverAddr, serverPort), handler)
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
print('The server is ready to receive')
httpd.serve_forever()