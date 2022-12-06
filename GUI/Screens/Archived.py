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
from Employee.EmployeeContainer import EmployeeContainer
from Config.config import DB, userSession
from Config.fetch_resource import fetch_resource
from Config.styles import background_color, btn_color, text_color, med_bold

import typing
if typing.TYPE_CHECKING:
    from Window import Window

class Archived(Profile):
    def __init__(self, master: 'Window', emp: EmployeeContainer, bgColor: str=background_color) -> None:
        super().__init__(master, emp, bgColor)

        self.img = None
        self.canvas.destroy()

        self.adminInfo = AI(self)
        self.adminInfo.grid(column=1, row=1, sticky='nsew', padx=15, pady=15, columnspan=3)

        self.permittedInfo.destroy()
        self.permittedInfo = PI(self, btn_color, locked=False)
        self.permittedInfo.grid(column=1, row=2, sticky='nsew', padx=15, columnspan=3)

        self.unarchiveBtn = tk.Button(self, text='Unarchive', font=med_bold, bg=btn_color, fg=text_color, command=self.unarchive)
        self.unarchiveBtn.grid(column=1, row=3, padx=(0, 15), sticky='e')

        self.grid()


    def unarchive(self):
        from GUI.Screens.Admin import Admin
        self.emp.Active = True
        DB.save()
        self.master=typing.cast('Window',self.master)
        #Switch to admin, since only admins can view or create archived
        self.master.switchFrame(Admin, self.emp)