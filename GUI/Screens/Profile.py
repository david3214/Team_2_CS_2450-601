'''
    Shows information about a given employee at the general permission level (General information panel, locked permitted information panel)
    Inherits the active Window which already has the Navigation Bar as an active component
    Uses GeneralInfo
'''


import customtkinter as ctk
import tkinter as tk
from typing import Type
from ..Components.Panels.GeneralInfo import GeneralInfo as GI
from ..Components.Panels.PermittedInfo import PermittedInfo as PI


class Profile (ctk.CTkFrame):
    def __init__(self, master: Type[ctk.CTk]) -> None:
        super().__init__(master)
        self.generalInfo = GI(self)
        self.generalInfo.grid(column=0)

        self.canvas = tk.Canvas(self, bg='#2e2e2e', width=400, height=400, borderwidth=0, highlightthickness=0)
        self.canvas.grid(column=1, row=0)

        self.img = tk.PhotoImage(file='Images/logo.png')
        self.canvas.create_image(200, 200, image=self.img)

        self.permittedInfo = PI(self)
        self.permittedInfo.grid(column=1, row=1)

        self.grid(row=0, column=0, sticky='nsew')
