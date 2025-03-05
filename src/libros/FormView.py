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
        
        Label(form_frame, text="Nombre:").grid(row=0, column=0, sticky=W)
        self.name_entry = Entry(form_frame)
        self.name_entry.grid(row=0, column=1, sticky=EW)
        
        Label(form_frame, text="Precio:").grid(row=1, column=0, sticky=W)
        self.price_entry = Entry(form_frame)
        self.price_entry.grid(row=1, column=1, sticky=EW)
        
        Label(form_frame, text="Editorial (ID):").grid(row=2, column=0, sticky=W)
        self.editorial_entry = Entry(form_frame)
        self.editorial_entry.grid(row=2, column=1, sticky=EW)

        Label(form_frame, text="Fecha Publicación:").grid(row=3, column=0, sticky=W)
        self.fecha_entry = Entry(form_frame)
        self.fecha_entry.grid(row=3, column=1, sticky=EW)
        
        Label(form_frame, text="Autores (IDs separados por coma):").grid(row=4, column=0, sticky=W)
        self.autores_entry = Entry(form_frame)
        self.autores_entry.grid(row=4, column=1, sticky=EW)
        
        # Botones
        btn_frame = Frame(self)
        btn_frame.pack(pady=10)
        
        Button(btn_frame, text="Guardar", command=self._save).pack(side=LEFT, padx=5)
        Button(btn_frame, text="Cancelar", command=self._cancel).pack(side=RIGHT, padx=5)
        
    def _save(self):
        data = {
            'titulo': self.name_entry.get(),  # Cambia 'name' a 'titulo'
            'precio': self.price_entry.get(),
            'editorial': self.editorial_entry.get(),
            'fecha_publicacion': self.fecha_entry.get(),
            'autores': self.autores_entry.get()
        }
        if self.controller:
            if self.current_id:
                self.controller.guardar_libro(  # Usa guardar_libro, no update_product
                    self.current_id,
                    data['titulo'],
                    data['precio'],
                    data['editorial'],
                    data['fecha_publicacion'],
                    data['autores'].split(',')
                )
            else:
                self.controller.guardar_libro(
                    data['titulo'],
                    data['precio'],
                    data['editorial'],
                    data['fecha_publicacion'],
                    data['autores'].split(',')
                )
        
    def _cancel(self):
        if self.controller:
            self.controller.listar_libros()
            
    def load_data(self, libro):
        self.current_id = libro['id']
        self.name_entry.insert(0, libro.get('titulo', ''))
        self.price_entry.insert(0, str(libro.get('precio', '')))
        self.editorial_entry.insert(0, str(libro.get('id_editorial', '')))
        self.fecha_entry.insert(0, libro.get('fecha_publicacion', ''))
        # Cargar autores (requiere consulta adicional)
        autores = self.controller.model.obtener_autores_libro(self.current_id)
        self.autores_entry.insert(0, ", ".join(str(a['id']) for a in autores))

