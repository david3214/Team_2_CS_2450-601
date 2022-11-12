'''
    This screen displays after login
    Shows all information about current user (General, admin, and permitted information panels)
    Screen inherits from profile screen class
    Navigation bar will be initialized and added to the active window
    Uses GeneralInfo, PermittedInfo, AdminInfo, Navigation
    General and permitted information can be edited
    Any updated information will be validated
'''


from GUI.Screens.Profile import Profile
from GUI.Components.Navigation import Navigation
from GUI.Components.Panels.GeneralInfo import GeneralInfo
from GUI.Components.Panels.PermittedInfo import PermittedInfo
from GUI.Components.Panels.AdminInfo import AdminInfo


class User(Profile):

    def __init__(self) -> None:
        pass

# Create new window components
#   Navigation Bar
#       Profile(underlined)
#       Search
#       Reports
#   Image
#   General employee information
#   Permitted information
#   Inputs to edit information
#   Button to update 
#       Validate changed fields
#       Save information in database
# Find employee in database and display information
