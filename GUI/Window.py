'''
    Holds tKinter, all window data, and screen
'''


import tkinter as tk
from typing import Type
from styles import background_color

class Window(tk.Tk):

    def __init__(self) -> None:
        super().__init__()

        self.title('Pay Roll')
        self.geometry('800x600')
        self.resizable(0, 0)
        self.frame = None
        self.configure(bg=background_color)


    def switchFrame(self, _frame: Type[tk.Frame]) -> None:
        '''Destroys current frame and pack a new one'''

        if self.frame is not None:
            self.frame.destroy()

        self.frame = _frame(self)
        #* frame.pack() should be called by the constructor

