'''
    Shows all the fields of an employee (General, admin, and permitted information panels)
     for an admin to fill out and add the new employee
    Screen inherits from admin screen class
    Uses GeneralInfo
    Inherits the active Window which already has the Navigation Bar as an active component
    Input fields will be validated for proper inputs
'''


import customtkinter as ctk
from typing import Type
from .Profile import Profile
from ..Components.Panels.AdminInfo import AdminInfo as AI
from ..Components.Panels.PermittedInfo import PermittedInfo as PI


class AddEmployee(Profile):
    def __init__(self, master: Type[ctk.CTk]) -> None:
        super().__init__(master)

        self.img = None
        self.imgL.destroy()

        self.adminInfo = AI(self, editable=True)
        self.adminInfo.grid(row=0)

        self.permittedInfo = PI(self, True, False)
        self.permittedInfo.grid(column=1, row=1)

        self.grid()
