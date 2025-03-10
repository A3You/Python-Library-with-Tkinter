from tkinter import *
from tkinter.ttk import *


class FormView(Frame):
    # styles()
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        self.current_id = None
        self.nombre = None
        self.apellidos = None
        self.fecha_nacimiento = None
        self.nacionalidad = None
        self.fecha_fallecimiento = None

    def set_controller(self, controller):
        self.controller = controller

    def create_widgets(self):
        self.form_frame = Toplevel(self)
        self.form_frame.transient(self)
        
        
        screen_width = self.form_frame.winfo_screenwidth()
        screen_height = self.form_frame.winfo_screenheight()
        width = 400
        height = 350
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.form_frame.geometry('%dx%d+%d+%d' % (width, height, x, y))
        
        self.form_frame.padding = 5
        
        Label(self.form_frame, text="Nombre:").pack(pady=self.form_frame.padding)                      
        self.nombre = StringVar()
        self.nombre_entry = Entry(self.form_frame, textvariable=self.nombre)
        self.nombre_entry.pack()
        
        Label(self.form_frame, text="Apellidos:").pack(pady=self.form_frame.padding)
        self.apellidos = StringVar()
        self.apellidos_entry = Entry(self.form_frame, textvariable=self.apellidos)
        self.apellidos_entry.pack()
        

        Label(self.form_frame, text="Nacionalidad:").pack(pady=self.form_frame.padding)
        self.nacionalidad = StringVar()
        self.nacionalidad_entry = Entry(self.form_frame, textvariable=self.nacionalidad)
        self.nacionalidad_entry.pack()

        Label(self.form_frame, text="Fecha Nacimiento:").pack(pady=self.form_frame.padding)
        self.fecha_nacimiento = StringVar()
        self.fecha_nacimiento_entry = Entry(self.form_frame, textvariable=self.fecha_nacimiento)
        self.fecha_nacimiento_entry.pack()

        Label(self.form_frame, text="Fecha Fallecimiento:").pack(pady=self.form_frame.padding)
        self.fecha_fallecimiento = StringVar()
        self.fecha_fallecimiento_entry = Entry(self.form_frame, textvariable=self.fecha_fallecimiento)
        self.fecha_fallecimiento_entry.pack()
        # Botones
        Button(self.form_frame, text="Guardar", command=self._save).pack(pady=self.form_frame.padding)
        Button(self.form_frame, text="Cancelar", command=self._cancel).pack(pady=self.form_frame.padding)
        

    def _save(self):
        data = {
            'nombre': self.nombre_entry.get(),
            'apellidos': self.apellidos_entry.get(),
            'fecha_nacimiento': self.fecha_nacimiento_entry.get(),
            'nacionalidad': self.nacionalidad_entry.get(),
            'fecha_fallecimiento': self.fecha_fallecimiento_entry.get()
        }
        if self.controller:
            if self.current_id:
                self.controller.guardar_autor(
                    current_id=self.current_id,
                    nombre=data['nombre'],
                    apellidos=data['apellidos'],
                    fecha_nacimiento=data['fecha_nacimiento'],
                    nacionalidad=data['nacionalidad'],
                    fecha_fallecimiento=data['fecha_fallecimiento']
                )
            else:
                self.controller.guardar_autor(
                    nombre=data['nombre'],
                    apellidos=data['apellidos'],
                    fecha_nacimiento=data['fecha_nacimiento'],
                    nacionalidad=data['nacionalidad'],
                    fecha_fallecimiento=data['fecha_fallecimiento']
                )

        self.form_frame.destroy()
            

    def _cancel(self):
        self.form_frame.destroy()

    def load_data(self, autor, autores_ids):
        try:
            # Si es una lista, extraer el primer elemento
            if isinstance(autor, list):
                autor = autor[0]
                
            self.current_id = autor['id']
            self.nombre.set(autor.get('nombre', ''))
            self.apellidos.set(autor.get('apellidos', ''))
            self.fecha_nacimiento.set(autor.get('fecha_nacimiento', ''))
            self.nacionalidad.set(autor.get('nacionalidad', ''))
            self.fecha_fallecimiento.set(autor.get('fecha_fallecimiento', ''))
            
        except (AttributeError, KeyError) as e:
            print(f"Error al mostrar el formulario: {e}")

        except AttributeError as e:
            print(f"Error al mostrar el formulario: {e}")

