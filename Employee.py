from datetime import datetime

# passlib import should be moved elsewhere
from passlib.context import CryptContext

#from Address import Address
from typing import Final

INVALID_STR: Final[str] = ""
#INVALID_ADDRESS: Final[Address] = Address()
INVALID_DATETIME: Final[datetime] = datetime.min

PERMISSION_LEVELS: Final[dict] = dict([(1, 'admin'), (0, 'user')])


class Employee:

    def __init__(self, name: str = INVALID_STR, address: str = "", apartment: str = "", city: str = "", state: str = "", country: str = "", zip: str = "", office_phone: str = INVALID_STR, Emp_ID: str = INVALID_STR, D_O_B: datetime = INVALID_DATETIME, SS_num: int = -1, Start_Date: datetime = INVALID_DATETIME, End_Date: datetime = INVALID_DATETIME, Permission_level: int = 0, Title: str = INVALID_STR, Dept: str = INVALID_STR, Office_email: str = INVALID_STR, hashed_password: str = INVALID_STR, active: bool = False, permitted_lock_on: bool = True, home_email: str = INVALID_STR, home_phone: str = INVALID_STR, pay_type: str = INVALID_STR, bank_info: str = INVALID_STR, route: str = INVALID_STR, salary: str = INVALID_STR, hourly: str = INVALID_STR, commission: str = INVALID_STR, **garbage) -> None:
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
        self.active = active
        self.address = address
        self.address = address
        self.apartment = apartment
        self.bank_info = bank_info
        self.city = city
        self.commission = commission
        self.country = country
        self.D_O_B = D_O_B
        self.Dept = Dept
        self.Emp_ID = Emp_ID
        self.End_Date = End_Date

        self.home_email = home_email
        self.home_phone = home_phone
        self.hourly = hourly
        self.name = name
        self.Office_email = Office_email
        self.office_phone = office_phone
        self.pay_type = pay_type
        self.Permission_level = Permission_level
        self.permitted_lock_on = permitted_lock_on
        self.route = route
        self.salary = salary
        self.SS_num = SS_num
        self.Start_Date = Start_Date
        self.state = state
        self.Title = Title
        self.zip = zip
        self.hashed_password = hashed_password
        # garbage handler, should switch to a ui based method
        if garbage:
            print("Employee recieved bad data:\n")
            for key in garbage:
                print(key+","+garbage[key]+"\n")

    def isCorrectLogin(self, textPassword: str, context: CryptContext):
        return context.verify(textPassword, self.hashed_password)
