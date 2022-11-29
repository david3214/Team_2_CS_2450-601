'''
Sets up database and user session.
'''

from Config.Database import Database
from pathlib import Path
from Employee.Employee import Employee
from Employee.EmployeeContainer import EmployeeSelf
from Config.fetch_resource import fetch_resource
from pathlib import Path
DB_PATH: str='./Resources/database.csv'

DB = Database(fetch_resource(DB_PATH))
userSession = EmployeeSelf(Employee(Permission_level=1))
