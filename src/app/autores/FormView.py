from tkinter import *
from tkinter.ttk import *


class FormView(Frame):
    # styles()
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        self.current_id = None
        self.titulo = None
        self.precio = None
        self.id_editorial = None
        self.editorial = None
        self.fecha_publicacion = None
        self.autores = None

        self.create_widgets()

    def create_widgets(self):
        # Campos del formulario
        form_frame = Frame(self)
        form_frame.pack(pady=20, padx=20, fill=X)
        
        Label(form_frame, text="Nombre:").pack()                        
        self.titulo = StringVar()
        self.titulo_entry = Entry(form_frame, textvariable=self.titulo)
        self.titulo_entry.pack()
        
        Label(form_frame, text="Precio:").pack()
        self.precio = StringVar()
        self.price_entry = Entry(form_frame, textvariable=self.precio)
        self.price_entry.pack()
        
        Label(form_frame, text="Editorial (ID):").pack()
        self.id_editorial = StringVar()
        self.id_editorial_entry = Entry(form_frame, textvariable=self.id_editorial)
        self.id_editorial_entry.pack()

        Label(form_frame, text="Editorial:").pack()
        self.editorial = StringVar()
        self.editorial_entry = Entry(form_frame, textvariable=self.editorial, state='readonly')
        self.editorial_entry.pack()

        Label(form_frame, text="Fecha Publicación:").pack()
        self.fecha_publicacion = StringVar()
        self.fecha_entry = Entry(form_frame, textvariable=self.fecha_publicacion)
        self.fecha_entry.pack()
        
        Label(form_frame, text="Autores:").pack()
        self.autores = StringVar()
        self.autores_entry = Entry(form_frame, textvariable=self.autores)
        self.autores_entry.pack()
        # Botones
        Button(form_frame, text="Guardar", command=self._save).pack()
        Button(form_frame, text="Cancelar", command=self._cancel).pack()
        
    def set_controller(self, controller):
        self.controller = controller

    def _save(self):
        data = {
            'titulo': self.titulo_entry.get(),  # Cambia 'name' a 'titulo'
            'precio': self.price_entry.get(),
            'editorial': self.editorial_entry.get(),
            'fecha_publicacion': self.fecha_entry.get(),
            'autores': [int(a) for a in self.autores_entry.get().split(',')]
        }
        if self.controller:
            if self.current_id:
                self.controller.guardar_libro(  
                    self.current_id,
                    data['titulo'],
                    data['precio'],
                    data['editorial'],
                    data['fecha_publicacion'],
                    data['autores']
                )
            else:
                self.controller.guardar_libro(
                    data['titulo'],
                    data['precio'],
                    data['editorial'],
                    data['fecha_publicacion'],
                    data['autores']
                )
        
    def _cancel(self):
        if self.controller:
            self.pack_forget()
            self.controller.show_list_view()

    def load_data(self, libro, autores_ids):
        print(f"Creando Formulario {libro[0]['id']}")
        try:            # Asegúrate de que 'libro' es un diccionario
            if isinstance(libro, list):
                libro = libro[0]
                self.current_id = libro['id']
                self.titulo.set(libro['titulo'])
                self.precio.set(libro['precio'])
                self.id_editorial.set(libro['id_editorial'])
                self.editorial.set(libro['editorial'])
                self.fecha_publicacion.set(libro['fecha_publicacion'])
                self.autores.set(libro['autores'])
                self.pack(fill="x", expand=True)

        except AttributeError as e:
            print(f"Error al mostrar el formulario: {e}")

