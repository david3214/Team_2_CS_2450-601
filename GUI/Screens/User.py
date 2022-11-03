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


class User(Profile):
    def __init__(self, master: Type[tk.Tk], bgColor: str='grey') -> None:
        super().__init__(master, bgColor)

        self.grid()
