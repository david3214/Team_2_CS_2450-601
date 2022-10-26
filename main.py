'''
    Entry point for GUI development and testing
'''
#? TODO: Decide if we want to refactor p5.py into this new entry point

from GUI.Window import Window
from GUI.Screens.Profile import Profile as screen


def main():
    window = Window()
    window.switchFrame(screen)
    window.mainloop()


if __name__ == '__main__':
    main()
