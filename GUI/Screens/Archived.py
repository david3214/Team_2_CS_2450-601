'''
    Shows information about a given employee at the admin permission level (General, admin, and permitted information panels)
    Screen inherits from user profile screen class
    Inherits the active Window which already has the Navigation Bar as an active component
    Uses GeneralInfo, PermittedInfo, AdminInfo
    Information cannot be edited
    Employee can be unarchived
'''


import tkinter as tk
from typing import Type
from .User import User


class Archived(User):
    def __init__(self, master: Type[tk.Tk]) -> None:
        super().__init__(master)

        self.grid()
