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
def main():
    #this is debug must remove for use versions
    DB.search(name="Karina Gay")[0].Password="688997"
    window = GUI.Window.Window()
    window.switchFrame(Login)
    window.mainloop()



if __name__ == '__main__':
    main()
