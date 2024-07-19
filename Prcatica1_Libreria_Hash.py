import hashlib

texto = "Hola, mi nombre es elizabeth!"
hash_obj = hashlib.sha256(texto.encode())
hash_hex = hash_obj.hexdigest()

print("Hash SHA-256 de 'Hola, mi nombre es elizabeth!':", hash_hex)
