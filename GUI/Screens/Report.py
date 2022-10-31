'''
    Shows options for generating the database report and the button to do so, as well as import a database
    Inherits the active Window which already has the Navigation Bar as an active component
    Will be able to filter archived employees based on toggle
    Will be able to include or omit admin info based on toggle
    Button to import database file
    Button to generate the report
'''
from msilib.schema import Font
import tkinter as tk
from tkinter import colorchooser
from PIL import ImageTk, Image
from typing import Type

class Report (tk.Frame):
    def __init__(self, master: Type[tk.Tk], bgColor: str='grey') -> None:
        super().__init__(master, bg=bgColor)
        self.grid(row=1, column=0)
        self.pack(expand=1, fill='both')
        self.archived_enabled = Toggle_Lbl(self, bgColor, width=60, height=30)
        self.archived_lbl = tk.Label(self, text='Archived Employees', font=('Arial', 25), bg='grey', foreground='white')
        self.admin_enabled = Toggle_Lbl(self, bgColor, width=60, height=30)
        self.archived_lbl.grid(row=1, column=0)
        self.archived_enabled.grid(row=1, column=1)
        self.admin_enabled.grid(row=1, column=3)



class Toggle_Lbl(tk.Label):
    
    def __init__(self, master: Type[tk.Frame], bgColor: str, width, height, **kwargs) -> None:
        super().__init__(master, bg=bgColor, width=width, height=height, **kwargs)
        self.IsEnabled = True
        img = Image.open('./images/on.png')
        img = img.resize((width, height))
        self.on_image = ImageTk.PhotoImage(image=img)
        img = Image.open('./images/off.png')
        img = img.resize((width, height))
        self.off_image = ImageTk.PhotoImage(image=img)
        self.config(image = self.on_image)
        self.bind('<Button-1>', self.change_state)
    
    def change_state(self, *args):
        if self.IsEnabled is True:
            self.IsEnabled = False
            self.config(image = self.off_image)
        else:
            self.IsEnabled = True
            self.config(image = self.on_image)

    def _resize_image(self, event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)

    

# Create new window components
#   Achieved Employees toggle
#   Admin info toggle
#   Export Employee List Button
