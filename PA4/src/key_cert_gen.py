import os
import sys
import subprocess as sp

CN1 = sys.argv[1]
CN2 = sys.argv[2]
H2 = '10.0.1.4'
H4 = '10.0.2.4'

def clean():
  # verify if folder "ca_cert" exists
  if os.path.exists('ca_cert'):
      sp.call(['rm', '-rf', 'ca_cert'])

if __name__ == '__main__':
  # this also includes the name of this file
  clean()
  sp.call(['mkdir', 'ca_cert'])

  # 1. generate a certificate and private key for web server
  sp.call(['openssl', 'genrsa', '-out', './ca_cert/webpa4.test-key.pem', '2048'])
  sp.call(['openssl', 'req', '-new', '-config', '/etc/ssl/openssl.cnf', '-key', './ca_cert/webpa4.test-key.pem', '-out', './ca_cert/webpa4.test.csr', '-subj', f'/C=US/ST=CA/L=Corona/O=CST311/OU=Networking/CN={CN1}'])
  return_code1 = sp.call(['sudo', 'openssl', 'x509', '-req', '-days', '365', '-in', './ca_cert/webpa4.test.csr',  '-CA', '/etc/ssl/demoCA/cacert.pem', '-CAkey', '/etc/ssl/demoCA/private/cakey.pem', '-CAcreateserial', '-out', './ca_cert/webpa4.test-cert.pem' ])

  if return_code1 != 0:
    clean()
    sys.exit(1)

  # 2. generate a certificate and private key for chat server
  sp.call(['openssl', 'genrsa', '-out', './ca_cert/chatpa4.test-key.pem', '2048'])
  sp.call(['openssl', 'req', '-new', '-config', '/etc/ssl/openssl.cnf', '-key', './ca_cert/chatpa4.test-key.pem', '-out', './ca_cert/chatpa4.test.csr', '-subj', f'/C=US/ST=CA/L=Corona/O=CST311/OU=Networking/CN={CN2}'])
  return_code2 = sp.call(['sudo', 'openssl', 'x509', '-req', '-days', '365', '-in', './ca_cert/chatpa4.test.csr',  '-CA', '/etc/ssl/demoCA/cacert.pem', '-CAkey', '/etc/ssl/demoCA/private/cakey.pem', '-CAcreateserial', '-out', './ca_cert/chatpa4.test-cert.pem' ])

  if return_code2 != 0:
    clean()
    sys.exit(1)

  hosts_file = open('/etc/hosts', 'r+')
  lines = hosts_file.readlines()
  hosts_file.seek(0)
  hosts_file.truncate()
  hosts_file.seek(0)

  for i in lines:
    if H2 in i:
      lines.remove(i)

    if H4 in i:
      lines.remove(i)

  for i in lines:
    if CN1 in i:
      lines.remove(i)

    if CN2 in i:
      lines.remove(i)

  lines.append(f'{H2}\t{CN1}\n')
  lines.append(f'{H4}\t{CN2}\n')

  hosts_file.writelines(lines)
  hosts_file.close()

  # print what was generated
  print('\nCertificate and private key generated for: Web Server')
  print('Certificate and private key generated for: Chat Server\n')
