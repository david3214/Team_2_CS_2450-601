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

        # This will be the employee list
        self.scrollableSearch = ScrollableSearch(self, master)
        self.scrollableSearch.grid(row=1, column=0, sticky='NSEW')
        
        # Search for all employees, and it will auto sort alphabetically
        self.search(name='')

    def search(self, *args, name = None):
        # If we are given a specific name use that, otherwise use the search bar
        searchName = name
        if searchName == None:
            searchName = self.searchRibbon.search_bar.get()
        employees = DB.search(name=searchName)
        self.scrollableSearch.changeList(employees)

    def updateScrollableSearch(self, employees):
        self.scrollableSearch.changeList(employees)


    def advancedSearch(self):
        # the grid configuration changes when we have the advanced sidebar open
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=7)

        # get rid of the top search ribbon
        self.searchRibbon.destroy()
        self.scrollableSearch.advancedSearch = True
        self.scrollableSearch.grid(row=0, column=1, sticky='NSEW')  
        self.scrollableSearch.redraw()

        # Add the advanced Search frame
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
