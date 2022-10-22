'''
    Shows information about a given employee at the admin permission level (General, admin, and permitted information panels)
    Screen inherits from user profile screen class
    Inherits the active Window which already has the Navigation Bar as an active component
    Uses GeneralInfo, PermittedInfo, AdminInfo
    Information cannot be edited
    Employee can be unarchived

'''


import User
import Components.Panels.GeneralInfo
import Components.Panels.PermittedInfo
import Components.Panels.AdminInfo


class Archived(User):

    def __init__(self) -> None:
        pass

# Create new window components to display information
#   Image
#   General employee information
#   Permitted information
#   Button to unarchive
# Find employee in database and display all information accessible to admin permission leve
