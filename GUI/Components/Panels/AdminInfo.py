'''
    An abstraction of all the employee's admin level information to be used by multiple screens
'''


import tkinter as tk
from typing import Type
from GUI.Components.Panels.Info import Info
from styles import btn_color


# Alias for typing
char = str


class AdminInfo(Info):
    def __init__(self, master: Type[tk.Frame], bgColor: str=btn_color, editable: bool=False) -> None:
        super().__init__(master, bgColor, editable)

        self.grid_columnconfigure((0, 1), weight=1)

        self.fields  = ['Pay Type', 'Bank Info', 'Route', 'Salary', 'Hourly', 'Commission', 'DOB', 'SSN']
        self.values  = [master.emp.PayMethod, master.emp.BankInfo, master.emp.Route, master.emp.Salary, master.emp.Hourly, master.emp.Commission, master.emp.DOB, master.emp.SSNum] if master.emp else ['' for _ in range(len(self.fields))]
        self.generate({}, {}, {}, ((lambda i, l: i if i < l else i - l), (lambda i, l: 0 if i < l else 1), {}))

        if self.editable:
            # Make Pay type an OptionMenu
            self.entries[0].destroy()
            self.entries[0] = tk.OptionMenu(self, self.variables[0][1], '1', '2', '3')
            self.entries[0].grid(row=0, column=1)

            # Template for testing the validation of Entries
            self.testValidateWrapper = (self.master.register(self.testValidate), '%P')
            self.entries[1].configure(validatecommand=self.testValidateWrapper)
            self.variables[1][1].trace_add('write', self.testUpdate)


    @staticmethod
    def testUpdate(*args: tuple) -> None:
        for arg in args:
            print(arg)


    @staticmethod
    def testValidate(input: char) -> bool:
        print(input)
        return False


    def vals(self) -> dict:
        return {self.fields[i]: self.variables[i][1].get() for i in range(len(self.fields))}
