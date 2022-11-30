from __future__ import annotations
from datetime import datetime
import dataclasses
# passlib import should be moved elsewhere
from passlib.context import CryptContext
import typing
from typing import Final
from pathlib import Path
INVALID_STR: Final[str] = str("")
#INVALID_ADDRESS: Final[Address] = Address()
INVALID_DATETIME: Final[datetime] = datetime.min

INVALID_PATH: Final[Path] = Path(" ")
PERMISSION_LEVELS: Final[dict] = dict([(1, 'admin'), (0, 'user')])

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=200
)


@dataclasses.dataclass
class Employee:

    active: bool = bool(False)
    address: str = INVALID_STR
    apartment: str = INVALID_STR
    bank_info: str = INVALID_STR
    city: str = INVALID_STR
    commission: str = INVALID_STR
    country: str = INVALID_STR
    D_O_B: datetime = INVALID_DATETIME
    Dept: str = INVALID_STR
    Emp_ID: str = INVALID_STR
    End_Date: datetime = INVALID_DATETIME
    hashed_password: str = INVALID_STR
    home_email: str = INVALID_STR
    home_phone: str = INVALID_STR
    hourly: str = INVALID_STR
    name: str = INVALID_STR
    Office_email: str = INVALID_STR
    office_phone: str = INVALID_STR
    pay_method: str = INVALID_STR
    Permission_level: int = int(0)
    permitted_lock_on: bool = True
    route: str = INVALID_STR
    salary: str = INVALID_STR
    SS_num: int = -1
    Start_Date: datetime = INVALID_DATETIME
    state: str = INVALID_STR
    Title: str = INVALID_STR
    zip: str = INVALID_STR

    def __post_init__(self):
        self.strCleanup()

    def isCorrectLogin(self, textPassword: str):
        return pwd_context.verify(textPassword, self.hashed_password)

    def setPwd(self, textPassword: str):
        self.hashed_password = pwd_context.hash(textPassword)

    def __eq__(self, other: Employee):
        return self.__dict__ == other.__dict__

    def strCleanup(self):
        for field in dataclasses.fields(Employee):
            if type(self.__getattribute__(field.name)) == type(field.default):
                continue
            else:
                t = type(field.default)
                if t == bool:
                    val = self.__getattribute__(field.name) == 'True'
                elif t == datetime:
                    val = datetime.fromisoformat(self.__getattribute__(field.name))
                else:
                    val = t(self.__getattribute__(field.name))
                setattr(self, field.name, val)

        if self.hashed_password == '':
            self.setPwd(str(self.Emp_ID))


    def set(self,name:str,val):
        if type(val) == EMP_FIELDS[name]:
            setattr(self,name,val)
        else:
            t = EMP_FIELDS[name]
            if t == bool:
                setattr(self,name,val == 'True')
            elif t == datetime:
                setattr(self,name, datetime.fromisoformat(val))
            else:
                setattr(self,name, t(val))


EMP_FIELDS: Final[dict[str, type]] = dict([(k.name, type(k.default)) for k in dataclasses.fields(Employee)])

