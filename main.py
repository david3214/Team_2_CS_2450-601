'''
    Entry point for GUI development and testing
'''

import GUI.Window
from GUI.Screens.Login import Login
from GUI.Screens.Report import Report
from GUI.Screens.Search import Search
from config import DB
from Database import Database
from pathlib import Path
from GUI.Components.Panels.PermittedInfo import PermittedInfo
from config import userSession, DB, fetch_resource
from EmployeeContainer import EmployeeAdmin
def main():
    window = GUI.Window.Window()
    window.switchFrame(Login)
    window.mainloop()



if __name__ == '__main__':
    main()
