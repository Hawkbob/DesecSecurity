#!/usr/bin/python3
import sys
from scapy.all import *

#Com o valor em 0 eculta a informação inicial do Scapy, se trocar para 1 volta ao padrão
conf.verb = 0

#Pode ser adicionado a quantidade de portas que quiser, ou carregar uma lista, ou uma sequencia de 1 a 65536
portas = [21,22,23,25,80,443,8080,110]

#variaveis e pacote
pIP = IP(dst=sys.argv[1])
pTCP = TCP(sport=65000, dport=portas, flags="S")
pacote = pIP/pTCP

#resp pega a resposta e noresp a porta que nao respondeu
resp, noresp = sr(pacote)

for resposta in resp:
#Variaveis porta e flag para obtermos os resultados que queremos. 
  porta =  resposta[1][TCP].sport
        flag = resposta[1][TCP].flags
        if (flag == "SA"):
                print (f"Porta {porta} ABERTA")
