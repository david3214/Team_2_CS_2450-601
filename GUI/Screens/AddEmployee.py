'''
    Shows all the fields of an employee (General, admin, and permitted information panels)
     for an admin to fill out and add the new employee
    Screen inherits from profile screen class
    Uses GeneralInfo
    Inherits the active Window which already has the Navigation Bar as an active component
'''

from tkinter import messagebox
import tkinter as tk
import typing
from .Profile import Profile
from ..Components.Panels.AdminInfo import AdminInfo as AI
from ..Components.Panels.PermittedInfo import PermittedInfo as PI
from ..Components.Panels.GeneralInfo import GeneralInfo as GI
from Employee.EmployeeContainer import EmployeeContainer, EmployeeAdmin
from Employee.Employee import Employee
from Config.config import DB
from Config.fetch_resource import fetch_resource
from Config.styles import background_color, btn_color, text_color, med_bold
from Config.Database import contToEmp
from ..Components.Image_Lbl import Image_Lbl


class AddEmployee(Profile):
    def __init__(self, master: tk.Tk, emp: EmployeeContainer = EmployeeAdmin(Employee()), bgColor: str = background_color) -> None:
        super().__init__(master, emp, bgColor=bgColor)

        self.img = None
        self.canvas.destroy()

        self.generalInfo.destroy()
        self.generalInfo = GI(self, editable=True)
        self.generalInfo.grid(column=0, row=0, rowspan=3, sticky='n')

        self.adminInfo = AI(self, editable=True)
        self.adminInfo.grid(column=1, row=1, sticky='nsew', padx=15, pady=15, columnspan=3)

        self.permittedInfo.destroy()
        self.permittedInfo = PI(self, btn_color, True)
        self.permittedInfo.grid(column=1, row=2, sticky='nsew', padx=15, columnspan=3)

        self.permittedInfo.lockToggle = Image_Lbl(self.permittedInfo, btn_color, 40, 40, None, fetch_resource('./Resources/images/locked.png'), fetch_resource('./Resources/images/unlocked.png'))
        if not self.emp.PermittedLockOn:
            self.permittedInfo.lockToggle.change_state()
        self.permittedInfo.lockToggle.grid(column=3, row=2, rowspan=2, sticky='e', padx=(0, 10), pady=(10, 0))

        self.addEmployeeBtn = tk.Button(self, text='Add Employee', font=med_bold, bg=btn_color, fg=text_color, command=self.addEmp)
        self.addEmployeeBtn.grid(column=1, row=3, padx=(0, 15), sticky='e')

        self.grid()

    def addEmp(self) -> None:
        if not self.generalInfo.validateAll() or not self.permittedInfo.validateAll() or not self.adminInfo.validateAll():
            return

        self.permittedInfo.lockToggle = typing.cast(Image_Lbl, self.permittedInfo.lockToggle)
        params = dict([(contToEmp[k], v) for k, v in (self.generalInfo.vals() | self.adminInfo.vals() | self.permittedInfo.vals()).items()])
        res = DB.addEmployee(**params)
        if res:
            self.emp.PermittedLockOn = self.permittedInfo.lockToggle.IsEnabled
            DB.save()
        else:
            messagebox.showerror("employee ID already exists in database")
