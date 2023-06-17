import subprocess

def create_cert(cn):
    # create key
    subprocess.run(["openssl", "genrsa", ",-out ",  f"{cn}-key.pem", " 2048"])

    with open(f"{cn}", "w") as file:
        file.write()

    # generate cert signing request (CSR)
    subprocess.run(["sudo openssl req -new -config /etc/ssl/openssl.cnf -key ", f"{cn}-key.pem", " -out ", f"{cn}.csr", "-subj", "/C=US/ST=CA/L=Seaside/O=CST311/OU=Networking/CN=www.cst311.test"])

    # generate self-signed certificate using the CSR
    subprocess.run(["sudo openssl x509 -req -days 365 -in", f"{cn}.csr", "-CA /etc/ssl/demoCA/cacert.pem -CAkey /etc/ssl/demoCA/private/cakey.pem  -CAcreateserial -out", f"{cn}-cert.pem"])

# asks for CN for the server
cn = input("Input CN for the server: ")
create_cert(cn)