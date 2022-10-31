from datetime import datetime

# passlib import should be moved elsewhere
from passlib.context import CryptContext

from Address import Address
from typing import Final

INVALID_STR: Final[str] = ""
INVALID_ADDRESS: Final[Address] = Address()
INVALID_DATETIME: Final[datetime] = datetime.min


class Employee:

    def __init__(self, name: str = INVALID_STR, address: Address = INVALID_ADDRESS, office_phone: str = INVALID_STR, Emp_ID: str = INVALID_STR, D_O_B: datetime = INVALID_DATETIME, SS_num: int = -1, Start_Date: datetime = INVALID_DATETIME, End_Date: datetime = INVALID_DATETIME, Permission_level: int = 0, Title: str = INVALID_STR, Dept: str = INVALID_STR, Office_email: str = INVALID_STR, hashed_password: str = INVALID_STR, active: bool = False, permitted_lock_on: bool = True, home_email: str = INVALID_STR, home_phone: str = INVALID_STR, pay_type: str = INVALID_STR, bank_info: str = INVALID_STR, route: str = INVALID_STR, salary: str = INVALID_STR, hourly: str = INVALID_STR, commission: str = INVALID_STR, **garbage) -> None:
        """_summary_

        Args:
            name (str): _description_
            address (Address): _description_
            office_phone (str): _description_
            Emp_ID (str): _description_
            D_O_B (datetime.date): _description_
            SS_num (int): _description_
            Start_Date (datetime.date): _description_
            End_Date (datetime.date): _description_
            Permission_level (int): _description_
            Title (str): _description_
            Dept (str): _description_
            Office_email (str): _description_
            hashed_password (str): _description_
            active (bool): _description_
            permitted_lock_on (bool): _description_
            home_email (str): _description_
            home_phone (str): _description_
            pay_type (str): _description_
            bank_info (str): _description_
            route (str): _description_
            salary (str): _description_
            hourly (str): _description_
            commission (str): _description_
        """
        self.name = name
        self.address = address
        self.office_phone = office_phone
        self.Emp_ID = Emp_ID
        self.D_O_B = D_O_B
        self.SS_num = SS_num
        self.Start_Date = Start_Date
        self.End_Date = End_Date
        self.Permission_level = Permission_level
        self.Title = Title
        self.Dept = Dept
        self.Office_email = Office_email
        self.hashed_password = hashed_password
        self.active = active
        self.permitted_lock_on = permitted_lock_on
        self.home_email = home_email
        self.home_phone = home_phone
        self.pay_type = pay_type
        self.bank_info = bank_info
        self.route = route
        self.salary = salary
        self.hourly = hourly
        self.commission = commission

    def isCorrectLogin(self, textPassword: str, context: CryptContext):
        return context.verify(textPassword, self.hashed_password)
