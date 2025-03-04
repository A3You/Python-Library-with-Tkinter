from tkinter import *
from tkinter.ttk import *
def styles():

    style = Style()

    style.theme_use("clam")

    style.configure(
        "Treeview",
        background="#f0f0f0",
        foreground="#2e2e2e",
        fieldbackground="#f0f0f0",
        font=("Poppins", 12),
    )

    style.configure(
        "Treeview.Heading",
        background="#3498db",
        foreground="#ffffff",
        font=("Poppins", 12, "bold"),
    )

    style.map(
        "Treeview",
        background=[
            ("selected", "#3498db"),
        ],
        foreground=[
            ("selected", "#ffffff"),
        ],
    )