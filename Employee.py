from __future__ import annotations
from datetime import datetime
from dataclasses import dataclass

from __future__ import annotations
# passlib import should be moved elsewhere
from passlib.context import CryptContext

#from Address import Address
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
    pay_type: str = INVALID_STR
    Permission_level: int = 0
    permitted_lock_on: bool = True
    route: str = INVALID_STR
    salary: str = INVALID_STR
    SS_num: int = -1
    Start_Date: datetime = INVALID_DATETIME
    state: str = INVALID_STR
    Title: str = INVALID_STR
    zip: str = INVALID_STR

    def isCorrectLogin(self, textPassword: str, context: CryptContext):
        return context.verify(textPassword, self.hashed_password)
