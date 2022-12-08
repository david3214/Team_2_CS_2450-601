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
        self.values = [master.emp.getFName(), master.emp.getLName(), master.emp.OfficePhone, master.emp.OfficeEmail, master.emp.EmpID, master.emp.Title, master.emp.Dept, master.emp.StartDate.date(), master.emp.EndDate.date(), master.emp.PermissionLevel] if master.emp else ['' for _ in range(len(self.fields))]
        self.validationIndexes = [i for i in range(5)]

        self.img  = tk.PhotoImage(file=fetch_resource('./Resources/images/userProfile.png'))
        self.imgL = tk.Label(self, image=self.img)
        self.generate({}, {}, {}, ((lambda i, l: i if i <= l else i - l), (lambda i, l: 0 if i <= l else 1), {'sticky': 'w'}))

        self.imgL.grid(columnspan=2)

        if self.editable:
            self.entries[9].destroy()
            self.entries[9] = tk.OptionMenu(self, self.variables[9][1], '0', '1')
            self.entries[9].grid(row=10, column=1)

            self.validationMethods = [(self.validateGenerator(*v.genValidationArgs[i], self.fields[idx]), idx) for i, idx in enumerate(self.validationIndexes)]
            self.validationWrappers = [(self.master.register(method[0]), '%d', '%P', '%S', '%V') for method in self.validationMethods]
            for i, wrapper in enumerate(self.validationWrappers):
                self.entries[self.validationMethods[i][1]].configure(validatecommand=wrapper, validate='all')

            self.entries[7].configure(validatecommand=self.dateWrapper, validate='focusout')
            self.entries[8].configure(validatecommand=self.dateWrapper, validate='focusout')


    def vals(self) -> dict[str,str]:
        remap = {key: self.variables[i + 2][1].get() for i, key in enumerate(['OfficePhone', 'OfficeEmail', 'EmpID', 'Title', 'Dept', 'StartDate', 'EndDate', 'PermissionLevel'])}
        remap['Name'] = self.variables[0][1].get() + ' ' + self.variables[1][1].get()

        return remap