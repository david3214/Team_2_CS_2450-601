'''
    Holds tKinter, all window data, and screen
'''


import tkinter as tk
from typing import Type
from GUI.Components.Navigation import Navigation
from GUI.Screens.Login import Login
from Employee.EmployeeContainer import EmployeeContainer
from Config.styles import background_color
import typing


class Window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title('Pay Roll')
        self.geometry('800x600')
        self.resizable(False, False)
        self.frame = None
        self.configure(bg=background_color)
        self.navigation = None
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=30)
        self.columnconfigure(0, weight=1)

    def switchFrame(self, _frame: tk.Frame | Type[tk.Frame], emp: typing.Optional[EmployeeContainer] = None) -> None:
        '''Destroys current frame and packs a new one'''
        if issubclass(type(_frame), tk.Frame):
            _frame = type(_frame)
        if self.frame is not None:
            self.frame.destroy()

        if _frame is Login:
            self.navigation = None
        else:
            self.navigation = Navigation(self)
            self.navigation.highlight_section(str(_frame))

        self.frame = typing.cast('type', _frame)(self) if emp == None else typing.cast('type', _frame)(self, emp)
