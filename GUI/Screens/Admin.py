'''
    Shows information about a given employee at the admin permission level (General, admin, and permitted information panels)
    Screen inherits from AddEmployee screen class
    Inherits the active Window which already has the Navigation Bar as an active component
    Uses GeneralInfo, PermittedInfo, AdminInfo
    Information can be edited
    Edited fields must be re-validated
    Employee can be archived
    Pay report can be generated
'''


import tkinter as tk
from typing import Type
from .AddEmployee import AddEmployee as AE
from styles import background_color,  med_bold, btn_color, text_color


class Admin(AE):
    def __init__(self, master: Type[tk.Tk], bgColor: str=background_color) -> None:
        super().__init__(master, bgColor=bgColor)

        self.addEmployeeBtn.destroy()

        self.options = {'font': med_bold, 'bg': btn_color, 'fg': text_color}

        self.genPayReportBtn = tk.Button(self, text='Generate Pay Report', **self.options)
        self.genPayReportBtn.grid(column=1, row=2, padx=(0, 15), sticky='e')

        self.archiveBtn = tk.Button(self, text='Archive', **self.options)
        self.archiveBtn.grid(column=2, row=2, padx=(0, 15))

        self.updateBtn = tk.Button(self, text='Update', **self.options)
        self.updateBtn.grid(column=3, row=2, padx=(0, 15))

        self.grid()
