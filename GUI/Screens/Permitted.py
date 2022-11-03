'''
    Shows information about a given employee at the permitted permission level (General and permitted information panels)
    Screen inherits from profile screen class
    Inherits the active Window which already has the Navigation Bar as an active component
    Uses GeneralInfo, PermittedInfo
'''


import tkinter as tk
from typing import Type
from .Profile import Profile


class Permitted(Profile):
    def __init__(self, master: Type[tk.Tk], bgColor: str='grey') -> None:
        super().__init__(master, bgColor)

        self.grid()
