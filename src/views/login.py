from tkinter import *
from tkinter import ttk

class LoginView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label_username = ttk.Label(self, text="Nombre de Usuario:")
        self.label_password = ttk.Label(self, text="Contraseña:")
        self.entry_username = ttk.Entry(self)
        self.entry_password = ttk.Entry(self, show="*")
        self.button_login = ttk.Button(self, text="Iniciar Sesión")

        self.label_username.grid(row=0, column=0, padx=5, pady=5)
        self.entry_username.grid(row=0, column=1, padx=5, pady=5)
        self.label_password.grid(row=1, column=0, padx=5, pady=5)
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)
        self.button_login.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.controller = None
    