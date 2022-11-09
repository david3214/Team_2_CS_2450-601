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

from GUI.Components.SearchRibbon import SearchRibbon
from GUI.Components.Panels.ScrollableSearch import ScrollableSearch
from GUI.Components.Panels.AdvancedSearch import AdvancedSearch
from styles import background_color, sm_text
from config import DB

class Search(tk.Frame):

    def __init__(self, master: Type[tk.Tk], bg_color: str = background_color) -> None:
        super().__init__(master, bg=bg_color)
        self.bg_color = bg_color

        # Configures grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=6)
        self.grid_columnconfigure(0, weight=1)
        self.grid(row=1, column=0, sticky='NSEW')

        # Creates search ribbon component
        self.searchRibbon = SearchRibbon(self, master, searchFunc=self.search)
        self.searchRibbon.grid(row=0, column=0, sticky='NSEW')

        self.scrollableSearch = ScrollableSearch(self, master)
        self.scrollableSearch.grid(row=1, column=0, sticky='NSEW')
        # Creates/configures scroll frame component
        # self.scroll_frame = ScrolledFrame(self, background='white')

        # Allows the scroll wheel to scroll the employee list
        # self.scroll_frame.bind_scroll_wheel(master)

        # # Creates/configures frame to display employees
        # self.inner_frame = self.scroll_frame.display_widget(tk.Frame, bg=bg_color, fit_width=True)
        # self.inner_frame.grid_columnconfigure(0, weight=1)

        # Loads in employees from the database
        # self.employee_img = ImageTk.PhotoImage(image=Image.open('./images/ListEmp.png').resize((35,35)))

        self.search(name='')

    def search(self, *args, name = None):
        self.scrollableSearch.clearSearchFrame()
        searchName = name
        if searchName == None:
            searchName = self.searchRibbon.search_bar.get()
        employees = DB.search(name=searchName)
        self.scrollableSearch.changeList(employees)

    def updateScrollableSearch(self, employees):
        self.scrollableSearch.clearSearchFrame()
        self.scrollableSearch.changeList(employees)


    def advancedSearch(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=7)
        self.searchRibbon.destroy()
        self.scrollableSearch.advancedSearch = True
        self.scrollableSearch.grid(row=0, column=1, sticky='NSEW')  
        self.scrollableSearch.redraw()
        self.advanced_search = AdvancedSearch(self, self.master, bg_color=self.bg_color)
        self.advanced_search.grid(row=0, column=0, sticky='NSEW')

    def __str__():
        return 'Search'


# Underline Search navigation component
# Create new window components
#   Search Bar
#   Advanced Search Button
#   Add employee button (admin)
# Get input from search bar and query the database
# Create the components to display the results and add them to the window
#   If no employees were found indicate so to the user
