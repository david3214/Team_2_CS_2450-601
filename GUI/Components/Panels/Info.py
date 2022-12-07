'''
    General information panel used to reduce duplicate code
'''


import tkinter as tk
import re
from Config.styles import background_color, med_bold, text_color, med_text
from abc import ABC,abstractmethod,abstractproperty
import typing

# Custom Type Aliases
tkLabelOptions = tkEntryOptions = dict
tkGridOptions = tuple


class Info(tk.Frame,ABC):
    def __init__(self, master: tk.Frame, bgColor: str=background_color, editable: bool=False) -> None:
        super().__init__(master, bg=bgColor)

        self.editable = editable
        self.bgColor = bgColor
        self.ids = {}

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


    def validateGenerator(self, strReg: str, vChars: str, mxLen: int, idName: str, errMsg: str) -> typing.Callable:
        def template(val: str, op: str) -> bool:
            vStr = re.match(strReg, val) is not None
            if op == 'key':
                if val == '':
                    return True
                vChange = re.match(vChars, input[-1]) is not None and len(val) <= mxLen
                if not vChange:
                    self.master.invalidInput()
                return vChange
            elif op == 'focusout':
                if not vStr:
                    if idName in self.ids:
                        self.master.alert(self.ids[idName])
                    else:
                        self.ids[idName] = self.master.addError(errMsg + 'is invalid')
                elif idName in self.ids:
                    self.master.clearError(self.ids[idName])
                    del self.ids[idName]
            return vStr
        return template