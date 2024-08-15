#!/bin/bash

#script para encontrar arquivos na internet de um determinado site, alvo.com pdf (qualquer extensão)
lynx -dump "http://google.com/search?num=500&q=site:"$1"+ext:"$2"" | cut -d "=" -f2 | grep ".$2" | egrep -v "site|google" | sed s'/...$//'g
