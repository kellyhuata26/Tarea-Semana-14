from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        self.productos = []
        self.usuarios = []

    def cargar_datos(self):
        productos_data = ArchivoServicio.leer_json("restaurante_app/datos/productos.json")
        usuarios_data = ArchivoServicio.leer_json("restaurante_app/datos/usuarios.json")

        self.productos = [Producto(p["nombre"], p["precio"], p["cantidad"]) for p in productos_data]
        self.usuarios = [Usuario(u["username"], u["password"]) for u in usuarios_data]

    def validar_usuario(self, username, password):
        for u in self.usuarios:
            if u.username == username and u.password == password:
                return True
        return False

    def listar_productos(self):
        return self.productos

    def listar_usuarios(self):
        return self.usuarios
