'''
    Shows information about a given employee at the permitted permission level (General and permitted information panels)
    Screen inherits from profile screen class
    Inherits the active Window which already has the Navigation Bar as an active component
    Uses GeneralInfo, PermittedInfo
'''


import tkinter as tk
from typing import Type
from .Profile import Profile
from ..Components.Panels.PermittedInfo import PermittedInfo as PI

class Permitted(Profile):
    def __init__(self, master: Type[tk.Tk], bgColor: str='grey') -> None:
        super().__init__(master, bgColor)

        self.permittedInfo.destroy()
        self.permittedInfo = PI(self, 'blue', True, False)
        self.permittedInfo.grid(column=1, row=1, sticky='nsew', padx=15, pady=(0, 15), columnspan=3)

        self.grid()
