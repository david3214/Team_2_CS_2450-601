import tkinter as tk
from tkinter import ttk

class UnderlineEntry(tk.Entry):
    def __init__(self, *args, **kwargs):
        kwargs["borderwidth"] = 0
        kwargs["cursor"] = 'arrow white'
        super().__init__(*args, **kwargs)
        separator = ttk.Separator(orient="horizontal")
        separator.place(in_=self, x=0, rely=1.0, height=2, relwidth=1.0)