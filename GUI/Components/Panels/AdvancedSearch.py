'''
    Shows all the options and toggles available to query the database
    Department, F Name, L Name, ID, ... Archived
    Has search button and add employee button
'''

import tkinter as tk
from tkscrolledframe import ScrolledFrame
from PIL import Image, ImageTk
from typing import Type

import GUI.Window
import GUI.Screens.AddEmployee
from GUI.Components.Image_Lbl import Image_Lbl
from styles import background_color, text_color, btn_color, sm_text, sm_bold, med_text


class AdvancedSearch(tk.Frame):

    def __init__(self, master: Type[tk.Tk], bg_color: str = background_color) -> None:

        super().__init__(master, bg=bg_color)

        # Configures grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=10)
        self.grid(row=0, column=0, sticky='NSEW')

        # Creates/configures left-most frame for advanced search widgets
        self.advanced_search_tab = tk.Frame(self, bg=bg_color)
        self.advanced_search_tab.grid_rowconfigure(0, weight=3)
        self.advanced_search_tab.grid_rowconfigure(1, weight=1)
        self.advanced_search_tab.grid_rowconfigure(2, weight=1)
        self.advanced_search_tab.grid_rowconfigure(3, weight=1)
        self.advanced_search_tab.grid_rowconfigure(4, weight=1)
        self.advanced_search_tab.grid_rowconfigure(5, weight=1)
        self.advanced_search_tab.grid_rowconfigure(6, weight=1)
        self.advanced_search_tab.grid_rowconfigure(7, weight=1)
        self.advanced_search_tab.grid_rowconfigure(8, weight=1)
        self.advanced_search_tab.grid_rowconfigure(9, weight=1)
        self.advanced_search_tab.grid_rowconfigure(10, weight=2)
        self.advanced_search_tab.grid_rowconfigure(11, weight=5)
        self.advanced_search_tab.grid_columnconfigure(0, weight=1)
        self.advanced_search_tab.grid_columnconfigure(1, weight=2)
        self.advanced_search_tab.grid(row=0, column=0, padx=15, pady=15, sticky='NSEW')

        # Defines the advanced search categories
        self.fields = ['Department', 'First Name', 'Last Name', 'Employee ID', 'Title', 'Phone #', 'Start Date',
                       'End Date', 'View Archived']

        # Creates labels for advanced search tab
        tk.Label(self.advanced_search_tab, text='Advanced Search', font=med_text, bg=bg_color, foreground=text_color) \
            .grid(row=0, column=0, columnspan=2, sticky='EW')
        for i, field in enumerate(self.fields):
            tk.Label(self.advanced_search_tab, text=field, font=med_text, bg=bg_color,
                     foreground=text_color).grid(row=i + 1, column=0, sticky='W')

        # Creates entry fields for advanced search tab
        self.entries = {}
        for i, field in enumerate(self.fields[:8]):
            entry_field = tk.Entry(self.advanced_search_tab, font=sm_text)
            entry_field.grid(row=i+1, column=1, sticky='E')
            self.entries[field] = entry_field
        self.archive_toggle = Image_Lbl(self.advanced_search_tab, bgColor=bg_color, width=60, height=30)
        self.archive_toggle.grid(row=9, column=1, sticky='E')

        # Creates buttons for searching for/adding employees
        tk.Button(self.advanced_search_tab, text='Search', font=sm_bold, bg=btn_color).grid(row=10, column=0,
                                                                                            columnspan=2,
                                                                                            sticky='EW')
        tk.Button(self.advanced_search_tab, text='Add Employee', font=sm_bold, bg=btn_color,
                  command=self.switch_frame).grid(row=11, column=0, columnspan=2, sticky='SEW')

        # Creates/configures scroll frame component
        self.scroll_frame = ScrolledFrame(self)
        self.scroll_frame.grid_rowconfigure(0, weight=1)
        self.scroll_frame.grid_columnconfigure(0, weight=1)
        self.scroll_frame.grid(row=0, column=1, sticky='NSEW')

        # Allows the scroll wheel to scroll the employee list
        self.scroll_frame.bind_scroll_wheel(master)

        # Creates/configures frame to display employees
        self.inner_frame = self.scroll_frame.display_widget(tk.Frame, bg=bg_color, fit_width=True)
        self.inner_frame.grid_columnconfigure(0, weight=1)

        # Loads in employees from the database
        self.employee_image = ImageTk.PhotoImage(Image.open('Images/profile.png'))
        self.load_employees(self.inner_frame, self.employee_image)

    # Switches windows when button is pressed
    def switch_frame(self):
        self.master.switchFrame(GUI.Screens.AddEmployee.AddEmployee(self.master))

    # Loads the employee list, with or without filtering
    def load_employees(self, container, image, entries=None):
        with open('employees.txt', 'r') as file:
            # if entries:
            #     filtered_employees = self.filter_employees(entries)

            for i, line in enumerate(file):
                employee_frame = tk.Frame(container)
                employee_frame.grid_columnconfigure(0, weight=1)
                employee_frame.grid_columnconfigure(1, weight=4)
                employee_frame.grid_columnconfigure(2, weight=4)
                employee_frame.grid_columnconfigure(3, weight=4)
                employee_frame.grid(row=i, column=0, pady=1, sticky='NSEW')

                data = line.split(',')

                employee_image = tk.Label(employee_frame)
                employee_image.config(image=image)
                employee_image.grid(row=0, column=0, padx=5)

                tk.Label(employee_frame, text=f'Employee: {data[1]}', font=sm_text).grid(row=0, column=1, padx=10,
                                                                                         sticky='W')
                tk.Label(employee_frame, text=f'Employee ID: {data[0]}', font=sm_text).grid(row=0, column=2,
                                                                                            sticky='W')
                tk.Label(employee_frame, text=f'Dept: TBA', font=sm_text).grid(row=0, column=3, padx=5, sticky='E')

    # def filter_employees(self, entries):
    #     pass
