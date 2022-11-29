'''
    An abstraction of all the employee's admin level information to be used by multiple screens
'''


import tkinter as tk
import re
import typing

from GUI.Components.Panels.Info import Info
from styles import btn_color

if typing.TYPE_CHECKING:
    from Screens.Profile import Profile

    from GUI.Window import Window

# Alias for typing
char = str


class AdminInfo(Info):
    def __init__(self, master: 'Profile', bgColor: str=btn_color, editable: bool=False) -> None:
        super().__init__(master, bgColor, editable)
        self.grid_columnconfigure((0, 1), weight=1)#type:ignore

        self.fields  = ['Pay Type', 'Bank Info', 'Route', 'Salary', 'Hourly', 'Commission', 'DOB', 'SSN']
        self.values  = [master.emp.PayMethod, master.emp.BankInfo, master.emp.Route, master.emp.Salary, master.emp.Hourly, master.emp.Commission, master.emp.DOB, master.emp.SSNum] if master.emp else ['' for _ in range(len(self.fields))]
        self.generate({}, {}, {}, ((lambda i, l: i if i < l else i - l), (lambda i, l: 0 if i < l else 1), {}))

        if self.editable:
            # Make Pay type an OptionMenu
            self.entries[0].destroy()
            self.entries=typing.cast('list[tk.Widget]',self.entries)
            self.entries[0] = tk.OptionMenu(self, self.variables[0][1], '1', '2', '3')
            self.entries[0].grid(row=0, column=1)

            self.validationMethods = [(self.bankInfoValidate, 1), (self.routeValidate, 2), (self.salaryValidate, 3), (self.hourlyValidate, 4), (self.commissionValidate, 5), (self.SSNValidate, 7)]
            self.validationWrappers = [(self.master.register(method[0]), '%P', '%V') for method in self.validationMethods]
            for i, wrapper in enumerate(self.validationWrappers):
                self.entries[self.validationMethods[i][1]].configure(validatecommand=wrapper)


    def vals(self) -> dict:
        return {key: self.variables[i][1].get() for i, key in enumerate(['PayMethod', 'Account', 'Route', 'Salary', 'Hourly', 'Commission', 'DOB', 'SSN'])}


    # Not sure if these could be made using a generator, since the wrappers need to be initialized before setting the validation command
    @staticmethod
    def bankInfoValidate(input: char, operation: str) -> bool:
        validString = re.match('^\d{6}-?\d{4}$', input) is not None
        if operation == 'key':
            validInput = re.match('^[\d-]$', input) is not None and len(input) <= 11
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
    def routeValidate(input: char, operation: str) -> bool:
        validString = re.match('^\d{8}-?[\dA-Za-z]$', input) is not None
        if operation == 'key':
            validInput = re.match('^[\dA-Za-z-]&', input) is not None and len(input) <= 10
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
    def salaryValidate(input: char, operation: str) -> bool:
        validString = re.match('^\d{1,9}(\.\d{1,2})?$', input) is not None
        if operation == 'key':
            validInput = re.match('^[\d\.]&', input) is not None and len(input) <= 12
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
    def hourlyValidate(input: char, operation: str) -> bool:
        validString = re.match('^\d{1,6}(\.\d{1,2})?$', input) is not None
        if operation == 'key':
            validInput = re.match('^[\d\.]$', input) is not None and len(input) <= 9
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
    def commissionValidate(input: char, operation: str) -> bool:
        validString = re.match('^0{0,2}(?:[0-9][0-9]?|100)$', input) is not None
        if operation == 'key':
            validInput = re.match('^[\d]$', input) is not None and len(input) <= 3
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
    def SSNValidate(input: char, operation: str) -> bool:
        validString = re.match('^(?!(000|666|9))\d{3}[-\s]?(?!00)\d{2}[-\s]?(?!0000)\d{4}$', input) is not None
        if operation == 'key':
            validInput = re.match('\d\-\s', input) is not None and len(input) <= 11
            if not validInput:
                # error msg
                pass
            return validInput
        elif operation == 'focusout':
            if not validString:
                # error msg
                pass
        return validString