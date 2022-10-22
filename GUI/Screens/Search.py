'''
    Shows results of database query
    Screen inherits from search screen class
    Inherits the active Window which already has the Navigation Bar as an active component
    Uses SearchRibbon, AdvancedSearch, EmployeeResult
    Starts empty and is filled with results of search
    Compare input to database entries
    Allows admins to access add employee screen
'''


import Components.SearchRibbon
import Components.Panels.AdvancedSearch
import Components.EmployeeResult


class Search:

    def __init__(self) -> None:
        pass

# Underline Search navigation component
# Create new window components
#   Search Bar
#   Advanced Search Button
#   Add employee button (admin)
# Get input from search bar and query the database
# Create the components to display the results and add them to the window
#   If no employees were found indicate so to the user
