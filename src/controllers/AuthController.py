from tkinter import  *
from views.login import LoginView


class AuthController:
    def __init__(self, model, view):
        self.view = view
        self.model = model

    def login(self):