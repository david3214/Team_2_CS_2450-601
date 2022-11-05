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
from .Profile import Profile
from ..Components.Panels.AdminInfo import AdminInfo as AI
from ..Components.Panels.PermittedInfo import PermittedInfo as PI


class Archived(Profile):
    def __init__(self, master: Type[tk.Tk], bgColor: str='grey') -> None:
        super().__init__(master, bgColor)

        self.img = None
        self.canvas.destroy()

        self.adminInfo = AI(self)
        self.adminInfo.grid(column=1, row=0, sticky='nsew', padx=15, pady=15, columnspan=3)

        self.permittedInfo.destroy()
        self.permittedInfo = PI(self, 'blue', locked=False)
        self.permittedInfo.grid(column=1, row=1, sticky='nsew', padx=15, columnspan=3)

        self.unarchiveBtn = tk.Button(self, text='Unarchive', font=('Arial', 12, 'bold'), bg='blue', fg='white')
        self.unarchiveBtn.grid(column=1, row=2, padx=(0, 15), sticky='e')

        self.grid()
