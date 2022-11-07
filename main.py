'''
    Entry point for GUI development and testing
'''
#? TODO: Decide if we want to refactor p5.py into this new entry point

import GUI.Window
from GUI.Screens.Login import Login
from GUI.Screens.Report import Report
from GUI.Screens.Search import Search

def main():
    window = GUI.Window.Window()
    # window.switchFrame(Login)
    window.switchFrame(Search)
    window.mainloop()


if __name__ == '__main__':
    main()
