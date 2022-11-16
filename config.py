'''
Sets up database and user session.
'''

from Database import Database
from pathlib import Path
from Employee import Employee
from EmployeeContainer import EmployeeSelf
import os
import sys
from pathlib import Path


def fetch_resource(rsrc_path):
  """Loads resources from the temp dir used by pyinstaller executables"""
  try:
    base_path = Path(sys._MEIPASS)
  except AttributeError:
    return rsrc_path  # not running as exe, just return the unaltered path
  else:
    return base_path.joinpath(rsrc_path)

# DB = Database(Path(os.path.abspath("database.csv")))
DB = Database(fetch_resource(r"database/database.csv"))
userSession = EmployeeSelf(Employee(Permission_level=1))