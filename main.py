'''
    Entry point for GUI development and testing
'''


from GUI.Window import Window
from GUI.Screens.AddEmployee import AddEmployee
from GUI.Screens.Admin import Admin
from GUI.Screens.Archived import Archived
from GUI.Screens.Permitted import Permitted
from GUI.Screens.Profile import Profile
from GUI.Screens.User import User


def main():
    window = Window()
    window.switchFrame(Profile)
    window.mainloop()


if __name__ == '__main__':
    main()
