from Database import Database
from pathlib import Path
from Employee import Employee
from EmployeeContainer import EmployeeSelf
import os

DB = Database(Path(os.path.abspath("database.csv")))
userSession = EmployeeSelf(Employee(Permission_level=1))
