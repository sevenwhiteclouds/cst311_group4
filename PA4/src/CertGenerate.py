import subprocess as sp
import os

# verify if folder "ca-cert" exists
# no?, create it
# yes?, delete it
if os.path.exists("ca-cert"):
    sp.call(["rm", "-rf", "ca-cert"])
sp.call(["mkdir", "ca-cert"])


# 1. generate a root CA certificate and private key for web server
sp.call(['openssl', 'genrsa', '-aes256', '-out', 'ca-cert/webpa4.test-key.pem', '2048'])
sp.call(['openssl', 'req', '-nodes', '-new', '-config', '/etc/ssl/openssl.cnf', '-key', 'ca-cert/webpa4.test-key.pem', '-out', 'ca-cert/webpa4.test.csr.pem', '-subj', "/C=US/ST=CA/L=Corona/O=CST311/OU=Networking/CN=www.webpa4.test"])
sp.call(['openssl', 'x509', '-req', '-days', '365', '-in', 'ca-cert/webpa4.test.csr.pem',  '-signkey', 'ca-cert/webpa4.test-key.pem', '-out', 'ca-cert/webpa4.test-cert.crt' ])
print("\n")


# 2. generate a root CA certificate and private key for chat server
sp.call(['openssl', 'genrsa', '-aes256', '-out', 'ca-cert/chatpa4.test-key.pem', '2048'])
sp.call(['openssl', 'req', '-nodes', '-new', '-config', '/etc/ssl/openssl.cnf', '-key', 'ca-cert/chatpa4.test-key.pem', '-out', 'ca-cert/chatpa4.test.csr.pem', '-subj', "/C=US/ST=CA/L=Corona/O=CST311/OU=Networking/CN=www.chatpa4.test"])
sp.call(['openssl', 'x509', '-req', '-days', '365', '-in', 'ca-cert/chatpa4.test.csr.pem',  '-signkey', 'ca-cert/chatpa4.test-key.pem', '-out', 'ca-cert/chatpa4.test-cert.crt' ])
print("\n")

print("CA certificate and private key generated for : Web Server")
print("CA certificate and private key generated for : Chat Server")
