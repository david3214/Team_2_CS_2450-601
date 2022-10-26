'''
    Shows information about a given employee at the general permission level (General information panel, locked permitted information panel)
    Inherits the active Window which already has the Navigation Bar as an active component
    Uses GeneralInfo
'''


import tkinter as tk
from typing import Type
from ..Components.Panels.GeneralInfo import GeneralInfo as GI


class Profile (tk.Frame):
    def __init__(self, master: Type[tk.Tk], bgColor: str='grey') -> None:
        super().__init__(master, bg=bgColor)
        self.generalInfo = GI(self)
        self.generalInfo.grid()
        #self.img = tk.Label(master, image=)
        #self.img.grid(column=1)

        self.pack(expand=1, fill='both')

# Create new window components to display information
#   Image
#   General employee information
#   Permitted information (locked)
