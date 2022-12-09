'''
    A toggleable button.
'''

import tkinter as tk
from PIL import ImageTk, Image
from typing import Type
from Config.fetch_resource import fetch_resource

TGL_ON = fetch_resource('./Resources/images/on.png')
TGL_OFF = fetch_resource('./Resources/images/off.png')


class Image_Lbl(tk.Label):

    def __init__(self, master: tk.Frame, bgColor: str, width, height, command=None, start_img=TGL_ON, off_image=TGL_OFF, **kwargs) -> None:
        super().__init__(master, bg=bgColor, width=width, height=height, **kwargs)
        self.IsEnabled = True
        img = Image.open(start_img)
        img = img.resize((width, height))
        self.on_image = ImageTk.PhotoImage(image=img)
        img = Image.open(off_image)
        img = img.resize((width, height))
        self.off_image = ImageTk.PhotoImage(image=img)
        self.config(image=self.on_image)
        # Image_Lbl is never called with command set
        # if command is not NULL:
        #  self.bind('<Button-1>', command)
        # else:
        self.bind('<Button-1>', self.change_state)

    def change_state(self, *args):
        if self.IsEnabled is True:
            self.IsEnabled = False
            self.config(image=self.off_image)
        else:
            self.IsEnabled = True
            self.config(image=self.on_image)
