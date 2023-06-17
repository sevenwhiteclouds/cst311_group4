import subprocess as sp
import os

# verify if folder "ca-cert" exists
# no?, create it
# yes?, delete it
if os.path.exists("ca-cert"):
    sp.call(["rm", "-rf", "ca-cert"])
sp.call(["mkdir", "ca-cert"])

# 1. generate a root CA certificate and private key for web server
print("\nGenerating Root CA Certificate for Web Server\n========================================\n")
sp.call(['openssl', 'genrsa', '-out', 'ca-cert/webpa4.test-key.pem', '2048'])
sp.call(['openssl', 'req', '-new', '-config', '/etc/ssl/openssl.cnf', '-key', 'ca-cert/webpa4.test-key.pem', '-out', 'ca-cert/webpa4.test.csr', '-subj', "/C=US/ST=CA/L=Corona/O=CST311/OU=Networking/CN=www.webpa4.test"])
sp.call(['openssl', 'x509', '-req', '-days', '365', '-in', 'ca-cert/webpa4.test.csr',  '-CA', '/etc/ssl/demoCA/cacert.pem', '-CAkey', '/etc/ssl/demoCA/private/cakey.pem', '-CAcreateserial', '-out', 'ca-cert/webpa4.test-cert.pem' ])
print("\n")


# 2. generate a root CA certificate and private key for chat server
print("Generating Root CA Certificate for Chat Server\n========================================\n")
sp.call(['openssl', 'genrsa', '-out', 'ca-cert/chatpa4.test-key.pem', '2048'])
sp.call(['openssl', 'req', '-new', '-config', '/etc/ssl/openssl.cnf', '-key', 'ca-cert/chatpa4.test-key.pem', '-out', 'ca-cert/chatpa4.test.csr', '-subj', "/C=US/ST=CA/L=Corona/O=CST311/OU=Networking/CN=www.chatpa4.test"])
sp.call(['openssl', 'x509', '-req', '-days', '365', '-in', 'ca-cert/chatpa4.test.csr',  '-CA', '/etc/ssl/demoCA/cacert.pem', '-CAkey', '/etc/ssl/demoCA/private/cakey.pem', '-CAcreateserial', '-out', 'ca-cert/chatpa4.test-cert.pem' ])
print("\n")


print("CA certificate and private key generated for : Web Server")
print("CA certificate and private key generated for : Chat Server")
print("\n")
