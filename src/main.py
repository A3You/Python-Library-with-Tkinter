from BaseView import BaseView
from libros.LibrosController import LibrosController


class App(BaseView):
    def __init__(self):
        super().__init__()
        self.controller = LibrosController(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()
