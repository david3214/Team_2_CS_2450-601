'''
    Shows all the options and toggles available to query the database
    Department, F Name, L Name, ID, ... Archived
    Has search button and add employee button
'''

import tkinter as tk

import typing
import GUI.Window
import GUI.Screens.AddEmployee
from GUI.Components.Image_Lbl import Image_Lbl
from GUI.Components.UnderlineEntry import UnderlineEntry
from Config.styles import background_color, text_color, btn_color, sm_text, med_bold, med_text
from Config.config import DB, userSession

if typing.TYPE_CHECKING:
    from GUI.Window import Window
    from Screens.Search import Search
from Employee.Employee import Employee
from Employee.EmployeeContainer import EmployeeContainer


class AdvancedSearch(tk.Frame):

    fieldsToDB = {'Department': 'Department', 'First Name': 'fName', 'Last Name': 'lName', 'Employee ID': 'Employee_ID', 'Title':'Title', 
                  'Phone #': 'oPhone', 'Start Date': 'StartDate', 'End Date': 'EndDate'}
    def __init__(self, master: 'Search', root: 'Window', bg_color: str = background_color) -> None:

        super().__init__(master, bg=bg_color)
        self.master=typing.cast('Search',self.master)
        self.root:Window = root
        # Creates/configures left-most frame for advanced search widgets
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=1)
        self.grid_rowconfigure(9, weight=1)
        self.grid_rowconfigure(10, weight=2)
        self.grid_rowconfigure(11, weight=5)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        # Defines the advanced search categories
        self.fields = ['Department', 'First Name', 'Last Name', 'Employee ID', 'Title', 'Phone #', 'Start Date', 'End Date', 'View Archived']

        # Creates labels for advanced search tab
        tk.Label(self, text='Advanced Search', font=med_text, bg=bg_color, foreground=text_color) \
            .grid(row=0, column=0, columnspan=2, sticky='EW')
        for i, field in enumerate(self.fields):
            if field == 'View Archived' and userSession.PermissionLevel != 1:
                continue
            tk.Label(self, text=field, font=med_text, bg=bg_color,foreground=text_color).grid(row=i + 1, column=0, sticky='W')

        # Creates entry fields for advanced search tab
        self.entries = {}
        for i, field in enumerate(self.fields[:8]):
            entry_field = UnderlineEntry(self, name=field, background=bg_color, font=sm_text, foreground=text_color,  insertbackground=text_color)
            entry_field.grid(row=i+1, column=1, sticky='E')
            entry_field.bind('<Return>', self.searchAdvanced)
            self.entries[field] = entry_field
        
        if userSession.PermissionLevel == 1:
            self.archive_toggle = Image_Lbl(self, bgColor=bg_color, width=60, height=30)
            self.archive_toggle.grid(row=9, column=1, sticky='E')
        else:
            self.archive_toggle = None

        # Creates buttons for searching for/adding employees
        self.search_btn = tk.Button(self, text='Search', font=med_bold, bg=btn_color,
                                    foreground=text_color, command=self.searchAdvanced)
        self.search_btn.grid(row=10, column=0, columnspan=2, sticky='EW', padx=20)
        if userSession.PermissionLevel == 1:
            self.add_btn = tk.Button(self, text='Add Employee', font=med_bold, bg=btn_color,
                                    foreground=text_color, command=self.addEmployee)
            self.add_btn.grid(row=11, column=0, columnspan=2, sticky='SEW', padx=20)

    # Switches windows when button is pressed
    def addEmployee(self):
        self.root.switchFrame(GUI.Screens.AddEmployee.AddEmployee(self.root,EmployeeContainer(Employee())))

    def searchAdvanced(self, *args):
        employees = DB.search(**self.getAllNonEmptyEntries())
        self.master.updateScrollableSearch(employees)

    def getAllNonEmptyEntries(self):
        # We only want to search for fields that have actual values and not just default values
        nonEmpties = dict()
        for key, value in self.entries.items():
            if value.get() != '' and value.get() != key:
                nonEmpties[self.fieldsToDB[key]] = value.get()
        if self.archive_toggle == None:
            nonEmpties['Archived'] = False
        else:
            nonEmpties['Archived'] = self.archive_toggle.IsEnabled
        return nonEmpties

    # Removes default text in search bar when selected
    def delete_text(self, event):
        if self.default_text:
            self.master.searchRibbon.search_bar.delete(0, tk.END)
            self.default_text = False
