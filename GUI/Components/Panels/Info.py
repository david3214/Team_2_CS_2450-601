'''
    General information panel used to reduce duplicate code
'''


import tkinter as tk
import re
from typing import Type
from styles import background_color, med_bold, text_color, med_text
from abc import ABC,abstractmethod,abstractproperty

# Custom Type Aliases
tkLabelOptions = tkEntryOptions = dict
tkGridOptions = tuple
char = str


class Info(tk.Frame,ABC):
    def __init__(self, master: tk.Frame, bgColor: str=background_color, editable: bool=False) -> None:
        super().__init__(master, bg=bgColor)

        self.editable = editable
        self.bgColor = bgColor

    fields:list[str]
    values:list

    def generate(self, labelOptions: tkLabelOptions, entryOptions: tkEntryOptions, valueLOptions: tkLabelOptions, layoutOptions: tkGridOptions):
        '''All options except layout are optional'''

        self.labels = [tk.Label(self, text=field, **labelOptions) for field in self.fields] if labelOptions else [tk.Label(self, text=field + ': ', font=med_bold, bg=self.bgColor, fg=text_color) for field in self.fields]

        if self.editable:
            self.variables = [(field, tk.StringVar()) for field in self.fields]
            self.entries = [tk.Entry(self, **entryOptions) for variable in self.variables] if entryOptions else [tk.Entry(self, textvariable=variable[1], validate='key') for variable in self.variables]
            [entry.insert(0, self.values[i]) for i, entry in enumerate(self.entries)]
        else:
            self.valueLabels:list[tk.Widget] = [tk.Label(self, **valueLOptions) for _ in self.values] if valueLOptions else [tk.Label(self, text=value, font=med_text, bg=self.bgColor, fg=text_color) for value in self.values]

        [self.children[child].grid(row=layoutOptions[0](i, len(self.fields)), column=layoutOptions[1](i, len(self.fields)), **layoutOptions[2]) for i, child in enumerate(self.children)]


    # Not sure if these could be made using a generator, since the wrappers need to be initialized before setting the validation command
    # These validation functions are used by multiple child classes
    @staticmethod
    def phoneValidate(input: char, operation: str) -> bool:
        validString = re.match('^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$', input) is not None
        if operation == 'key':
            validInput = re.match('[\d\-\(\)\.\+\s', input) is not None and len(input) <= 18
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
    def emailValidate(input: char, operation: str) -> bool:
        validString = re.match('(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])', input) is not None
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
    def dateValidate(input: char, operation: str) -> bool:
        validString = re.match('^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$', input) is not None
        if operation == 'key':
            validInput = re.match('\d/\-\.', input) is not None and len(input) <= 10
            if not validInput:
                # error msg
                pass
            return validInput
        elif operation == 'focusout':
            if not validString:
                # error msg
                pass
        return validString