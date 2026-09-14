import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Restaurante App")
        self.servicio = RestauranteServicio()
        self.servicio.cargar_datos()
        self.vista_actual = None
        self.cambiar_vista("login")

    def cambiar_vista(self, vista):
        if self.vista_actual:
            self.vista_actual.destroy()
        if vista == "login":
            self.vista_actual = LoginView(self, self.servicio, self.cambiar_vista)
        elif vista == "main":
            self.vista_actual = MainView(self, self.servicio, self.cambiar_vista)
        self.vista_actual.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
