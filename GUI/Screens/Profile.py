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

        self.grid_columnconfigure(1, weight=1)

        self.generalInfo = GI(self)
        self.generalInfo.grid(column=0, row=0, rowspan=3, sticky='n')

        self.permittedInfo = PI(self)
        self.permittedInfo.grid(column=1, row=1, sticky='nsew', padx=15, pady=(0, 15))

        self.canvas = tk.Canvas(self, bg=bgColor, width=300, height=300, borderwidth=0, highlightthickness=0)
        self.img = tk.PhotoImage(file='Images/logo1.png')
        self.canvas.create_image(150, 150, image=self.img)
        self.canvas.grid(column=1, row=0, sticky='w', padx=15, pady=15)

        self.grid(row=0, column=0, sticky='nsew')
