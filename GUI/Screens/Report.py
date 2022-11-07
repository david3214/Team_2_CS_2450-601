'''
    Shows options for generating the database report and the button to do so, as well as import a database
    Inherits the active Window which already has the Navigation Bar as an active component
    Will be able to filter archived employees based on toggle
    Will be able to include or omit admin info based on toggle
    Button to import database file
    Button to generate the report
'''
import tkinter as tk
from tkinter import filedialog
from GUI.Components.Navigation import Navigation
from GUI.Components.Image_Lbl import Image_Lbl
from styles import med_bold, background_color, text_color, btn_color
from typing import Type
from pathlib import Path
from config import DB

class Report (tk.Frame):
    def __init__(self, master: Type[tk.Tk], bgColor: str=background_color) -> None:
        super().__init__(master, bg=bgColor, width=master.winfo_width())
        self.configure_columns_n_rows(master)
        # self.nav_bar = Navigation(master)
        self.grid(row=1, sticky='WENS')
        
        self.create_gui_elements()
        

    def configure_columns_n_rows(self, master):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=50)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=5)

    def create_gui_elements(self):
        ## Create the archived label and toggle
        self.archived_enabled = Image_Lbl(self, background_color, width=60, height=30)
        self.archived_lbl = tk.Label(self, text='Archived Employees', 
                                     font=med_bold, bg=background_color, foreground=text_color)
        
        ## Create the admin Label and toggle
        self.admin_enabled = Image_Lbl(self, background_color, width=60, height=30)
        self.admin_lbl = tk.Label(self, text='Admin Info', 
                                     font=med_bold, bg=background_color, foreground=text_color)
        
        ## Create the import and export buttons
        self.export_btn = tk.Button(self, text='Export Database Report', font=med_bold, foreground=text_color, 
                                        background=btn_color, command=self.export_database)
        self.import_btn = tk.Button(self, text='Import Database File', font=med_bold, foreground=text_color, 
                                        background=btn_color, command=self.import_database)

        ## Place the first row of items    
        self.archived_lbl.grid(row=0, column=0, pady=10)
        self.archived_enabled.grid(row=0, column=1, pady=10)
        self.admin_lbl.grid(row=0, column=2, pady=10)
        self.admin_enabled.grid(row=0, column=3, pady=10)
        self.export_btn.grid(row=0, column=4, pady=10)

        ## Place the import button on the second row, centered at the top
        self.import_btn.grid(row=1, column=0, columnspan=5, sticky='N')

    
    def import_database(self):
        # Call the import database function
        csvPath = filedialog.askopenfile(filetypes = (("csv file (*.csv)", "*.csv"),))
        DB.importDB(Path(csvPath.name))


    def export_database(self):
        adminInfo = self.admin_enabled.IsEnabled
        archivedInfo = self.archived_enabled.IsEnabled

        csvPath = filedialog.asksaveasfilename(defaultextension = "*.csv", filetypes = (("csv file (*.csv)", "*.csv"),))

        DB.exportDB(csvPath, adminInfo=adminInfo, showArchivedEmployees=archivedInfo)
        
        # call the export function, using these parameters


    def __str__():
        return 'Report'


# Create new window components
#   Achieved Employees toggle
#   Admin info toggle
#   Export Employee List Button
