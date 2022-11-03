'''
    An abstraction of all the employee's admin level information to be used by multiple screens
'''


import customtkinter as ctk
from typing import Type
from GUI.Components.Panels.Info import Info


# Alias for typing
char = str


class AdminInfo(Info):
    def __init__(self, master: Type[ctk.CTkFrame], editable: bool=False) -> None:
        super().__init__(master, editable)

        self.fields = ['Pay Type', 'Bank Info', 'Route', 'Salary', 'Hourly', 'Commission', 'DOB', 'SSN']
        self.generate({}, {}, {}, ((lambda i, l: i if i < l else i - l), (lambda i, l: 0 if i < l else 1), {}))

        # Make Pay type a OptionMenu
        self.entries[0].destroy()
        self.entries[0] = ctk.CTkOptionMenu(master=self, variable=self.variables[0][1], values=['1', '2', '3'])
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
    def testValidate(input: char):
        print(input)
        return False
