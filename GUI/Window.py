'''
    Holds tKinter, all window data, and screen
'''


import customtkinter as ctk
from typing import Type


class Window(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        ctk.set_appearance_mode('System')
        ctk.set_default_color_theme('green')

        self.iconbitmap('Images/icon.ico')
        self.title('Pay Roll')
        self.geometry('800x600')
        self.resizable(0, 0)
        self.grid_rowconfigure(1, weight=1) # Row 1 to save row 0 for navbar
        self.grid_columnconfigure(0, weight=1)
        self.frame = None


    def switchFrame(self, _frame: Type[ctk.CTkFrame]) -> None:
        '''Destroys current frame and pack a new one'''

        if self.frame is not None:
            self.frame.destroy()

        self.frame = _frame(self)
