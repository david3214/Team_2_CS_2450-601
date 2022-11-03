'''
    General information panel used to reduce duplicate code
'''


import customtkinter as ctk
import tkinter as tk
from typing import Type


# Custom Type Aliases
ctkLabelOptions = ctkEntryOptions = dict
ctkGridOptions = tuple


class Info(ctk.CTkFrame):
    def __init__(self, master: Type[ctk.CTkFrame], editable: bool=False) -> None:
        super().__init__(master)

        self.editable = editable
        self.widgets = []
        self.entries = []
        self.valueLabels = []

    def generate(self, labelOptions: ctkLabelOptions, entryOptions: ctkEntryOptions, valueLOptions: ctkLabelOptions, layoutOptions: ctkGridOptions):
        '''All options except layout are optional'''

        self.labels = [ctk.CTkLabel(master=self, text=field, **labelOptions) for field in self.fields] if labelOptions else [ctk.CTkLabel(master=self, text=field + ': ', text_font=('Arial', 12, 'bold')) for field in self.fields]

        if self.editable:
            self.variables = [(field, tk.StringVar()) for field in self.fields]
            self.entries = [ctk.CTkEntry(master=self, **entryOptions) for _ in self.variables] if entryOptions else [ctk.CTkEntry(master=self, textvariable=variable[1], validate='key') for variable in self.variables]
        else:
            self.valueLabels = [ctk.CTkLabel(master=self, **valueLOptions) for _ in self.labels] if valueLOptions else [ctk.CTkLabel(master=self, text='temp', text_font=('Arial', 12)) for _ in self.labels]

        self.widgets = self.widgets + self.labels + self.entries + self.valueLabels
        [widget.grid(row=layoutOptions[0](i, len(self.fields)), column=layoutOptions[1](i, len(self.fields)), **layoutOptions[2]) for i, widget in enumerate(self.widgets)] # TODO: **layoutOptions[2] not applying