'''
    This screen displays after login
    Shows all information about current user (General, admin, and permitted information panels)
    Screen inherits from profile screen class
    Navigation bar will be initialized and added to the active window
    Uses GeneralInfo, PermittedInfo, AdminInfo, Navigation
    General and permitted information can be edited
    Any updated information will be validated
'''


import Profile
import Components.Navigation
import Components.Panels.GeneralInfo
import Components.Panels.PermittedInfo
import Components.Panels.AdminInfo


class Admin(Profile):

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
