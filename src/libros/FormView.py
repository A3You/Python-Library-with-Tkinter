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
        
        Label(form_frame, text="Stock:").grid(row=2, column=0, sticky=W)
        self.stock_entry = Entry(form_frame)
        self.stock_entry.grid(row=2, column=1, sticky=EW)
        
        # Botones
        btn_frame = Frame(self)
        btn_frame.pack(pady=10)
        
        Button(btn_frame, text="Guardar", command=self._save).pack(side=LEFT, padx=5)
        Button(btn_frame, text="Cancelar", command=self._cancel).pack(side=RIGHT)
        
    def _save(self):
        data = {
            'name': self.name_entry.get(),
            'price': self.price_entry.get(),
            'stock': self.stock_entry.get()
        }
        if self.controller:
            if self.current_id:
                self.controller.update_product(self.current_id, data)
            else:
                self.controller.create_product(data)
    
    def _cancel(self):
        if self.controller:
            self.controller.show_list_view()

