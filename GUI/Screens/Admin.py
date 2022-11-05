'''
    Shows information about a given employee at the admin permission level (General, admin, and permitted information panels)
    Screen inherits from profile screen class
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


class Admin(AE):
    def __init__(self, master: Type[tk.Tk], bgColor: str='grey') -> None:
        super().__init__(master, bgColor=bgColor)

        self.addEmployeeBtn.destroy()

        self.options = {'font': ('Arial', 12, 'bold'), 'bg': 'blue', 'fg': 'white'}

        self.genPayReportBtn = tk.Button(self, text='Generate Pay Report', **self.options)
        self.genPayReportBtn.grid(column=1, row=2, padx=(0, 15), sticky='e')

        self.archiveBtn = tk.Button(self, text='Archive', **self.options)
        self.archiveBtn.grid(column=2, row=2, padx=(0, 15))

        self.updateBtn = tk.Button(self, text='Update', **self.options)
        self.updateBtn.grid(column=3, row=2, padx=(0, 15))

        self.grid()
