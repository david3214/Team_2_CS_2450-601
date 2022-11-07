'''
    Shows information about a given employee at the permitted permission level (General and permitted information panels)
    Screen inherits from profile screen class
    Inherits the active Window which already has the Navigation Bar as an active component
    Uses GeneralInfo, PermittedInfo
'''


from GUI.Screens.Profile import Profile
from Components.Panels.GeneralInfo import GeneralInfo0
from Components.Panels.PermittedInfo import PermittedInfo


class Permitted(Profile):

    def __init__(self) -> None:
        pass

# Create new window components to display information
#   Image
#   General employee information
#   Permitted information
