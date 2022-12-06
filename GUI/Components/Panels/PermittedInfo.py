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

# Alias for typing
char = str


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
            self.entries[2] = tk.ttk.Combobox(self, textvariable=self.variables[2][1], state='readonly', values=['AL', 'AK', 'AZ', 'AR', 'AS', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'TT', 'UT', 'VT', 'VA', 'VI', 'WA', 'WV', 'WI', 'WY'])
            self.entries[2].grid(row=1, column=2)

            self.validationMethods = [(self.streetAddrValidate, 0), (self.cityValidate, 1), (self.zipValidate, 3), (self.phoneValidate, 4), (self.emailValidate, 5)]
            self.validationWrappers = [(self.master.register(method[0]), '%P', '%V') for method in self.validationMethods]
            for i, wrapper in enumerate(self.validationWrappers):
                self.entries[self.validationMethods[i][1]].configure(validatecommand=wrapper)

    def vals(self) -> dict:
        remap = {key: self.variables[i][1].get() for i, key in enumerate(['Address', 'City', 'State', 'Zip', 'HomePhone', 'HomeEmail'])}

        return remap


    # Not sure if these could be made using a generator, since the wrappers need to be initialized before setting the validation command
    @staticmethod
    def streetAddrValidate(input: char) -> bool:
        return re.match('[*,()"\':;@&-]', input) is None and len(input) <= 100


    @staticmethod
    def cityValidate(input: char, operation: str) -> bool:
        validString = re.match('^([a-zA-Z\u0080-\u024F]+(?:. |-| |\'))*[a-zA-Z\u0080-\u024F]*$', input) is not None
        if operation == 'key':
            validInput = re.match('.', input) is not None and len(input) <= 100
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
    def zipValidate(input: char, operation: str) -> bool:
        validString = re.match('^\d{5}([-\s]?\d{4})?$', input) is not None
        if operation == 'key':
            validInput = re.match('^[\d\s-]$', input) is not None and len(input) <= 10
            if not validInput:
                # error msg
                pass
            return validInput
        elif operation == 'focusout':
            if not validString:
                # error msg
                pass
        return validString