'''
    An abstraction of all the employee's permitted level information to be used by multiple screens
'''


import tkinter as tk
import re
from GUI.Components.Panels.Info import Info
from Config.styles import btn_color, med_bold_underline, text_color

import typing
from .Info import Info
if typing.TYPE_CHECKING:
    from GUI.Screens.Profile import Profile
import Config.regexValidators as v


class PermittedInfo(Info):
    def __init__(self, master: 'Profile', bgColor: str=btn_color, editable: bool=False, locked: bool=True) -> None:
        super().__init__(master, bgColor, editable)

        self.grid_columnconfigure((0, 1, 2, 3), weight=1)  # type: ignore

        self.fields = ['Street Addr.', 'City', 'State', 'Zipcode', 'Personal #', 'Home Email']
        self.values = [master.emp.Address, master.emp.City, master.emp.State, master.emp.Zip, master.emp.HomePhone, master.emp.HomeEmail] if master.emp else ['' for _ in range(len(self.fields))]

        if not locked:
            self.generate({'font': med_bold_underline, 'bg': self.bgColor, 'fg': text_color}, {}, {}, ((lambda i, l: [0, 0, 0, 0, 2, 2, 1, 1, 1, 1, 3, 3][i]), (lambda i, l: [0, 1, 2, 3, 0, 1, 0, 1, 2, 3, 0, 1][i]), {'sticky': 'w'}))
        else:
            self.configure(height=100)

        if self.editable:
            self.entries[2].destroy()
            self.entries[2] = tk.ttk.Combobox(self, textvariable=self.variables[2][1], state='readonly', values=v.states)
            self.entries[2].grid(row=1, column=2)

            self.validationMethods = [(self.validateGenerator(v.city, '.', 100, 'city', self.fields[1]), 1), (self.validateGenerator(v.zip, v.dsd, 10, 'zip', self.fields[3]), 3), (self.validateGenerator(v.phone, v.phoneChars, 18, 'hphone', self.fields[4]), 4), (self.validateGenerator(v.email, '.', 100, 'hemail', self.fields[5]), 5)]
            self.validationWrappers = [(self.master.register(method[0]), '%P', '%V') for method in self.validationMethods]
            for i, wrapper in enumerate(self.validationWrappers):
                self.entries[self.validationMethods[i][1]].configure(validatecommand=wrapper, validate='all')

    def vals(self) -> dict:
        remap = {key: self.variables[i][1].get() for i, key in enumerate(['Address', 'City', 'State', 'Zip', 'HomePhone', 'HomeEmail'])}

        return remap