import tkinter as tk

class LoginView(tk.Frame):
    def __init__(self, master, servicio, cambiar_vista):
        super().__init__(master)
        self.servicio = servicio
        self.cambiar_vista = cambiar_vista

        tk.Label(self, text="Usuario").pack()
        self.username = tk.Entry(self)
        self.username.pack()

        tk.Label(self, text="Contraseña").pack()
        self.password = tk.Entry(self, show="*")
        self.password.pack()

        self.mensaje = tk.Label(self, text="")
        self.mensaje.pack()

        tk.Button(self, text="Ingresar", command=self.login).pack()

    def login(self):
        if self.servicio.validar_usuario(self.username.get(), self.password.get()):
            self.cambiar_vista("main")
        else:
            self.mensaje.config(text="Credenciales incorrectas")
