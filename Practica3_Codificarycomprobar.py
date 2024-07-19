import hashlib

import os

# Definir las rutas de los archivos
file_path1 = "Documentos/Archivo1.txt"
file_path2 = "Documentos/Documento2.txt"

# Crear el directorio "Documentos" si no existe
if not os.path.exists("Documentos"):
    os.makedirs("Documentos")

# Crear y escribir algo en Archivo1.txt si no existe
if not os.path.exists(file_path1):
    with open(file_path1, 'w') as file:
        file.write("Este es el contenido del Archivo1.\n")

# Crear y escribir algo en Documento2.txt si no existe
if not os.path.exists(file_path2):
    with open(file_path2, 'w') as file:
        file.write("Este es el contenido del Documento2.\n")

print("Archivos creados correctamente.")

def generate_md5_hash(file_path1, file_path2):
    md5_obj1 = hashlib.md5()
    md5_obj2 = hashlib.md5()

    with open(file_path1, 'rb') as file1:
        while chunk := file1.read(8192):
            md5_obj1.update(chunk)

    with open(file_path2, 'rb') as file2:
        while chunk := file2.read(8192):
            md5_obj2.update(chunk)

    hash1 = md5_obj1.hexdigest()
    hash2 = md5_obj2.hexdigest()

    print("Hash del archivo 1:", hash1)
    print("Hash del archivo 2:", hash2)

    return hash1 == hash2

file_path1 = "documentos/archivo1.txt"
file_path2 = "documentos/documento2.txt"  

if os.path.exists(file_path1) and os.path.exists(file_path2):
    son_iguales = generate_md5_hash(file_path1, file_path2)
    print("¿Los archivos son iguales?:", son_iguales)
else:
    print("Al menos uno de los archivos no existe.")