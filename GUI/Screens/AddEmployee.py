'''
    Shows all the fields of an employee (General, admin, and permitted information panels)
     for an admin to fill out and add the new employee
    Screen inherits from admin screen class
    Uses GeneralInfo
    Inherits the active Window which already has the Navigation Bar as an active component
    Input fields will be validated for proper inputs
'''


from GUI.Screens.Admin import Admin
from GUI.Components.Panels.GeneralInfo import GeneralInfo


class AddEmployee(Admin):

    def __init__(self) -> None:
        pass

# Create new empty Employee object.
# Open Employee object in a copy of profile screen except with update button replaced with add button. On click: Employee object is added to database. Goto search screen.
