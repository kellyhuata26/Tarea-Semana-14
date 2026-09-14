import tkinter as tk

class MainView(tk.Frame):
    def __init__(self, master, servicio, cambiar_vista):
        super().__init__(master)
        self.servicio = servicio
        self.cambiar_vista = cambiar_vista

        tk.Label(self, text="Usuarios registrados").pack()
        for u in self.servicio.listar_usuarios():
            tk.Label(self, text=u.username).pack()

        tk.Label(self, text="Productos disponibles").pack()
        for p in self.servicio.listar_productos():
            tk.Label(self, text=f"{p.nombre} - {p.precio} USD - {p.cantidad} unidades").pack()

        tk.Button(self, text="Cerrar sesión", command=lambda: self.cambiar_vista("login")).pack()
