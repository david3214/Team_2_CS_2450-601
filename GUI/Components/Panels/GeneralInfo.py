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


# Alias for typing
char = str

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
            self.entries[9] = tk.OptionMenu(self, self.variables[9][1], 'General', 'Admin')
            self.entries[9].grid(row=0, column=1)

            self.validationMethods = [(self.nameValidate, 0), (self.nameValidate, 1), (self.phoneValidate, 2), (self.emailValidate, 3), (self.IDValidate, 4), (self.dateValidate, 7), (self.dateValidate, 8)]
            self.validationWrappers = [(self.master.register(method[0]), '%P', '%V') for method in self.validationMethods]
            for i, wrapper in enumerate(self.validationWrappers):
                self.entries[self.validationMethods[i][1]].configure(validatecommand=wrapper)


    def vals(self) -> dict:
        remap = {key: self.variables[i + 2][1].get() for i, key in enumerate(['OfficePhone', 'Email', 'EmpID', 'Title', 'Dept', 'StartDate', 'EndDate', 'Permission Level'])}
        remap['Name'] = self.variables[0][1].get() + ' ' + self.variables[1][1].get()

        return remap


    # Not sure if these could be made using a generator, since the wrappers need to be initialized before setting the validation command
    @staticmethod
    def nameValidate(input: char, operation: str) -> bool:
        validString = re.match('^[\w\'\-,.]*[^_!¡?÷?¿\/\\+=@#$%ˆ&*(){}|~<>;:[\]]*$', input) is not None
        if operation == 'key':
            validInput = re.match('^[\w\'\-,.]*[^_!¡?÷?¿\/\\+=@#$%ˆ&*(){}|~<>;:[\]]*$', input) is not None and len(input) <= 100
            if not validInput:
                # error msg
                pass
            return validInput
        elif operation == 'focusout':
            if not validString:
                # error msg
                pass
        return validString


    @staticmethod
    def IDValidate(input: char, operation: str) -> bool:
        validString = re.match('^\d{1, 15}', input) is not None
        if operation == 'key':
            validInput = re.match('\d', input) is not None and len(input) <= 15
            if not validInput:
                # error msg
                pass
            return validInput
        elif operation == 'focusout':
            if not validString:
                # error msg
                pass
        return validString