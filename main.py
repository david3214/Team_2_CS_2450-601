'''
    Entry point for GUI development and testing
'''
#? TODO: Decide if we want to refactor p5.py into this new entry point

import GUI.Window
import GUI.Screens.Login


def main():
    window = GUI.Window.Window()
    window.switchFrame(GUI.Screens.Login.Login)
    window.mainloop()


if __name__ == '__main__':
    main()
