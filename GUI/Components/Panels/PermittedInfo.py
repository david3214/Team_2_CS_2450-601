'''
    An abstraction of all the employee's permitted level information to be used by multiple screens
'''


import tkinter as tk
from typing import Type
from GUI.Components.Panels.Info import Info
from styles import btn_color, med_bold_underline, text_color


class PermittedInfo(Info):
    def __init__(self, master: Type[tk.Frame], bgColor: str=btn_color, editable: bool=False, locked: bool=True) -> None:
        super().__init__(master, bgColor, editable)

        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.fields  = ['Street Addr.', 'City', 'State', 'Zipcode', 'Personal #', 'Home Email']

        if not locked:
            self.generate({'font': med_bold_underline, 'bg': self.bgColor, 'fg': text_color}, {}, {}, ((lambda i, l: [0, 0, 0, 0, 2, 2, 1, 1, 1, 1, 3, 3][i]), (lambda i, l: [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 0, 1][i]), {'sticky': 'w'}))
        else:
            self.configure(height=100)
