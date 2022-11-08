'''
    Holds tKinter, all window data, and screen
'''


from asyncio.windows_events import NULL
import tkinter as tk
from typing import Type
from GUI.Components.Navigation import Navigation
from GUI.Screens.Login import Login
from styles import background_color

class Window(tk.Tk):

    def __init__(self) -> None:
        super().__init__()

        self.title('Pay Roll')
        self.geometry('800x600')
        self.resizable(0, 0)
        self.frame = None
        self.configure(bg=background_color)
        self.navigation = NULL
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=30)
        self.columnconfigure(0, weight=1)

    def switchFrame(self, _frame: Type[tk.Frame]) -> None:
        '''Destroys current frame and pack a new one'''

        if self.frame is not None:
            self.frame.destroy()

        if _frame is Login:
            self.navigation = NULL
        else:
            self.navigation = Navigation(self)
            self.navigation.highlight_section(_frame.__str__())

        self.frame = _frame(self)
