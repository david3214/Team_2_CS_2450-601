'''
    Shows all the fields of an employee (General, admin, and permitted information panels)
     for an admin to fill out and add the new employee
    Screen inherits from profile screen class
    Uses GeneralInfo
    Inherits the active Window which already has the Navigation Bar as an active component
'''


import tkinter as tk
from typing import Type
from .Profile import Profile
from ..Components.Panels.AdminInfo import AdminInfo as AI
from ..Components.Panels.PermittedInfo import PermittedInfo as PI
from ..Components.Panels.GeneralInfo import GeneralInfo as GI
from EmployeeContainer import EmployeeContainer
from config import DB, fetch_resource
from styles import background_color, btn_color, text_color, med_bold


class AddEmployee(Profile):
    def __init__(self, master: Type[tk.Tk], emp: Type[EmployeeContainer]=None, bgColor: str=background_color) -> None:
        super().__init__(master, emp, bgColor=bgColor)

        self.img = None
        self.canvas.destroy()

        self.generalInfo.destroy()
        self.generalInfo = GI(self, editable=True)
        self.generalInfo.grid(column=0, row=0, rowspan=3, sticky='n')

        self.adminInfo = AI(self, editable=True)
        self.adminInfo.grid(column=1, row=0, sticky='nsew', padx=15, pady=15, columnspan=3)

        self.permittedInfo.destroy()
        self.permittedInfo = PI(self, btn_color, True, False)
        self.permittedInfo.grid(column=1, row=1, sticky='nsew', padx=15, columnspan=3)

        self.addEmployeeBtn = tk.Button(self, text='Add Employee', font=med_bold, bg=btn_color, fg=text_color, command=self.addEmp)
        self.addEmployeeBtn.grid(column=1, row=2, padx=(0, 15), sticky='e')

        self.grid()


    def addEmp(self) -> None:
        DB.addEmployee(**(self.generalInfo.vals() | self.adminInfo.vals() | self.permittedInfo.vals()))
        DB.exportDB(fetch_resource('database/database.csv'), True)
