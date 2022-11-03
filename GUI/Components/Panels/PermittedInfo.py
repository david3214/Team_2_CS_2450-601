'''
    An abstraction of all the employee's permitted level information to be used by multiple screens
'''


import tkinter as tk
from typing import Type
from GUI.Components.Panels.Info import Info


class PermittedInfo(Info):
    def __init__(self, master: Type[tk.Frame], bgColor: str='grey', editable: bool=False, locked: bool=True) -> None:
        super().__init__(master, bgColor, editable)

        self.fields  = ['Street Address', 'City', 'State', 'Zipcode', 'Personal Phone', 'Home Email']

        if not locked:
            self.generate({'font': ('Arial', 12, 'bold', 'underline'), 'bg': self.bgColor, 'fg':'white'}, {}, {}, ((lambda i, l: 0 if i < l else 1), (lambda i, l: i if  i < l else i - l), {}))
