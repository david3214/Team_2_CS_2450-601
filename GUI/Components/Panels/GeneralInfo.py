'''
    An abstraction of all the employee's general level information to be used by multiple screens
'''


import tkinter as tk
from typing import Type
from GUI.Components.Panels.Info import Info


class GeneralInfo(Info):
    def __init__(self, master: Type[tk.Frame], bgColor: str='grey', editable: bool=False) -> None:
        super().__init__(master, bgColor, editable)

        self.fields  = ['First Name', 'Last Name', 'Office Phone', 'Office Email', 'Employee ID', 'Title', 'Department', 'Start Date', 'End Date', 'Permission Level']

        self.img     = tk.PhotoImage(file='Images/profile.png')
        self.imgL    = tk.Label(self, image=self.img)
        self.generate({}, {}, {}, ((lambda i, l: i if i <= l else i - l), (lambda i, l: 0 if i <= l else 1), {'sticky': 'w'}))
