'''
    General information panel used to reduce duplicate code
'''


import tkinter as tk
from typing import Type
from styles import background_color, med_bold, text_color, med_text


# Custom Type Aliases
tkLabelOptions = tkEntryOptions = dict
tkGridOptions = tuple


class Info(tk.Frame):
    def __init__(self, master: Type[tk.Frame], bgColor: str=background_color, editable: bool=False) -> None:
        super().__init__(master, bg=bgColor)

        self.editable = editable
        self.bgColor = bgColor

    def generate(self, labelOptions: tkLabelOptions, entryOptions: tkEntryOptions, valueLOptions: tkLabelOptions, layoutOptions: tkGridOptions):
        '''All options except layout are optional'''

        self.labels = [tk.Label(self, text=field, **labelOptions) for field in self.fields] if labelOptions else [tk.Label(self, text=field + ': ', font=med_bold, bg=self.bgColor, fg=text_color) for field in self.fields]

        if self.editable:
            self.variables = [(field, tk.StringVar()) for field in self.fields]
            self.entries = [tk.Entry(self, **entryOptions) for variable in self.variables] if entryOptions else [tk.Entry(self, textvariable=variable[1], validate='key') for variable in self.variables]
            [entry.insert(0, self.values[i]) for i, entry in enumerate(self.entries)]
        else:
            self.valueLabels = [tk.Label(self, **valueLOptions) for _ in self.values] if valueLOptions else [tk.Label(self, text=value, font=med_text, bg=self.bgColor, fg=text_color) for value in self.values]

        [self.children[child].grid(row=layoutOptions[0](i, len(self.fields)), column=layoutOptions[1](i, len(self.fields)), **layoutOptions[2]) for i, child in enumerate(self.children)]
