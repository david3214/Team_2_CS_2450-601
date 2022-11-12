'''
    Entry point for GUI development and testing
'''
# ? TODO: Decide if we want to refactor p5.py into this new entry point

#import GUI.Window
#from GUI.Screens.Login import Login
#from GUI.Screens.Report import Report
from Database import Database
from pathlib import Path

import GUI.Window
from GUI.Screens.Login import Login
from GUI.Screens.Report import Report
from GUI.Screens.Search import Search
from config import DB


def main():
    #window = GUI.Window.Window()
    # window.switchFrame(Login)
    # window.mainloop()
    db = Database(Path("employees.csv"))
    db.exportDB(Path("out.csv"), adminInfo=True)


if __name__ == '__main__':
    main()
