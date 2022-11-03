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


class AddEmployee(Profile):
    def __init__(self, master: Type[tk.Tk], bgColor: str='grey') -> None:
        super().__init__(master, bgColor=bgColor)

        self.img = None
        self.imgL.destroy()

        self.adminInfo = AI(self, editable=True)
        self.adminInfo.grid(column=1, row=0)

        self.permittedInfo = PI(self, 'blue', True, False)
        self.permittedInfo.grid(column=1, row=1)

        self.grid()
