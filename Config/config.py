'''
Sets up database and user session.
'''

from Config.Database import Database
from pathlib import Path
from Employee.Employee import Employee
from Employee.EmployeeContainer import EmployeeSelf
from Config.fetch_resource import fetch_resource
from pathlib import Path


# DB = Database(Path(os.path.abspath("database.csv")))
DB = Database(fetch_resource(r"./Resources/database.csv"))
userSession = EmployeeSelf(Employee(Permission_level=1))