import mysql.connector
import hashlib

class PasswordManagerCLI:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'sasa'
        self.database = 'base_de_usuarios'
        
        self.password_manager = PasswordManager(self.host, self.user, self.password, self.database)
        
    def display_menu(self):
        print("Bienvenido al Administrador de Contraseñas")
        print("1. Agregar Usuario")
        print("2. Verificar Contraseña")
        print("3. Mostrar Usuarios")
        print("4. Eliminar Usuario")
        print("5. Modificar Contraseña")
        print("0. Salir")
        
    def run(self):
        while True:
            self.display_menu()
            choice = input("Ingrese el número de la opción que desea realizar: ")
            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.verify_password()
            elif choice == '3':
                self.show_users()
            elif choice == '4':
                self.delete_user()
            elif choice == '5':
                self.update_password()
            elif choice == '0':
                print("Bai")
                break
            else:
                print("Numero no valido.")
    
    def add_user(self):
        username = input("Ingrese el nombre de usuario: ")
        password = input("Ingrese la contraseña: ")
        self.password_manager.add_user(username, password)
        print("Usuario agregado exitosamente.")
        
    def verify_password(self):
        username = input("Ingrese el nombre de usuario: ")
        password = input("Ingrese la contraseña: ")
        if self.password_manager.verify_password(username, password):
            print("La contraseña es correcta.")
        else:
            print("Usuario o contraseña incorrecta.")
            
    def show_users(self):
        users = self.password_manager.show_users()
        print("Usuarios Registrados:")
        for user in users:
            print(user)
    
    def delete_user(self):
        username = input("Ingrese el nombre de usuario que desea eliminar: ")
        self.password_manager.delete_user(username)
        print("Usuario eliminado exitosamente.")
        
    def update_password(self):
        username = input("Ingrese el nombre de usuario: ")
        new_password = input("Ingrese la nueva contraseña: ")
        self.password_manager.update_password(username, new_password)
        print("Contraseña actualizada exitosamente.")

class PasswordManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        self.create_table()
        
    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS usuarios (
            username VARCHAR(255) PRIMARY KEY,
            password_hash VARCHAR(32)
        )
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()
    
    def add_user(self, username, password):
        password_hash = self.generate_md5_hash(password)
        insert_query = "INSERT INTO usuarios (username, password_hash) VALUES (%s, %s)"
        self.cursor.execute(insert_query, (username, password_hash))
        self.connection.commit()
    
    def verify_password(self, username, password):
        select_query = "SELECT password_hash FROM usuarios WHERE username = %s"
        self.cursor.execute(select_query, (username,))
        result = self.cursor.fetchone()
        if result:
            password_hash_from_db = result[0]
            return password_hash_from_db == self.generate_md5_hash(password)
        return False
    
    def show_users(self):
        select_query = "SELECT * FROM usuarios"
        self.cursor.execute(select_query)
        users = self.cursor.fetchall()3
        return users
    
    def delete_user(self, username):
        delete_query = "DELETE FROM usuarios WHERE username = %s"
        self.cursor.execute(delete_query, (username,))
        self.connection.commit()
    
    def update_password(self, username, new_password):
        password_hash = self.generate_md5_hash(new_password)
        update_query = "UPDATE usuarios SET password_hash = %s WHERE username = %s"
        self.cursor.execute(update_query, (password_hash, username))
        self.connection.commit()
    
    def generate_md5_hash(self, password):
        md5_obj = hashlib.md5()
        md5_obj.update(password.encode())
        return md5_obj.hexdigest()

def main():
    # Otorgar permisos necesarios en MySQL
    grant_permissions()
    # Iniciar la aplicación
    password_manager_cli = PasswordManagerCLI()
    password_manager_cli.run()

def grant_permissions():
    try:
        connection = mysql.connector.connect(
            host='',
            user='root',
            password='sasa',
            database='base_de_usuarios'
        )
        cursor = connection.cursor()
        cursor.execute("GRANT SELECT, INSERT, UPDATE, DELETE ON base_de_usuarios.usuarios TO 'root'@'localhost';")
        connection.commit()
        print("Permisos otorgados correctamente.")
    except mysql.connector.Error as error:
        print(f"Error al otorgar permisos: {error}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    main()
    
