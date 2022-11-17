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
    if hasattr(sys, '_MEIPASS'):
        base_path = Path(getattr(sys, '_MEIPASS'))
        return base_path.joinpath(rsrc_path)
    else:
        # not running as exe, just return the unaltered path
        return Path(rsrc_path)


#if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
DB = Database(fetch_resource(r"database/database.csv"))
#else:
#DB = Database(Path(os.path.abspath("database.csv")))
userSession = EmployeeSelf(Employee(Permission_level=1))
