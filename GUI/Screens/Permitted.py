'''
    Shows information about a given employee at the permitted permission level (General and permitted information panels)
    Screen inherits from profile screen class
    Inherits the active Window which already has the Navigation Bar as an active component
    Uses GeneralInfo, PermittedInfo
'''


import Profile
import Components.Panels.GeneralInfo
import Components.Panels.PermittedInfo


class Permitted(Profile):

    def __init__(self) -> None:
        pass

# Create new window components to display information
#   Image
#   General employee information
#   Permitted information
