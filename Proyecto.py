import hashlib
import os
import sqlite3

# Función para generar hash seguro de contraseñas
def hash_password(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + key

# Función para verificar contraseña
def verify_password(stored_password, provided_password):
    salt = stored_password[:32]
    stored_password = stored_password[32:]
    key = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
    return key == stored_password

# Función para calcular hash de archivo
def calculate_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        buffer = file.read(65536)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = file.read(65536)
    return hasher.hexdigest()

# Función para conectar a la base de datos y agregar columna de hash
def add_hash_column_to_db(db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f'ALTER TABLE {table_name} ADD COLUMN hash TEXT')
    conn.commit()
    conn.close()

# Función para calcular hash de registro en la base de datos
def calculate_db_record_hash(record):
    hasher = hashlib.sha256()
    for field in record:
        hasher.update(str(field).encode('utf-8'))
    return hasher.hexdigest()

# Función para enviar archivo con verificación de integridad
def send_file_with_integrity_verification(file_path, receiver):
    file_hash_before = calculate_file_hash(file_path)
    # Aquí se implementaría el envío del archivo a 'receiver'
    # Después del envío, se recibiría el archivo y se calcularía su hash
    file_hash_after = calculate_file_hash(received_file_path)
    return file_hash_before == file_hash_after

# Interfaz de usuario (ejemplo básico)
def main():
    print("1. Registro")
    print("2. Iniciar sesión")
    choice = input("Seleccione una opción: ")

    if choice == "1":
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        hashed_password = hash_password(password)
        # Aquí se almacenaría el nombre de usuario y la contraseña en la base de datos

    elif choice == "2":
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        # Aquí se verificaría la autenticidad del nombre de usuario y la contraseña

    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
