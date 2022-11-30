'''
    Entry point for GUI development and testing
'''

import GUI.Window
from GUI.Screens.Login import Login
def main():
    window = GUI.Window.Window()
    window.switchFrame(Login)
    window.mainloop()


if __name__ == '__main__':
    main()
