import subprocess

def create_cert(cn):
    # create key
    subprocess.run(["openssl", "genrsa", ",-out ",  f"{cn}-key.pem", " 2048"])

    # create configuration file for cert attributes
    config = f"""
        [req]
        distingushed_name = dn
        """

    with open(f"{cn}", "w") as file:
        file.write(config)

    # generate cert signing request (CSR)
    subprocess.run(["sudo openssl req -nodes -new -config /etc/ssl/openssl.cnf -key ", f"{cn}-key.pem", " -out ", f"{cn}"])

    # generate self-signed certificate using the CSR
    subprocess.run(["sudo openssl x509 -req -days 365 -in", f"{cn}.csr", "-CA cacert.pem -CAkey ./private/cakey.pem -CAcreateserial -out", f"{cn}-cert.pem"])

# asks for CN for the server
cn = input("Input CN for the server: ")
create_cert(cn)