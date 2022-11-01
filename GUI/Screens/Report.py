'''
    Shows options for generating the database report and the button to do so, as well as import a database
    Inherits the active Window which already has the Navigation Bar as an active component
    Will be able to filter archived employees based on toggle
    Will be able to include or omit admin info based on toggle
    Button to import database file
    Button to generate the report
'''
import tkinter as tk
from PIL import ImageTk, Image
from styles import med_bold, background_color, text_color, btn_color
from typing import Type

class Report (tk.Frame):
    def __init__(self, master: Type[tk.Tk], bgColor: str=background_color) -> None:
        super().__init__(master, bg=bgColor, width=master.winfo_width())
        self.configure_columns_n_rows(master)
        self.grid(row=1, sticky='WENS')
        
        self.create_gui_elements()
        


    def configure_columns_n_rows(self, master):
        master.rowconfigure(0, weight=1)
        master.rowconfigure(1, weight=9)
        master.columnconfigure(0, weight=10)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=7)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=5)

    def create_gui_elements(self):
        ## Create the archived label and toggle
        self.archived_enabled = Toggle_Lbl(self, background_color, width=60, height=30)
        self.archived_lbl = tk.Label(self, text='Archived Employees', 
                                     font=med_bold, bg=background_color, foreground=text_color)
        
        ## Create the admin Label and toggle
        self.admin_enabled = Toggle_Lbl(self, background_color, width=60, height=30)
        self.admin_lbl = tk.Label(self, text='Admin Info', 
                                     font=med_bold, bg=background_color, foreground=text_color)
        
        ## Create the import and export buttons
        self.export_btn = tk.Button(self, text='Export Database Report', font=med_bold, foreground=text_color, 
                                        background=btn_color, command=self.export_database)
        self.import_btn = tk.Button(self, text='Import Database File', font=med_bold, foreground=text_color, 
                                        background=btn_color, command=self.import_database)

        ## Place the first row of items    
        self.archived_lbl.grid(row=0, column=0)
        self.archived_enabled.grid(row=0, column=1)
        self.admin_lbl.grid(row=0, column=2)
        self.admin_enabled.grid(row=0, column=3)
        self.export_btn.grid(row=0, column=4)

        ## Place the import button on the second row, centered at the top
        self.import_btn.grid(row=1, column=0, columnspan=5, sticky='N')

    
    def import_database(self):
        # Call the import database function
        pass


    def export_database(self):
        adminInfo = self.admin_enabled.IsEnabled
        archivedInfo = self.archived_enabled.IsEnabled
        
        # call the export function, using these parameters



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

    

# Create new window components
#   Achieved Employees toggle
#   Admin info toggle
#   Export Employee List Button
