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
from Employee.EmployeeContainer import EmployeeContainer
from Config.styles import background_color, btn_color
import typing
if typing.TYPE_CHECKING:
    from Window import Window

    
class Permitted(Profile):
    def __init__(self, master: 'Window', emp: EmployeeContainer, bgColor: str=background_color) -> None:
        super().__init__(master, emp, bgColor)

        self.permittedInfo.destroy()
        self.permittedInfo = PI(self, btn_color, locked=False)
        self.permittedInfo.grid(column=1, row=1, sticky='nsew', padx=15, pady=(0, 15), columnspan=3)

        self.grid()
