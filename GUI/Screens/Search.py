'''
    Shows results of database query
    Screen inherits from search screen class
    Inherits the active Window which already has the Navigation Bar as an active component
    Uses SearchRibbon, AdvancedSearch, EmployeeResult
    Starts empty and is filled with results of search
    Compare input to database entries
    Allows admins to access add employee screen
'''

import tkinter as tk
from tkscrolledframe import ScrolledFrame
from PIL import Image, ImageTk
from typing import Type

import GUI.Components.SearchRibbon
from styles import background_color, sm_text


class Search(tk.Frame):

    def __init__(self, master: Type[tk.Tk], bg_color: str = background_color) -> None:
        super().__init__(master, bg=bg_color)

        # Configures grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=6)
        self.grid_columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky='NSEW')

        # Creates search ribbon component
        GUI.Components.SearchRibbon.SearchRibbon(self, master).grid(row=0, column=0, sticky='NSEW')

        # Creates/configures scroll frame component
        self.scroll_frame = ScrolledFrame(self)
        self.scroll_frame.grid_rowconfigure(0, weight=1)
        self.scroll_frame.grid_columnconfigure(0, weight=1)
        self.scroll_frame.grid(row=1, column=0, sticky='NSEW')

        # Allows the scroll wheel to scroll the employee list
        self.scroll_frame.bind_scroll_wheel(master)

        # Creates/configures frame to display employees
        self.inner_frame = self.scroll_frame.display_widget(tk.Frame, bg=bg_color, fit_width=True)
        self.inner_frame.grid_columnconfigure(0, weight=1)

        # Loads in employees from the database
        with open('employees.txt', 'r') as file:
            self.employee_img = ImageTk.PhotoImage(image=Image.open('./images/profile.png'))

            for i, line in enumerate(file):
                employee_frame = tk.Frame(self.inner_frame)
                employee_frame.grid_columnconfigure(0, weight=1)
                employee_frame.grid_columnconfigure(1, weight=4)
                employee_frame.grid_columnconfigure(2, weight=4)
                employee_frame.grid_columnconfigure(3, weight=4)
                employee_frame.grid(row=i, column=0, pady=1, sticky='NSEW')

                data = line.split(',')

                self.employee_image = tk.Label(employee_frame)
                self.employee_image.config(image=self.employee_img)
                self.employee_image.grid(row=0, column=0)

                tk.Label(employee_frame, text=f'Employee: {data[1]}', font=sm_text).grid(row=0, column=1, padx=15,
                                                                                         sticky='W')
                tk.Label(employee_frame, text=f'Employee ID: {data[0]}', font=sm_text).grid(row=0, column=2,
                                                                                            sticky='W')
                tk.Label(employee_frame, text=f'Dept: TBA', font=sm_text).grid(row=0, column=3, padx=15, sticky='E')

    def __str__(self):
        return 'Search'


# Underline Search navigation component
# Create new window components
#   Search Bar
#   Advanced Search Button
#   Add employee button (admin)
# Get input from search bar and query the database
# Create the components to display the results and add them to the window
#   If no employees were found indicate so to the user
