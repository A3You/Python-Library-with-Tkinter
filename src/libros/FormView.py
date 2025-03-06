from tkinter import *
from tkinter.ttk import *


class FormView(Frame):
    # styles()
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        self.current_id = None
        self._create_widgets()
    
    def set_controller(self, controller):
        self.controller = controller

    def _create_widgets(self):
        # Campos del formulario
        form_frame = Frame(self)
        form_frame.pack(pady=20, padx=20, fill=X)
        
        Label(form_frame, text="Nombre:").pack()
        self.titulo_entry = Entry(form_frame)
        self.titulo_entry.pack()
        
        Label(form_frame, text="Precio:").pack()
        self.price_entry = Entry(form_frame)
        self.price_entry.pack()
        
        Label(form_frame, text="Editorial (ID):").pack()
        self.id_editorial_entry = Entry(form_frame)
        self.id_editorial_entry.pack()

        Label(form_frame, text="Editorial:").pack()
        self.editorial_entry = Entry(form_frame)
        self.editorial_entry.pack()

        Label(form_frame, text="Fecha Publicación:").pack()
        self.fecha_entry = Entry(form_frame)
        self.fecha_entry.pack()
        
        Label(form_frame, text="Autores (IDs separados por coma):").pack()
        self.autores_entry = Entry(form_frame)
        self.autores_entry.pack()
        
        # Botones
        btn_frame = Frame(self)
        btn_frame.pack(pady=10)
        
        Button(btn_frame, text="Guardar", command=self._save).pack(side=LEFT, padx=5)
        Button(btn_frame, text="Cancelar", command=self._cancel).pack(side=RIGHT, padx=5)
        
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
            self.controller.show_list_view()

    def load_data(self, libro):
        print(f"Creando Formulario {libro[0]['id']}")
        try:            # Asegúrate de que 'libro' es un diccionario
            if isinstance(libro, list):
                libro = libro[0]
                titulo = libro['titulo']
                precio = libro['precio']
                id_editorial = libro['id_editorial']
                editorial = libro['editorial']
                fecha_publicacion = libro['fecha_publicacion']
                autores = libro['autores']
            self.current_id = libro["id"]
            self.titulo_entry.delete(0, END)
            self.titulo_entry.insert(0, titulo)
            print(self.titulo_entry.get())
            self.price_entry.delete(0, END)
            self.price_entry.insert(0, precio)
            print(self.price_entry.get())
            self.id_editorial_entry.delete(0, END)
            self.id_editorial_entry.insert(0, id_editorial)
            
            self.editorial_entry.delete(0, END)
            self.editorial_entry.insert(0, editorial)
            self.fecha_entry.delete(0, END)
            self.fecha_entry.insert(0, fecha_publicacion)
            self.autores_entry.delete(0, END)
            self.autores_entry.insert(0, autores)
        except AttributeError as e:
            print(f"Error al mostrar el formulario: {e}")