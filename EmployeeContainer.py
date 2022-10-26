from xmlrpc.client import Boolean
import Employee
from Address import Address
from datetime import datetime


class EmployeeContainer():
    def __init__(self, employee: Employee.Employee) -> None:
        self._employee = employee

    def getName(self):
        return ""

    def setName(self, val: str) -> Boolean:
        return False

    def getAddress(self):
        return Address()

    def setAddress(self, val: Address) -> Boolean:
        return False

    def getOfficePhone(self):
        return ""

    def setOfficePhone(self, val: str) -> Boolean:
        return False

    def getEmpID(self):
        return ""

    def setEmpID(self, val: str) -> Boolean:
        return False

    def getDOB(self):
        return datetime.min

    def setDOB(self, val: datetime) -> Boolean:
        return False

    def getSSNum(self):
        return -2

    def setSSNum(self, val: int) -> Boolean:
        return False

    def getStartDate(self):
        return datetime.min

    def setStartDate(self, val: datetime) -> Boolean:
        return False

    def getEndDate(self):
        return datetime.min

    def setEndDate(self, val: datetime) -> Boolean:
        return False

    def getPermissionLevel(self):
        return -1

    def setPermissionLevel(self, val: int) -> Boolean:
        return False

    def getTitle(self):
        return ""

    def setTitle(self, val: str) -> Boolean:
        return False

    def getDept(self):
        return ""

    def setDept(self, val: str) -> Boolean:
        return False

    def getOfficeEmail(self):
        return ""

    def setOfficeEmail(self, val: str) -> Boolean:
        return False

    def getActive(self):
        return self._employee.active

    def setActive(self, val: Boolean) -> Boolean:
        return False

    def getPermittedLockOn(self):
        return self._employee.permitted_lock_on

    def setPermittedLockOn(self, val: Boolean) -> Boolean:
        return False

    def getHomePhone(self):
        return ""

    def setHomePhone(self, val: str) -> Boolean:
        return False

    def getHomeEmail(self):
        return ""

    def setHomeEmail(self, val: str) -> Boolean:
        return False

    def getPayType(self):
        return ""

    def setPayType(self, val: str) -> Boolean:
        return False

    def getBankInfo(self):
        return ""

    def setBankInfo(self, val: str) -> Boolean:
        return False

    def getRoute(self):
        return ""

    def setRoute(self, val: str) -> Boolean:
        return False

    def getSalary(self):
        return ""

    def setSalary(self, val: str) -> Boolean:
        return False

    def getHourly(self):
        return ""

    def setHourly(self, val: str) -> Boolean:
        return False

    def getCommission(self):
        return ""

    def setCommission(self, val: str) -> Boolean:
        return False


class EmployeeOther(EmployeeContainer):
    def getName(self):
        return super()._employee.name

    def getOfficePhone(self):
        return super()._employee.office_phone

    def getEmpID(self):
        return super()._employee.Emp_ID

    def getStartDate(self):
        return super()._employee.Start_Date

    def getEndDate(self):
        return super()._employee.End_Date

    def getTitle(self):
        return super()._employee.Title

    def getOfficeEmail(self):
        return super()._employee.Office_email

    def getAddress(self):
        if super().getPermittedLockOn:
            return super().getAddress()
        return super()._employee.address

    def getHomeEmail(self):
        if super().getPermittedLockOn:
            return super().getHomeEmail()
        return super()._employee.home_email

    def getHomePhone(self):
        if super().getPermittedLockOn:
            return super().getHomePhone()
        return super()._employee.home_phone


class EmployeeSelf(EmployeeOther):
    def getAddress(self):
        return super()._employee.address

    def getHomeEmail(self):
        return super()._employee.home_email

    def getHomePhone(self):
        return super()._employee.home_phone

    def getEmpID(self):
        return super()._employee.Emp_ID

    def getDOB(self):
        return super()._employee.D_O_B

    def getSSNum(self):
        return super()._employee.SS_num

    def getPermissionLevel(self):
        return super()._employee.Permission_level

    def getPayType(self):
        return super()._employee.pay_type

    def getBankInfo(self):
        return super()._employee.bank_info

    def getRoute(self):
        return super()._employee.route

    def getSalary(self):
        return super()._employee.salary

    def getHourly(self):
        return super()._employee.hourly

    def getCommission(self):
        return super()._employee.commission

    def setName(self, val: str) -> Boolean:
        super()._employee.name = val
        return True

    def setAddress(self, val: Address) -> Boolean:
        super()._employee.address = val
        return True

    def setOfficePhone(self, val: str) -> Boolean:
        super()._employee.office_phone = val
        return True

    def setPermittedLockOn(self, val: Boolean) -> Boolean:
        super()._employee.permitted_lock_on = val
        return True


class EmployeeAdmin(EmployeeSelf):

    def setEmpID(self, val: str) -> Boolean:
        super()._employee.Emp_ID = val
        return True

    def setDOB(self, val: datetime) -> Boolean:
        super()._employee.D_O_B = val
        return True

    def setSSNum(self, val: int) -> Boolean:
        super()._employee.SS_num = val
        return True

    def setStartDate(self, val: datetime) -> Boolean:
        super()._employee.Start_Date = val
        return True

    def setEndDate(self, val: datetime) -> Boolean:
        super()._employee.End_Date = val
        return True

    def setPermissionLevel(self, val: int) -> Boolean:
        super()._employee.Permission_level = val
        return True

    def setTitle(self, val: str) -> Boolean:
        super()._employee.Title = val
        return True

    def setDept(self, val: str) -> Boolean:
        super()._employee.Dept = val
        return True

    def setOfficeEmail(self, val: str) -> Boolean:
        super()._employee.Office_email = val
        return True

    def setActive(self, val: Boolean) -> Boolean:
        super()._employee.active = val
        return True

    def setHomePhone(self, val: str) -> Boolean:
        super()._employee.home_phone = val
        return True

    def setHomeEmail(self, val: str) -> Boolean:
        super()._employee.home_email = val
        return True

    def setPayType(self, val: str) -> Boolean:
        super()._employee.pay_type = val
        return True

    def setBankInfo(self, val: str) -> Boolean:
        super()._employee.bank_info = val
        return True

    def setRoute(self, val: str) -> Boolean:
        super()._employee.route = val
        return True

    def setSalary(self, val: str) -> Boolean:
        super()._employee.salary = val
        return True

    def setHourly(self, val: str) -> Boolean:
        super()._employee.hourly = val
        return True

    def setCommission(self, val: str) -> Boolean:
        super()._employee.commission = val
        return True
