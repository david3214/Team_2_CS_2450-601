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
from Config.PayReport import generate_pay_report
from Employee.EmployeeContainer import EmployeeContainer
from .AddEmployee import AddEmployee as AE
from .Archived import Archived
from Config.config import DB
from Config.fetch_resource import fetch_resource
from Config.styles import background_color,  med_bold, btn_color, text_color


class Admin(AE):
    def __init__(self, master: Type[tk.Tk], emp: Type[EmployeeContainer], bgColor: str=background_color) -> None:
        super().__init__(master, emp, bgColor=bgColor)

        self.addEmployeeBtn.destroy()

        self.options = {'font': med_bold, 'bg': btn_color, 'fg': text_color}

        self.genPayReportBtn = tk.Button(self, text='Generate Pay Report', **self.options, command=lambda: generate_pay_report(self.emp))
        self.genPayReportBtn.grid(column=1, row=2, padx=(0, 15), sticky='e')

        self.archiveBtn = tk.Button(self, text='Archive', **self.options, command=self.archive)
        self.archiveBtn.grid(column=2, row=2, padx=(0, 15))

        self.updateBtn = tk.Button(self, text='Update', **self.options, command=self.update)
        self.updateBtn.grid(column=3, row=2, padx=(0, 15))

        self.grid()


    def archive(self):
        self.emp.Active = False
        DB.exportDB(fetch_resource('./Resources/database.csv'), True)
        self.master.switchFrame(Archived, self.emp)


    def update(self) -> None:
        # Can certainly be improved
        self.emp.Address.address = self.permittedInfo.variables[0][1].get()
        self.emp.Address.city = self.permittedInfo.variables[1][1].get()
        self.emp.Address.state = self.permittedInfo.variables[2][1].get()
        self.emp.Address.zip = self.permittedInfo.variables[3][1].get()
        self.emp.HomePhone = self.permittedInfo.variables[4][1].get()
        self.emp.HomeEmail = self.permittedInfo.variables[5][1].get()
   
        self.emp.Name = self.generalInfo.variables[0][1].get() + ' ' + self.generalInfo.variables[1][1].get()
        self.emp.OfficePhone = self.generalInfo.variables[2][1].get()
        self.emp.OfficeEmail = self.generalInfo.variables[3][1].get()
        self.emp.EmpID = self.generalInfo.variables[4][1].get()
        self.emp.Title = self.generalInfo.variables[5][1].get()
        self.emp.Dept = self.generalInfo.variables[6][1].get()
        self.emp.StartDate = self.generalInfo.variables[7][1].get()
        self.emp.EndDate = self.generalInfo.variables[8][1].get()
        self.emp.PermissionLevel = self.generalInfo.variables[9][1].get()

        self.emp.PayMethod = self.adminInfo.variables[0][1].get()
        self.emp.BankInfo = self.adminInfo.variables[1][1].get()
        self.emp.Route = self.adminInfo.variables[2][1].get()
        self.emp.Salary = self.adminInfo.variables[3][1].get()
        self.emp.Hourly = self.adminInfo.variables[4][1].get()
        self.emp.Commission = self.adminInfo.variables[5][1].get()
        self.emp.DOB = self.adminInfo.variables[6][1].get()
        self.emp.SSNum = self.adminInfo.variables[7][1].get()

        DB.exportDB(fetch_resource('./Resources/database.csv'), True)
