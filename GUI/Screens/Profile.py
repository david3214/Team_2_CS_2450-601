'''
    Shows information about a given employee at the general permission level (General information panel, locked permitted information panel)
    Inherits the active Window which already has the Navigation Bar as an active component
    Uses GeneralInfo
'''


import tkinter as tk
from typing import Type
from ..Components.Panels.GeneralInfo import GeneralInfo as GI
from ..Components.Panels.PermittedInfo import PermittedInfo as PI


class Profile (tk.Frame):
    def __init__(self, master: Type[tk.Tk], bgColor: str='grey') -> None:
        super().__init__(master, bg=bgColor)
        self.generalInfo = GI(self)
        self.generalInfo.grid(column=0)

        self.permittedInfo = PI(self)
        self.permittedInfo.grid(column=1, row=1)

        self.img = tk.PhotoImage(file='Images/logo.png')
        self.img = self.img.subsample(2, 2)
        self.imgL = tk.Label(self, image=self.img)
        self.imgL.grid(column=1,row=0)

        self.grid(row=0, column=0, sticky='nsew')
