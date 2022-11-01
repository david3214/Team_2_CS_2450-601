from pickle import TRUE
from xmlrpc.client import Boolean
from Employee import INVALID_ADDRESS, INVALID_DATETIME, INVALID_STR, Employee
from Address import Address
from datetime import datetime
from types import MappingProxyType


class EmployeeContainer():
    def __init__(self, employee: Employee) -> None:
        self._employee = employee

    # this is a read only dict, aand can be interacted with using any method that would work on a dict, except writing to it
    # each key corresponds to an employee variable. the first bool of the value is whether it can be read, the second is if it can be set
    # the permitted lock allows the variables it governs to be read regardless of permissionList
    permissionList = MappingProxyType({'name': {False, False}, 'address': {False, False}, 'office_phone': {False, False}, 'Emp_ID': {False, False}, 'D_O_B': {False, False}, 'SS_num': {False, False}, 'Start_Date': {False, False}, 'End_Date': {False, False}, 'Permission_level': {False, False}, 'Title': {False, False}, 'Dept': {False, False}, 'Office_email': {
                                      False, False}, 'hashed_password': {False, False}, 'active': {False, False}, 'permitted_lock_on': {False, False}, 'home_email': {False, False}, 'home_phone': {False, False}, 'pay_type': {False, False}, 'bank_info': {False, False}, 'route': {False, False}, 'salary': {False, False}, 'hourly': {False, False}, 'commission': {False, False}})

    def getFName(self):
        name = self.getName()
        if name == INVALID_STR:
            return name
        else:
            return name.split()[0]

    def getLName(self):
        name = self.getName()
        if name == INVALID_STR:
            return name
        else:
            if len(name.split()) >= 2:
                return name.split()[1]
            else:
                return INVALID_STR

    def getName(self):
        if self.permissionList['name'][0]:
            return self._employee.name
        return INVALID_STR

    def getOfficePhone(self):
        if self.permissionList['office_phone'][0]:
            return self._employee.office_phone
        return INVALID_STR

    def getEmpID(self):
        if self.permissionList['Emp_ID'][0]:
            return self._employee.Emp_ID
        return INVALID_STR

    def getStartDate(self):
        if self.permissionList['Start_Date'][0]:
            return self._employee.Start_Date
        return INVALID_DATETIME

    def getEndDate(self):
        if self.permissionList['End_Date'][0]:
            return self._employee.End_Date
        return INVALID_DATETIME

    def getTitle(self):
        if self.permissionList['Title'][0]:
            return self._employee.Title
        return INVALID_STR

    def getOfficeEmail(self):
        if self.permissionList['Office_email'][0]:
            return self._employee.Office_email
        return INVALID_STR

    def getAddress(self):
        if self.getPermittedLockOn:
            if self.permissionList['address'][0]:
                return self._employee.address
            else:
                return INVALID_ADDRESS
        return self._employee.home_email

    def getHomeEmail(self):
        if self.getPermittedLockOn:
            if self.permissionList['home_email'][0]:
                return self._employee.home_email
            else:
                return INVALID_STR
        return self._employee.home_email

    def getHomePhone(self):
        if self.getPermittedLockOn:
            if self.permissionList['home_phone'][0]:
                return self._employee.home_phone
            else:
                return INVALID_STR
        return self._employee.home_phone

    def getEmpID(self):
        if self.permissionList['Emp_ID'][0]:
            return self._employee.Emp_ID
        return INVALID_STR

    def getDOB(self):
        if self.permissionList['D_O_B'][0]:
            return self._employee.D_O_B
        return INVALID_DATETIME

    def getSSNum(self):
        if self.permissionList['SS_num'][0]:
            return self._employee.SS_num
        return INVALID_STR

    def getPermissionLevel(self):
        if self.permissionList['Permission_level'][0]:
            return self._employee.Permission_level
        return INVALID_STR

    def getPayType(self):
        if self.permissionList['pay_type'][0]:
            return self._employee.pay_type
        return INVALID_STR

    def getBankInfo(self):
        if self.permissionList['bank_info'][0]:
            return self._employee.bank_info
        return INVALID_STR

    def getRoute(self):
        if self.permissionList['route'][0]:
            return self._employee.route
        return INVALID_STR

    def getSalary(self):
        if self.permissionList['salary'][0]:
            return self._employee.salary
        return INVALID_STR

    def getHourly(self):
        if self.permissionList['hourly'][0]:
            return self._employee.hourly
        return INVALID_STR

    def getCommission(self):
        if self.permissionList['commission'][0]:
            return self._employee.commission
        return INVALID_STR

    def setName(self, val: str) -> Boolean:
        if self.permissionList['name'][1]:
            self._employee.name = val
            return True
        return False

    def setAddress(self, val: Address) -> Boolean:
        if self.permissionList['address'][1]:
            self._employee.address = val
            return True
        return False

    def setOfficePhone(self, val: str) -> Boolean:
        if self.permissionList['office_phone'][1]:
            self._employee.office_phone = val
            return True
        return False

    def setPermittedLockOn(self, val: Boolean) -> Boolean:
        if self.permissionList['permitted_lock_on'][1]:
            self._employee.permitted_lock_on = val
            return True
        return False

    def setEmpID(self, val: str) -> Boolean:
        if self.permissionList['Emp_ID'][1]:
            self._employee.Emp_ID = val
            return True
        return False

    def setDOB(self, val: datetime) -> Boolean:
        if self.permissionList['D_O_B'][1]:
            self._employee.D_O_B = val
            return True
        return False

    def setSSNum(self, val: int) -> Boolean:
        if self.permissionList['SS_num'][1]:
            self._employee.SS_num = val
            return True
        return False

    def setStartDate(self, val: datetime) -> Boolean:
        if self.permissionList['Start_Date'][1]:
            self._employee.Start_Date = val
            return True
        return False

    def setEndDate(self, val: datetime) -> Boolean:
        if self.permissionList['End_Date'][1]:
            self._employee.End_Date = val
            return True
        return False

    def setPermissionLevel(self, val: int) -> Boolean:
        if self.permissionList['Permission_level'][1]:
            self._employee.Permission_level = val
            return True
        return False

    def setTitle(self, val: str) -> Boolean:
        if self.permissionList['Title'][1]:
            self._employee.Title = val
            return True
        return False

    def setDept(self, val: str) -> Boolean:
        if self.permissionList['Dept'][1]:
            self._employee.Dept = val
            return True
        return False

    def setOfficeEmail(self, val: str) -> Boolean:
        if self.permissionList['Office_email'][1]:
            self._employee.Office_email = val
            return True
        return False

    def setActive(self, val: Boolean) -> Boolean:
        if self.permissionList['active'][1]:
            self._employee.active = val
            return True
        return False

    def setHomePhone(self, val: str) -> Boolean:
        if self.permissionList['home_phone'][1]:
            self._employee.home_phone = val
            return True
        return False

    def setHomeEmail(self, val: str) -> Boolean:
        if self.permissionList['home_email'][1]:
            self._employee.home_email = val
            return True
        return False

    def setPayType(self, val: str) -> Boolean:
        if self.permissionList['pay_type'][1]:
            self._employee.pay_type = val
            return True
        return False

    def setBankInfo(self, val: str) -> Boolean:
        if self.permissionList['bank_info'][1]:
            self._employee.bank_info = val
            return True
        return False

    def setRoute(self, val: str) -> Boolean:
        if self.permissionList['route'][1]:
            self._employee.route = val
            return True
        return False

    def setSalary(self, val: str) -> Boolean:
        if self.permissionList['salary'][1]:
            self._employee.salary = val
            return True
        return False

    def setHourly(self, val: str) -> Boolean:
        if self.permissionList['hourly'][1]:
            self._employee.hourly = val
            return True
        return False

    def setCommission(self, val: str) -> Boolean:
        if self.permissionList['commission'][1]:
            self._employee.commission = val
            return True
        return False
# add setPassword() here when method off sharing CryptContext is decided


class EmployeeOther(EmployeeContainer):
    permissionList = MappingProxyType({'name': {True, False}, 'address': {False, False}, 'office_phone': {True, False}, 'Emp_ID': {True, False}, 'D_O_B': {False, False}, 'SS_num': {False, False}, 'Start_Date': {True, False}, 'End_Date': {True, False}, 'Permission_level': {False, False}, 'Title': {True, False}, 'Dept': {True, False}, 'Office_email': {
                                      True, False}, 'hashed_password': {False, False}, 'active': {True, False}, 'permitted_lock_on': {True, False}, 'home_email': {False, False}, 'home_phone': {False, False}, 'pay_type': {False, False}, 'bank_info': {False, False}, 'route': {False, False}, 'salary': {False, False}, 'hourly': {False, False}, 'commission': {False, False}})


class EmployeeSelf(EmployeeContainer):
    permissionList = MappingProxyType({'name': {True, False}, 'address': {True, False}, 'office_phone': {True, False}, 'Emp_ID': {True, False}, 'D_O_B': {True, False}, 'SS_num': {True, False}, 'Start_Date': {True, False}, 'End_Date': {True, False}, 'Permission_level': {True, False}, 'Title': {True, False}, 'Dept': {True, False}, 'Office_email': {
                                      True, False}, 'hashed_password': {True, False}, 'active': {True, False}, 'permitted_lock_on': {True, False}, 'home_email': {True, False}, 'home_phone': {True, False}, 'pay_type': {True, False}, 'bank_info': {True, False}, 'route': {True, False}, 'salary': {True, False}, 'hourly': {True, False}, 'commission': {True, False}})


class EmployeeAdmin(EmployeeContainer):
    permissionList = MappingProxyType({'name': {True, True}, 'address': {True, True}, 'office_phone': {True, True}, 'Emp_ID': {True, True}, 'D_O_B': {True, True}, 'SS_num': {True, True}, 'Start_Date': {True, True}, 'End_Date': {True, True}, 'Permission_level': {True, True}, 'Title': {True, True}, 'Dept': {True, True}, 'Office_email': {
                                      True, True}, 'hashed_password': {True, True}, 'active': {True, True}, 'permitted_lock_on': {True, True}, 'home_email': {True, True}, 'home_phone': {True, True}, 'pay_type': {True, True}, 'bank_info': {True, True}, 'route': {True, True}, 'salary': {True, True}, 'hourly': {True, True}, 'commission': {True, True}})
