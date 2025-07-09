import hashlib
import base64
import time


# Esse script pega palavras e encripta em md5 - base64 - sha1 e compara as senhas
target_hash = "hash aqui"
wordlist_path = "wordlist.txt" 

def process(password: str) -> str:
    # 1. MD5 como string hexa
    md5_hex = hashlib.md5(password.encode()).hexdigest()

    # 2. Base64 da string hexa (como você fez com echo/base64)
    b64_encoded = base64.b64encode(md5_hex.encode()).decode()

    # 3. SHA1 da base64 (string final)
    sha1 = hashlib.sha1(b64_encoded.encode()).hexdigest()

    return sha1

start_time = time.time()
count = 0

with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        pwd = line.strip()
        count += 1
        result = process(pwd)
        if result == target_hash:
            elapsed = time.time() - start_time
            print(f"[✅] SENHA ENCONTRADA: {pwd}")
            print(f"[⏱️] Tentativas: {count} | Tempo: {elapsed:.2f}s")
            break
        if count % 1000 == 0:
            print(f"[...] {count} senhas testadas...")
    else:
        print("[-] Nenhuma senha bateu com o hash.")
