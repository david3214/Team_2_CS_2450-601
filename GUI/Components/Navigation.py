'''
    A component to be used by screens allows the user to transition screens thus navigating the application
    User can navigate to Profile, Search, and Reports
'''
import tkinter as tk
from turtle import back
from typing import Type
from styles import nav_color, med_bold, text_color, med_bold_underline
import GUI.Screens as Screens
from PIL import Image, ImageTk
from GUI.Screens.User import User
from GUI.Screens.Admin import Admin
from EmployeeContainer import EmployeeAdmin
from config import userSession

class Navigation(tk.Frame):
    def __init__(self, master: Type[tk.Tk], bgColor: str=nav_color) -> None:
        super().__init__(master, bg=bgColor, width=master.winfo_width())
        self.configure_columns_n_rows(master)
        self.grid(row=0, sticky="WENS")
        
        self.create_gui_elements()
        self.draw_nav_bar()


    def configure_columns_n_rows(self, master):        
        ## this creates spacing like so
        ## img-profile -------------img-search -------------img-reports
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=20)
        self.columnconfigure(2, weight=10)
        self.columnconfigure(3, weight=10)
        self.columnconfigure(4, weight=20)
        self.columnconfigure(5, weight=1)
        self.rowconfigure(0, weight=1)

    def create_gui_elements(self):

        # Profile Button
        img = Image.open('./images/profile.png')
        img = img.resize((25, 40))
        self.profile_image = ImageTk.PhotoImage(image=img)
        self.profile_img = tk.Label(self, bg=nav_color)
        self.profile_img.config(image=self.profile_image)

        self.profile = tk.Label(self, text='Profile', font=med_bold, 
                                bg=nav_color, foreground=text_color)
        self.profile_img.bind('<Button-1>', lambda x: self.switch_frame('Profile'))    
        self.profile.bind('<Button-1>', lambda x: self.switch_frame('Profile'))    


        # Search Button
        img = Image.open('./images/Search.png')
        img = img.resize((35, 40))
        self.search_image = ImageTk.PhotoImage(image=img)
        self.search_img = tk.Label(self, bg=nav_color)
        self.search_img.config(image=self.search_image)

        self.search = tk.Label(self, text='Search', font=med_bold, 
                                bg=nav_color, foreground=text_color)
        self.search_img.bind('<Button-1>', lambda x: self.switch_frame('Search'))    
        self.search.bind('<Button-1>', lambda x: self.switch_frame('Search'))    
        
        if userSession.PermissionLevel == 1:
            # Reports Button
            img = Image.open('./images/Reports.png')
            img = img.resize((35, 40))
            self.reports_image = ImageTk.PhotoImage(image=img)
            self.reports_img = tk.Label(self, bg=nav_color)
            self.reports_img.config(image=self.reports_image)

            self.reports = tk.Label(self, text='Reports', font=med_bold, 
                                    bg=nav_color, foreground=text_color)
            self.reports_img.bind('<Button-1>', lambda x: self.switch_frame('Reports'))    
            self.reports.bind('<Button-1>', lambda x: self.switch_frame('Reports'))
        else:
            self.reports_image = None
            self.reports_img = None
            self.reports = None

    def draw_nav_bar(self):
        # Layout
        self.profile_img.grid(row=0, column=0, sticky='E')
        self.profile.grid(row=0, column=1, sticky='W')
        self.search_img.grid(row=0, column=2, sticky='E')
        self.search.grid(row=0, column=3, sticky='W')
        if self.reports != None:
            self.reports_img.grid(row=0, column=4, sticky='E')
            self.reports.grid(row=0, column=5, sticky='W')

    def switch_frame(self, frame):
        match (frame):
            case 'Reports':
                self.master.switchFrame(Screens.Report.Report)
            case 'Search':
                self.master.switchFrame(Screens.Search.Search)
            case 'Profile':
                if userSession.PermissionLevel == 1:
                    self.master.switchFrame(Admin, EmployeeAdmin(userSession._employee))
                else:
                    self.master.switchFrame(User)
        return

    def highlight_section(self, section):
        match (section):
            case 'Report':
                self.reports.configure(font=med_bold_underline)
                self.profile.configure(font=med_bold)
                self.search.configure(font=med_bold)
            case 'Search':
                self.reports.configure(font=med_bold)
                self.profile.configure(font=med_bold)
                self.search.configure(font=med_bold_underline)
            case 'Profile':
                self.reports.configure(font=med_bold)
                self.profile.configure(font=med_bold_underline)
                self.search.configure(font=med_bold)
        