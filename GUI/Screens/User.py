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
import typing
from .Profile import Profile
from ..Components.Panels.AdminInfo import AdminInfo as AI
from ..Components.Panels.PermittedInfo import PermittedInfo as PI
from ..Components.Image_Lbl import Image_Lbl
from Config.config import userSession, DB
from Config.fetch_resource import fetch_resource
from Config.styles import background_color, text_color, btn_color, med_bold


class User(Profile):
    def __init__(self, master: tk.Tk, bgColor: str=background_color) -> None:
        super().__init__(master, userSession, bgColor)

        self.img  = None
        self.canvas.destroy()

        self.options = {'font': med_bold, 'bg': btn_color, 'fg': text_color}
        self.generalInfo.variables = []

        for i in range(4):
            self.generalInfo.valueLabels[i].destroy()
            self.generalInfo.variables.append((self.generalInfo.fields[i], tk.StringVar()))
            self.generalInfo.valueLabels[i] = tk.Entry(self.generalInfo, textvariable=self.generalInfo.variables[i][1], validate='key')
            typing.cast('tk.Entry',self.generalInfo.valueLabels[i]).insert(0, self.generalInfo.values[i])
            self.generalInfo.valueLabels[i].grid(row=i + 1, column=1, sticky='w')

        self.adminInfo = AI(self)
        self.adminInfo.grid(column=1, row=1, sticky='nsew', padx=15, pady=15, columnspan=3)

        self.permittedInfo.destroy()
        self.permittedInfo = PI(self, btn_color, True, False)
        self.permittedInfo.grid(column=1, row=2, sticky='nsew', padx=15, columnspan=3)

        self.permittedInfo.lockToggle = Image_Lbl(self.permittedInfo, btn_color, 40, 40, None, fetch_resource('./Resources/images/locked.png'), fetch_resource('./Resources/images/unlocked.png'))
        if not self.emp.PermittedLockOn:
            self.permittedInfo.lockToggle.change_state()
        self.permittedInfo.lockToggle.grid(column=3, row=2, rowspan=2, sticky='e', padx=(0, 10), pady=(10, 0))

        self.updateBtn = tk.Button(self, text='Update', **self.options, command=self.update)
        self.updateBtn.grid(column=1, row=3, padx=(0, 15), sticky='e')

        self.grid()

    def update(self) -> None:
        if self.emp == None:
            return

        vals = self.permittedInfo.vals()
        for val in vals:
            setattr(self.emp, val, vals[val])

        self.emp.Name = self.generalInfo.variables[0][1].get() + ' ' + self.generalInfo.variables[1][1].get()
        self.emp.OfficePhone = self.generalInfo.variables[2][1].get()
        self.emp.OfficeEmail = self.generalInfo.variables[3][1].get()

        self.emp.PermittedLockOn = self.permittedInfo.lockToggle.IsEnabled

        DB.save()
