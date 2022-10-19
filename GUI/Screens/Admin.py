'''
    Shows information about a given employee at the admin permission level (General, admin, and permitted information panels)
    Screen inherits from profile screen class
    Inherits the active Window which already has the Navigation Bar as an active component
    Uses GeneralInfo, PermittedInfo, AdminInfo
    Information can be edited
    Edited fields must be re-validated
    Employee can be archived
    Pay report can be generated
'''


import Profile
import Components.Panels.GeneralInfo
import Components.Panels.PermittedInfo
import Components.Panels.AdminInfo


class Admin(Profile):
    '''TODO'''

    def __init__(self) -> None:
        '''TODO'''
        pass

# Create new window components to display information
#   Image
#   General employee information
#   Permitted information
#   Inputs to edit all information
#   Button to update 
#       Validate updated fields
#       Save new information in database
#   Button to generate pay report
#       Gen pay rep
#       Button to archive
# Find employee in database and display all information accessible to admin permission level
