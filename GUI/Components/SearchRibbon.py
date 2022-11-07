'''
    A component that can be added to screens allowing the user to search the database
    Has a search bar, advanced search buttons, and an add employee button
'''

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from typing import Type

import GUI.Components.Panels.AdvancedSearch
import GUI.Screens.AddEmployee
from GUI.Components.UnderlineEntry import UnderlineEntry
from styles import background_color, btn_color, sm_bold, med_text, text_color


class SearchRibbon(tk.Frame):

    def __init__(self, master: Type[tk.Frame], root: Type[tk.Tk], bg_color: str = background_color) -> None:

        super().__init__(master, bg=bg_color)
        self.root = root

        # Configures grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=10)
        self.grid_columnconfigure(3, weight=5)
        self.grid(row=0, column=0, sticky='NSEW')

        # Creates buttons and entry field
        tk.Button(self, text='Advanced Search', font=sm_bold, bg=btn_color,
                  command=lambda: self.switch_frame('advanced_search')).grid(row=0, column=0, padx=25, sticky='EW')

        self.search_img = ImageTk.PhotoImage(image=Image.open('./images/Search.png').resize([40, 40]))
        self.search_image = tk.Label(self, bg=bg_color)
        self.search_image.config(image=self.search_img)
        self.search_image.grid(row=0, column=1)

        self.search_bar = UnderlineEntry(self, font=med_text, foreground=text_color, background=bg_color, insertbackground=text_color)
        self.search_bar.insert(-1, 'Search')
        
        self.default_text = True
        self.search_bar.bind('<Button-1>', self.delete_text)
        self.search_bar.grid(row=0, column=2, sticky='EW')

        tk.Button(self, text='Add Employee', font=sm_bold, bg=btn_color,
                  command=lambda: self.switch_frame('add_employee')).grid(row=0, column=3, padx=25, sticky='EW')

    # Switches to frame depending on which button is pushed
    def switch_frame(self, frame):
        match frame:
            case 'advanced_search':
                self.root.switchFrame(GUI.Components.Panels.AdvancedSearch.AdvancedSearch(self.root))
            case 'add_employee':
                self.root.switchFrame(GUI.Screens.AddEmployee.AddEmployee(self.root))

    # Removes default text in search bar when selected
    def delete_text(self, event):
        if self.default_text:
            self.search_bar.delete(0, tk.END)
            self.default_text = False
