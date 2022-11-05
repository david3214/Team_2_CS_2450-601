'''
    Shows all the fields of an employee (General, admin, and permitted information panels)
     for an admin to fill out and add the new employee
    Screen inherits from admin screen class
    Uses GeneralInfo
    Inherits the active Window which already has the Navigation Bar as an active component
    Input fields will be validated for proper inputs
'''


import tkinter as tk
from typing import Type
from .Profile import Profile
from ..Components.Panels.AdminInfo import AdminInfo as AI
from ..Components.Panels.PermittedInfo import PermittedInfo as PI
from ..Components.Panels.GeneralInfo import GeneralInfo as GI


class AddEmployee(Profile):
    def __init__(self, master: Type[tk.Tk], bgColor: str='grey') -> None:
        super().__init__(master, bgColor=bgColor)

        self.img = None
        self.canvas.destroy()

        self.generalInfo.destroy()
        self.generalInfo = GI(self, editable=True)
        self.generalInfo.grid(column=0, row=0, rowspan=3, sticky='n')

        self.adminInfo = AI(self, editable=True)
        self.adminInfo.grid(column=1, row=0, sticky='nsew', padx=15, pady=15, columnspan=3)

        self.permittedInfo.destroy()
        self.permittedInfo = PI(self, 'blue', True, False)
        self.permittedInfo.grid(column=1, row=1, sticky='nsew', padx=15, columnspan=3)

        self.addEmployeeBtn = tk.Button(self, text='Add Employee', font=('Arial', 12, 'bold'), bg='blue', fg='white')
        self.addEmployeeBtn.grid(column=1, row=2, padx=(0, 15), sticky='e')

        self.grid()
