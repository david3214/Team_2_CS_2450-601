from __future__ import annotations
from datetime import datetime
from dataclasses import dataclass

# passlib import should be moved elsewhere
from passlib.context import CryptContext

from typing import Final
from pathlib import Path
INVALID_STR: Final[str] = ""
#INVALID_ADDRESS: Final[Address] = Address()
INVALID_DATETIME: Final[datetime] = datetime.min
INVALID_PATH: Final[Path] = Path(" ")
PERMISSION_LEVELS: Final[dict] = dict([(1, 'admin'), (0, 'user')])

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=200
)


@dataclass
class Employee:

    active: bool = False
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
    Permission_level: int = 0
    permitted_lock_on: bool = True
    route: str = INVALID_STR
    salary: str = INVALID_STR
    SS_num: int = -1
    Start_Date: datetime = INVALID_DATETIME
    state: str = INVALID_STR
    Title: str = INVALID_STR
    zip: str = INVALID_STR

    def isCorrectLogin(self, textPassword: str):
        return pwd_context.verify(textPassword, self.hashed_password)

    def setPwd(self, textPassword: str):
        self.hashed_password = pwd_context.hash(textPassword)

    def __eq__(self, other: Employee):
        return self.__dict__ == other.__dict__


EMP_FIELDS: Final[dict[str, type]] = dict(
    [(k, type(Employee().__dict__[k])) for k in Employee().__dict__.keys()])
