'''
    An abstraction of all the employee's general level information to be used by multiple screens
'''


import tkinter as tk
from typing import Type
from GUI.Components.Panels.Info import Info
from styles import background_color


class GeneralInfo(Info):
    def __init__(self, master: Type[tk.Frame], bgColor: str=background_color, editable: bool=False) -> None:
        super().__init__(master, bgColor, editable)

        self.fields = ['First Name', 'Last Name', 'Office #', 'Office Email', 'Employee ID', 'Title', 'Department', 'Start Date', 'End Date', 'Perm. Level']

        self.img  = tk.PhotoImage(file='images/userProfile.png')
        self.imgL = tk.Label(self, image=self.img)
        self.generate({}, {}, {}, ((lambda i, l: i if i <= l else i - l), (lambda i, l: 0 if i <= l else 1), {'sticky': 'w'}))

        self.imgL.grid(columnspan=2)
