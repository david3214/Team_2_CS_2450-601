'''
    Holds tKinter, all window data, and screen
'''


import tkinter as tk
from typing import Type


class Window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title('Pay Roll')
        self.geometry('800x600')
        self.resizable(0, 0)
        self.grid_rowconfigure(1, weight=1) # Row 1 to save row 0 for navbar
        self.grid_columnconfigure(0, weight=1)
        self.frame = None


    def switchFrame(self, _frame: Type[tk.Frame]) -> None:
        '''Destroys current frame and pack a new one'''

        if self.frame is not None:
            self.frame.destroy()

        self.frame = _frame(self)
