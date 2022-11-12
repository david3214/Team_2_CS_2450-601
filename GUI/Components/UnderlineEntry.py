'''
    Used to make entry fields.
'''

import tkinter as tk
from tkinter import ttk

class UnderlineEntry(tk.Entry):
    def __init__(self, *args, name='', **kwargs):
        kwargs["borderwidth"] = 0
        kwargs["cursor"] = 'arrow white'
        super().__init__(*args, **kwargs)
        separator = ttk.Separator(orient="horizontal")
        separator.place(in_=self, x=0, rely=1.0, height=2, relwidth=1.0)
        self.insert(-1, name)
        
        self.default_text = True
        self.bind('<Button-1>', self.delete_text)

    def delete_text(self, event):
        if self.default_text:
            self.delete(0, tk.END)
            self.default_text = False
