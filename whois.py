#!/usr/bin/python3
import socket, sys

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.connect(("whois.iana.org",43))
s.send(str.encode(sys.argv[1]+"\r\n"))
resposta = s.recv(1024).decode('latin-1')
lista = resposta.split()
whois = lista[19]
s.close()

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((whois,43))
s1.send(str.encode(sys.argv[1]+"\r\n"))
resposta2 = s1.recv(1024).decode('latin-1')
print(resposta2)
