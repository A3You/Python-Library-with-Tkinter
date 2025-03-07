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

    def create_widgets(self):
        # Campos del formulario
        self.form_frame = Toplevel(self)
        self.form_frame.transient(self)
        
        # Centrar en la pantalla
        screen_width = self.form_frame.winfo_screenwidth()
        screen_height = self.form_frame.winfo_screenheight()
        width = 400
        height = 420
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.form_frame.geometry('%dx%d+%d+%d' % (width, height, x, y))
        
        self.form_frame.padding = 3
        
        Label(self.form_frame, text="Nombre:").pack(pady=self.form_frame.padding)                        
        self.titulo = StringVar()
        self.titulo_entry = Entry(self.form_frame, textvariable=self.titulo)
        self.titulo_entry.pack(pady=self.form_frame.padding)
        
        Label(self.form_frame, text="Precio:").pack(pady=self.form_frame.padding)
        self.precio = StringVar()
        self.price_entry = Entry(self.form_frame, textvariable=self.precio)
        self.price_entry.pack(pady=self.form_frame.padding)
        
        Label(self.form_frame, text="Editorial (ID):").pack(pady=self.form_frame.padding)
        self.id_editorial = StringVar()
        self.id_editorial_entry = Entry(self.form_frame, textvariable=self.id_editorial)
        self.id_editorial_entry.pack(pady=self.form_frame.padding)

        Label(self.form_frame, text="Editorial:").pack(pady=self.form_frame.padding)
        self.editorial = StringVar()
        self.editorial_entry = Entry(self.form_frame, textvariable=self.editorial, state='readonly')
        self.editorial_entry.pack(pady=self.form_frame.padding)

        Label(self.form_frame, text="Fecha Publicación:").pack(pady=self.form_frame.padding)
        self.fecha_publicacion = StringVar()
        self.fecha_entry = Entry(self.form_frame, textvariable=self.fecha_publicacion)
        self.fecha_entry.pack(pady=self.form_frame.padding)
        
        Label(self.form_frame, text="Autores:").pack(pady=self.form_frame.padding)
        self.autores = StringVar()
        self.autores_entry = Entry(self.form_frame, textvariable=self.autores)
        self.autores_entry.pack(pady=self.form_frame.padding)
        # Botones
        Button(self.form_frame, text="Guardar", command=self._save).pack(pady=self.form_frame.padding)
        Button(self.form_frame, text="Cancelar", command=self._cancel).pack(pady=self.form_frame.padding)
        
    def set_controller(self, controller):
        self.controller = controller


    def _save(self):
        data = {
            'titulo': self.titulo_entry.get(),
            'precio': self.price_entry.get(),
            'id_editorial': self.id_editorial.get(),  # <- Cambiado aquí
            'fecha_publicacion': self.fecha_entry.get(),
            'autores': [int(a) for a in self.autores_entry.get().split(',')]
        }
        if self.controller:
            if self.current_id:
                self.controller.guardar_libro(  
                    self.current_id,
                    data['titulo'],
                    data['precio'],
                    data['id_editorial'],  # <- Asegurar que se envía el ID
                    data['fecha_publicacion'],
                    data['autores']
                )
            else:
                self.controller.guardar_libro(
                    data['titulo'],
                    data['precio'],
                    data['id_editorial'],  # <- Aquí también
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

