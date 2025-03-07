from tkinter import *
from tkinter.ttk import *
from tkcalendar import DateEntry



class FormView(Frame):
    # styles()
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        self.current_id = None
        self.titulo = None
        self.precio = None
        self.combo_editorial = None  
        self.id_editorial = None
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
        height = 400
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
        
        Label(self.form_frame, text="Editorial:").pack(pady=self.form_frame.padding)        
        self.combo_editorial = Combobox(self.form_frame, state="readonly")
        self.combo_editorial.pack(pady=self.form_frame.padding)
     
        if self.controller:
            editoriales = self.controller.obtener_editoriales()
            self.combo_editorial['values'] = [f"{e['nombre']} (ID: {e['id']})" for e in editoriales]
            self.editoriales_data = {e['id']: f"{e['nombre']} (ID: {e['id']})" for e in editoriales}
        
        Label(self.form_frame, text="Fecha Publicación:").pack(pady=self.form_frame.padding)
        self.fecha_publicacion = DateEntry(self.form_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.fecha_publicacion.pack(pady=self.form_frame.padding)
        
        Label(self.form_frame, text="Asignar Autores:").pack(pady=self.form_frame.padding)
        autores_frame = Frame(self.form_frame)
        autores_frame.pack(pady=self.form_frame.padding)
        
        scrollbar = Scrollbar(autores_frame, orient=VERTICAL)
        self.autores_listbox = Listbox(
            autores_frame, 
            selectmode=MULTIPLE, 
            yscrollcommand=scrollbar.set,
            height=5
        )
        scrollbar.config(command=self.autores_listbox.yview)
        
        self.autores_listbox.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # Cargar autores desde el controlador
        if self.controller:
            autores = self.controller.obtener_autores()
            for autor in autores:
                self.autores_listbox.insert(END, f"{autor['apellidos']}, {autor['nombre']} (ID: {autor['id']})")
        # Botones
        Button(self.form_frame, text="Guardar", command=self._save).pack(pady=self.form_frame.padding)
        Button(self.form_frame, text="Cancelar", command=self._cancel).pack(pady=self.form_frame.padding)
        
    def set_controller(self, controller):
        self.controller = controller


    def _save(self):
        selected_indices = self.autores_listbox.curselection()
        autores_ids = [self.autores_listbox.get(idx).split(' (ID: ')[1].split(')')[0] for idx in selected_indices]
        editorial_text = self.combo_editorial.get()
        editorial_id = None
        if editorial_text and self.controller:
            for eid, text in self.editoriales_data.items():
                if text == editorial_text:
                    editorial_id = eid
                    break
        data = {
            'titulo': self.titulo_entry.get(),
            'precio': self.price_entry.get(),
            'id_editorial': editorial_id,  
            'fecha_publicacion': self.fecha_publicacion.get(),
            'autores': autores_ids  
        }
        if self.controller:
            if self.current_id:
                self.controller.guardar_libro(  
                    self.current_id,
                    data['titulo'],
                    data['precio'],
                    data['id_editorial'],  
                    data['fecha_publicacion'],
                    data['autores']
                )
            else:
                self.controller.guardar_libro(
                    data['titulo'],
                    data['precio'],
                    data['id_editorial'],  
                    data['fecha_publicacion'],
                    data['autores']
                )
    
    def _cancel(self):
        self.form_frame.destroy()

    def load_data(self, libro, autores_ids):
        try:
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

            if self.controller:
                    all_autores = self.controller.obtener_autores()
                    for idx, autor in enumerate(all_autores):
                        if autor['id'] in autores_ids:
                            self.autores_listbox.selection_set(idx)

            if libro['id_editorial'] and self.controller:
                    editorial_id = libro['id_editorial']
                    display_text = self.editoriales_data.get(editorial_id, "")
                    self.combo_editorial.set(display_text)

        except AttributeError as e:
            print(f"Error al mostrar el formulario: {e}")

