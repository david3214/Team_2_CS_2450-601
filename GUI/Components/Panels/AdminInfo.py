'''
    An abstraction of all the employee's admin level information to be used by multiple screens
'''


import tkinter as tk
import re
import typing

from GUI.Components.Panels.Info import Info
from Config.styles import btn_color

if typing.TYPE_CHECKING:
    from Screens.Profile import Profile

    from GUI.Window import Window
import Config.regexValidators as v


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

            self.validationMethods = [(self.validateGenerator(v.bank, v.bankChars, 11, 'bankinfo', self.fields[1]), 1), (self.validateGenerator(v.route, v.routeChars, 10, 'route', self.fields[2]), 2), (self.validateGenerator(v.float, v.floatChars, 12, 'salary', self.fields[3]), 3), (self.validateGenerator(v.float, v.floatChars, 12, 'hourly', self.fields[4]), 4), (self.validateGenerator(v.commission, '\d', 3, 'commission', self.fields[5]), 5), (self.validateGenerator(v.ssn, v.dsd, 11, 'ssn', self.fields[7]), 7)]
            self.validationWrappers = [(self.master.register(method[0]), '%P', '%V') for method in self.validationMethods]
            for i, wrapper in enumerate(self.validationWrappers):
                self.entries[self.validationMethods[i][1]].configure(validatecommand=wrapper, validate='all')


    def vals(self) -> dict:
        return {key: self.variables[i][1].get() for i, key in enumerate(['PayMethod', 'Account', 'Route', 'Salary', 'Hourly', 'Commission', 'DOB', 'SSN'])}