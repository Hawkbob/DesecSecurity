#!/bin/bash

clear
echo -e "\e[1;37m" 

echo " ##::::'##::::'###::::'##:::::'##:'##:::'##::'######:::'######:::::'###::::'##::: ##:"
echo " ##:::: ##:::'## ##::: ##:'##: ##: ##::'##::'##... ##:'##... ##:::'## ##::: ###:: ##:"
echo " ##:::: ##::'##:. ##:: ##: ##: ##: ##:'##::: ##:::..:: ##:::..:::'##:. ##:: ####: ##:"
echo " #########:'##:::. ##: ##: ##: ##: #####::::. ######:: ##:::::::'##:::. ##: ## ## ##:"
echo " ##.... ##: #########: ##: ##: ##: ##. ##::::..... ##: ##::::::: #########: ##. ####:"
echo " ##:::: ##: ##.... ##: ##: ##: ##: ##:. ##::'##::: ##: ##::: ##: ##.... ##: ##:. ###:"
echo " ##:::: ##: ##:::: ##:. ###. ###:: ##::. ##:. ######::. ######:: ##:::: ##: ##::. ##:"
echo "..:::::..::..:::::..:::...::...:::..::::..:::......::::......:::..:::::..::..::::..::"

echo "                                                                           By Hawkbob"


echo -e "\e[0m"  # Resetar cor
echo -e "\e[1;32m[+] Hawkscan carregado! Preparando a ferramenta...\e[0m"
sleep 2

for palavra in $(cat $2)
do
        resposta=$(curl -s -L -H "User-Agent: Hawkbobv1.1" -o /dev/null -w "%{http_code}" $1/$palavra/)

        if [ "$resposta" == "200" ]; then

                echo -ne "\r\033[K"
                echo "Diretorio Encontrado: $1/$palavra/"

        elif [ "$resposta" == "301" ]; then
        echo -ne "\r\033[K"
        echo "Redirecionamento Encontrado (301): $1/$palavra/"

        else
                echo -ne "\r\033[KRealizando Scan: $1/$palavra/"
        fi
done

echo ""
