'''
    This screen displays after login
    Shows all information about current user (General, admin, and permitted information panels)
    Screen inherits from profile screen class
    Navigation bar will be initialized and added to the active window
    Uses GeneralInfo, PermittedInfo, AdminInfo, Navigation
    General and permitted information can be edited
    Any updated information will be validated
'''


import tkinter as tk
from typing import Type
from .Profile import Profile
from ..Components.Panels.AdminInfo import AdminInfo as AI
from ..Components.Panels.PermittedInfo import PermittedInfo as PI
from config import userSession
from styles import background_color, text_color, btn_color, med_bold


class User(Profile):
    def __init__(self, master: Type[tk.Tk], bgColor: str=background_color) -> None:
        super().__init__(master, userSession, bgColor)

        self.img  = None
        self.canvas.destroy()

        self.options = {'font': med_bold, 'bg': btn_color, 'fg': text_color}
        self.generalInfo.variables = []

        for i in range(4):
            self.generalInfo.valueLabels[i].destroy()
            self.generalInfo.variables.append((self.generalInfo.fields[i], tk.StringVar()))
            self.generalInfo.valueLabels[i] = tk.Entry(self.generalInfo, textvariable=self.generalInfo.variables[i][1], validate='key')
            self.generalInfo.valueLabels[i].insert(0, self.generalInfo.values[i])
            self.generalInfo.valueLabels[i].grid(row=i + 1, column=1, sticky='w')

        self.adminInfo = AI(self)
        self.adminInfo.grid(column=1, row=0, sticky='nsew', padx=15, pady=15, columnspan=3)

        self.permittedInfo.destroy()
        self.permittedInfo = PI(self, btn_color, True, False)
        self.permittedInfo.grid(column=1, row=1, sticky='nsew', padx=15, columnspan=3)

        self.updateBtn = tk.Button(self, text='Update', **self.options, command=self.update)
        self.updateBtn.grid(column=1, row=2, padx=(0, 15))

        self.grid()

    def update(self) -> None:
        for i, setter in enumerate(self.permittedInfo.values):
            setter(self.adminInfo.variables[i][1].get())
            
        for i, setter in enumerate(self.generalInfo.values):
            setter(self.adminInfo.variables[i][1].get())
