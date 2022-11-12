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
        self.values = [master.emp.getFName(), master.emp.getLName(), master.emp.OfficePhone, master.emp.OfficeEmail, master.emp.EmpID, master.emp.Title, master.emp.Dept, master.emp.StartDate, master.emp.EndDate, master.emp.PermissionLevel] if master.emp else ['' for _ in range(len(self.fields))]

        self.img  = tk.PhotoImage(file='images/userProfile.png')
        self.imgL = tk.Label(self, image=self.img)
        self.generate({}, {}, {}, ((lambda i, l: i if i <= l else i - l), (lambda i, l: 0 if i <= l else 1), {'sticky': 'w'}))

        self.imgL.grid(columnspan=2)


    def vals(self) -> dict:
        remap = {key: self.variables[i + 2][1].get() for i, key in enumerate(['OfficePhone', 'Email', 'EmpID', 'Title', 'Dept', 'StartDate', 'EndDate', 'Permission Level'])}
        remap['Name'] = self.variables[0][1].get() + ' ' + self.variables[1][1].get()

        return remap
