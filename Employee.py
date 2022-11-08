from datetime import datetime

# passlib import should be moved elsewhere
from passlib.context import CryptContext

from Address import Address
from typing import Final

INVALID_STR: Final[str] = ""
INVALID_ADDRESS: Final[Address] = Address()
INVALID_DATETIME: Final[datetime] = datetime.min

PERMISSION_LEVELS: Final[dict] = dict([(1, 'admin'), (0, 'user')])

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=200
    )

class Employee:

    def __init__(self, **kwargs) -> None:
        """_summary_

        Args:
            name (str, optional): _description_. Defaults to INVALID_STR.
            address (Address, optional): _description_. Defaults to INVALID_ADDRESS.
            office_phone (str, optional): _description_. Defaults to INVALID_STR.
            Emp_ID (str, optional): _description_. Defaults to INVALID_STR.
            D_O_B (datetime, optional): _description_. Defaults to INVALID_DATETIME.
            SS_num (int, optional): _description_. Defaults to -1.
            Start_Date (datetime, optional): _description_. Defaults to INVALID_DATETIME.
            End_Date (datetime, optional): _description_. Defaults to INVALID_DATETIME.
            Permission_level (int, optional): _description_. Defaults to 0.
            Title (str, optional): _description_. Defaults to INVALID_STR.
            Dept (str, optional): _description_. Defaults to INVALID_STR.
            Office_email (str, optional): _description_. Defaults to INVALID_STR.
            hashed_password (str, optional): _description_. Defaults to INVALID_STR.
            active (bool, optional): _description_. Defaults to False.
            permitted_lock_on (bool, optional): _description_. Defaults to True.
            home_email (str, optional): _description_. Defaults to INVALID_STR.
            home_phone (str, optional): _description_. Defaults to INVALID_STR.
            pay_type (str, optional): _description_. Defaults to INVALID_STR.
            bank_info (str, optional): _description_. Defaults to INVALID_STR.
            route (str, optional): _description_. Defaults to INVALID_STR.
            salary (str, optional): _description_. Defaults to INVALID_STR.
            hourly (str, optional): _description_. Defaults to INVALID_STR.
            commission (str, optional): _description_. Defaults to INVALID_STR.
        """
        self.name = kwargs.get("Name", INVALID_STR)
        self.address = Address(**kwargs)
        self.office_phone = kwargs.get("OfficePhone", INVALID_STR)
        self.Emp_ID = kwargs.get("EmpID") if kwargs.get("ID", INVALID_STR) == INVALID_STR else kwargs.get("ID", INVALID_STR)
        self.D_O_B = kwargs.get("DOB", INVALID_DATETIME)
        self.SS_num = kwargs.get("SSN", -1)
        self.Start_Date = kwargs.get("StartDate", INVALID_DATETIME)
        self.End_Date = kwargs.get("EndDate", INVALID_DATETIME)
        self.Permission_level = kwargs.get("Permission Level", 0)
        self.Title = kwargs.get("Title", INVALID_STR)
        self.Dept = kwargs.get("Dept", INVALID_STR)
        self.Office_email = kwargs.get("Email", INVALID_STR)
        self.active = kwargs.get("Archived", True)
        self.permitted_lock_on = kwargs.get("Permitted", 0)
        self.home_email = kwargs.get("HomeEmail", INVALID_STR)
        self.home_phone = kwargs.get("HomePhone", INVALID_STR)
        self.pay_method = kwargs.get("PayMethod", 1)
        self.bank_info = kwargs.get("Account", INVALID_STR)
        self.route = kwargs.get("Route", INVALID_STR)
        self.salary = kwargs.get("Salary", INVALID_STR)
        self.hourly = kwargs.get("Hourly", INVALID_STR)
        self.commission = kwargs.get("Commission", INVALID_STR)
        self.hashed_password = kwargs.get("Hashed Password", INVALID_STR)
        if self.hashed_password == INVALID_STR and self.Emp_ID != INVALID_STR:
            self.hashed_password = pwd_context.hash(str(self.Emp_ID))

    def isCorrectLogin(self, textPassword: str):
        return pwd_context.verify(textPassword, self.hashed_password)
