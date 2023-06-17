import subprocess as sp
import os

# verify if folder "ca-cert" exists
# no?, create it
# yes?, delete it
if os.path.exists("ca-cert"):
    sp.call(["rm", "-rf", "ca-cert"])
sp.call(["mkdir", "ca-cert"])

#Create and keep track of serial numbers
sp.call(["mkdir", "ca-cert/serial"])
sp.call(['touch', 'ca-cert/serial/index.txt'])
f=open("ca-cert/serial/index.txt", "w+")
f.write("1000")
f.close


# 1. generate a root CA signing certificate
print("Generating Root CA Signing Certificate\n========================================\n")
sp.call(['openssl', 'genrsa', '-aes256', '-out', 'cakey.pem', '2048'])
sp.call(['openssl', 'req', '-x509', '-new', '-nodes', '-key','cakey.pem', '-sha256', '-days', '1825', '-out','cacert.pem', '-subj', "/C=US/ST=CA/L=Corona/O=CST311/OU=Networking/CN=www.ca.csumb.test"])
print("\n")

# 2. generate a root CA certificate and private key for web server
print("Generating Root CA Certificate for Web Server\n========================================\n")
sp.call(['openssl', 'genrsa', '-out', 'ca-cert/webpa4.test-key.pem', '2048'])
sp.call(['openssl', 'req', '-nodes', '-new', '-config', '/etc/ssl/openssl.cnf', '-key', 'ca-cert/webpa4.test-key.pem', '-out', 'ca-cert/webpa4.test.csr', '-subj', "/C=US/ST=CA/L=Corona/O=CST311/OU=Networking/CN=www.webpa4.test"])
sp.call(['openssl', 'x509', '-req', '-days', '365', '-in', 'ca-cert/webpa4.test.csr',  '-CA', 'cacert.pem', '-CAkey', 'cakey.pem', '-CAcreateserial', '-out', 'ca-cert/webpa4.test-cert.pem' ])
print("\n")


# 3. generate a root CA certificate and private key for chat server
print("Generating Root CA Certificate for Chat Server\n========================================\n")
sp.call(['openssl', 'genrsa', '-out', 'ca-cert/chatpa4.test-key.pem', '2048'])
sp.call(['openssl', 'req', '-nodes', '-new', '-config', '/etc/ssl/openssl.cnf', '-key', 'ca-cert/chatpa4.test-key.pem', '-out', 'ca-cert/chatpa4.test.csr', '-subj', "/C=US/ST=CA/L=Corona/O=CST311/OU=Networking/CN=www.chatpa4.test"])
sp.call(['openssl', 'x509', '-req', '-days', '365', '-in', 'ca-cert/chatpa4.test.csr',  '-CA', 'cacert.pem', '-CAkey', 'cakey.pem', '-CAcreateserial', '-out', 'ca-cert/chatpa4.test-cert.pem' ])
print("\n")

print("CA certificate and private key generated for : Web Server")
print("CA certificate and private key generated for : Chat Server")
print("\n")
