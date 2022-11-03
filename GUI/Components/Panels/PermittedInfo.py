'''
    An abstraction of all the employee's permitted level information to be used by multiple screens
'''


import customtkinter as ctk
from typing import Type
from GUI.Components.Panels.Info import Info


class PermittedInfo(Info):
    def __init__(self, master: Type[ctk.CTkFrame], editable: bool=False, locked: bool=True) -> None:
        super().__init__(master, editable)

        self.fields = ['Street Address', 'City', 'State', 'Zipcode', 'Personal Phone', 'Home Email']

        if not locked:
            self.generate({'text_font': ('Arial', 12, 'bold', 'underline')}, {}, {}, ((lambda i, l: 0 if i < l else 1), (lambda i, l: i if  i < l else i - l), {}))
        else:
            self.configure(width=500, height=100)
