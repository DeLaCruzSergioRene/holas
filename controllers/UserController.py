from models.UserModel import UsuarioModel
from models.schemasModel import UsuarioSchema, UsuarioLogin
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()

    def login(self, email, password):
        user = self.model.validar_login(email, password)
        if user:
            return user, "Login exitoso"
        else:
            return None, "Credenciales inválidas"
    
    def registrar_usuario(self, nombre, email, password):
        try:
            # Validar datos con el Schema
            usuario_data = UsuarioSchema(nombre=nombre, email=email, password=password)
            success = self.model.registrar(usuario_data)
            if success:
                return True, "Usuario creado correctamente"
            return False, "No se pudo crear el usuario"
        except ValidationError as e:
            # Retorna el primer error de validación encontrado
            return False, e.errors()[0]['msg']