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
from PayReport import generate_pay_report
from EmployeeContainer import EmployeeContainer
from .AddEmployee import AddEmployee as AE
from styles import background_color,  med_bold, btn_color, text_color


class Admin(AE):
    def __init__(self, master: Type[tk.Tk], emp: Type[EmployeeContainer], bgColor: str=background_color) -> None:
        super().__init__(master, emp, bgColor=bgColor)

        self.addEmployeeBtn.destroy()

        self.options = {'font': med_bold, 'bg': btn_color, 'fg': text_color}

        self.genPayReportBtn = tk.Button(self, text='Generate Pay Report', **self.options, command=lambda: generate_pay_report(master.emp))
        self.genPayReportBtn.grid(column=1, row=2, padx=(0, 15), sticky='e')

        self.archiveBtn = tk.Button(self, text='Archive', **self.options, command=lambda: master.emp.Active(False))
        self.archiveBtn.grid(column=2, row=2, padx=(0, 15))

        self.updateBtn = tk.Button(self, text='Update', **self.options, command=self.update)
        self.updateBtn.grid(column=3, row=2, padx=(0, 15))

        self.grid()


    def update(self) -> None:
        for i, setter in enumerate(self.adminInfo.values):
            setter(self.adminInfo.variables[i][1].get())

        for i, setter in enumerate(self.permittedInfo.values):
            setter(self.adminInfo.variables[i][1].get())
            
        for i, setter in enumerate(self.generalInfo.values):
            setter(self.adminInfo.variables[i][1].get())
