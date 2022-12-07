'''
    An abstraction of all the employee's general level information to be used by multiple screens
'''


import tkinter as tk
import re
from GUI.Components.Panels.Info import Info
from Config.styles import background_color
from Config.fetch_resource import fetch_resource
import typing
if typing.TYPE_CHECKING:
    from GUI.Screens.Profile import Profile
import Config.regexValidators as v


class GeneralInfo(Info):
    def __init__(self, master: 'Profile', bgColor: str=background_color, editable: bool=False) -> None:
        super().__init__(master, bgColor, editable)

        self.fields = ['First Name', 'Last Name', 'Office #', 'Office Email', 'Employee ID', 'Title', 'Department', 'Start Date', 'End Date', 'Perm. Level']
        self.values = [master.emp.getFName(), master.emp.getLName(), master.emp.OfficePhone, master.emp.OfficeEmail, master.emp.EmpID, master.emp.Title, master.emp.Dept, master.emp.StartDate, master.emp.EndDate, master.emp.PermissionLevel] if master.emp else ['' for _ in range(len(self.fields))]

        self.img  = tk.PhotoImage(file=fetch_resource('./Resources/images/userProfile.png'))
        self.imgL = tk.Label(self, image=self.img)
        self.generate({}, {}, {}, ((lambda i, l: i if i <= l else i - l), (lambda i, l: 0 if i <= l else 1), {'sticky': 'w'}))

        self.imgL.grid(columnspan=2)

        if self.editable:
            self.entries[9].destroy()
            self.entries[9] = tk.OptionMenu(self, self.variables[9][1], '0', '1')
            self.entries[9].grid(row=10, column=1)

            self.validationMethods = [(self.validateGenerator(v.name, '.', 100, 'fname', self.fields[0]), 0), (self.validateGenerator(v.name, '.', 100, 'lname', self.fields[1]), 1), (self.validateGenerator(v.phone, v.phoneChars, 18, 'ophone', self.fields[2]), 2), (self.validateGenerator(v.email, '.', 100, 'oemail', self.fields[3]), 3), (self.validateGenerator(v.empID, '\d', 15, 'id', self.fields[4]), 4), (self.validateGenerator(v.date, v.dateChars, 10, 'sDate', self.fields[7]), 7), (self.validateGenerator(v.date, v.dateChars, 10, 'eDate', self.fields[8]), 8)]
            self.validationWrappers = [(self.master.register(method[0]), '%P', '%V') for method in self.validationMethods]
            for i, wrapper in enumerate(self.validationWrappers):
                self.entries[self.validationMethods[i][1]].configure(validatecommand=wrapper, validate='all')


    def vals(self) -> dict:
        remap = {key: self.variables[i + 2][1].get() for i, key in enumerate(['OfficePhone', 'Email', 'EmpID', 'Title', 'Dept', 'StartDate', 'EndDate', 'Permission Level'])}
        remap['Name'] = self.variables[0][1].get() + ' ' + self.variables[1][1].get()

        return remap