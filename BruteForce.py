#!/usr/bin/python
import socket,sys,re
import time

file = open("lista.txt")
for linha in file:

        print("Realizano conexão, aguarde..")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((sys.argv[1],25))
        banner = s.recv(1024)

        print("Aguarde, Verificando..")
        time.sleep(5)

        print("Enviando VRFY")
        s.send(str.encode("VRFY"+linha))
        user = s.recv(1024)
        if re.search("252",user):
                print("Usuário encontrado {user}")

sock.close()
