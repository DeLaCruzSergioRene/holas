import bcrypt
from .database import Database

# Modelo para operaciones de usuario
class UsuarioModel:
    def __init__(self):
        self.db = Database()

    def registrar(self, usuario_data):
        # Encriptar contraseña antes de guardar
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(usuario_data.password.encode('utf-8'), salt)

        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuario (nombre, email, password) VALUES (%s, %s, %s)",
                (usuario_data.nombre, usuario_data.email, hashed_pw.decode('utf-8'))
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    def validar_login(self, email, password):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE email=%s", (email,))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            try:
                # Convertir la contraseña guardada a bytes si es string
                stored_hash = user['password']
                # Comparar contraseña ingresada con la guardada
                if isinstance(stored_hash, str):
                    stored_hash = stored_hash.encode('utf-8')
                
                if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
                    return user
            except Exception as e:
                print(f"Error en validación de contraseña: {e}")
                return None
        return None