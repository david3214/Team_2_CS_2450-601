
from __future__ import annotations
# passlib import should be moved elsewhere
from passlib.context import CryptContext
from datetime import datetime
from Address import Address
from typing import Final
from pathlib import Path
INVALID_STR: Final[str] = ""
INVALID_ADDRESS: Final[Address] = Address()
INVALID_DATETIME: Final[datetime] = datetime.min
INVALID_PATH: Final[Path] = Path(" ")
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
        self.name: str = kwargs.get("Name", INVALID_STR)
        self.address: Address = Address(**kwargs)
        self.office_phone: str = kwargs.get("OfficePhone", INVALID_STR)
        self.Emp_ID: str = kwargs.get("EmpID", INVALID_STR) if kwargs.get(
            "ID", INVALID_STR) == INVALID_STR else kwargs.get("ID", INVALID_STR)
        self.D_O_B: datetime = kwargs.get("DOB", INVALID_DATETIME)
        self.SS_num: int = kwargs.get("SSN", -1)
        self.Start_Date: datetime = kwargs.get("StartDate", INVALID_DATETIME)
        self.End_Date: datetime = kwargs.get("EndDate", INVALID_DATETIME)
        self.Permission_level: int = kwargs.get("Permission Level", 0)
        self.Title: str = kwargs.get("Title", INVALID_STR)
        self.Dept: str = kwargs.get("Dept", INVALID_STR)
        self.Office_email: str = kwargs.get("Email", INVALID_STR)
        self.active: bool = kwargs.get("Archived", True)
        self.permitted_lock_on: bool = kwargs.get("Permitted", True)
        self.home_email: str = kwargs.get("HomeEmail", INVALID_STR)
        self.home_phone: str = kwargs.get("HomePhone", INVALID_STR)
        self.pay_method: str = kwargs.get("PayMethod", 1)
        self.bank_info: str = kwargs.get("Account", INVALID_STR)
        self.route: str = kwargs.get("Route", INVALID_STR)
        self.salary: str = kwargs.get("Salary", INVALID_STR)
        self.hourly: str = kwargs.get("Hourly", INVALID_STR)
        self.commission: str = kwargs.get("Commission", INVALID_STR)
        self.hashed_password: str = kwargs.get("Password", INVALID_STR) if kwargs.get(
            "Hashed Password", INVALID_STR) == INVALID_STR else kwargs.get("Hashed Password", INVALID_STR)

    def isCorrectLogin(self, textPassword: str):
        return pwd_context.verify(textPassword, self.hashed_password)

    def setPwd(self, textPassword: str):
        self.hashed_password = pwd_context.hash(textPassword)

    def __eq__(self, other: Employee):
        return self.__dict__ == other.__dict__


EMP_FIELDS: Final[list[str]] = list(Employee().__dict__.keys())
