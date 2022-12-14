from pickle import TRUE
from xmlrpc.client import Boolean
from Employee.Employee import INVALID_STR, INVALID_DATETIME, INVALID_STR, Employee
#from Address import Address
from datetime import datetime
from types import MappingProxyType
import typing
adminFields = ['Address', 'DOB', 'Password', 'HomeEmail', 'HomePhone', 'SSNum',
               'PayMethod', 'BankInfo', 'Route', 'Salary', 'Hourly', 'PermissionLevel', 'Commission']


class EmployeeContainer():
    def __init__(self, employee: Employee) -> None:
        self._employee: Employee = employee

    # this is a read only dict, and can be interacted with using any method that would work on a dict, except writing to it
    # each key corresponds to an employee variable. the first bool of the value is whether it can be read, the second is if it can be set
    # the permitted lock allows the variables it governs to be read regardless of permissionList
    permissionList = MappingProxyType({'name': [False, False], 'address': [False, False], 'apartment': [False, False], 'city': [False, False], 'state': [False, False], 'country': [False, False], 'zip': [False, False], 'office_phone': [False, False], 'Emp_ID': [False, False], 'D_O_B': [False, False], 'SS_num': [False, False], 'Start_Date': [False, False], 'End_Date': [False, False], 'Permission_level': [False, False], 'Title': [False, False], 'Dept': [False, False], 'Office_email': [
        False, False],  'hashed_password': [False, False], 'active': [False, False], 'permitted_lock_on': [False, False], 'home_email': [False, False], 'home_phone': [False, False], 'pay_method': [False, False], 'bank_info': [False, False], 'route': [False, False], 'salary': [False, False], 'hourly': [False, False], 'commission': [False, False]})

    def ChangeEmployee(self, employee: Employee) -> None:
        self._employee = employee

    def isCorrectLogin(self, testPassword):
        return self._employee.isCorrectLogin(testPassword)

    def getFName(self):
        name = self.Name
        if name == INVALID_STR:
            return name
        else:
            return name.split()[0]

    def getLName(self):
        name = self.Name
        if name == INVALID_STR:
            return name
        else:
            if len(name.split()) >= 2:
                return name.split()[-1]
            else:
                return INVALID_STR

    @property
    def Name(self):
        if self.permissionList['name'][0]:
            return self._employee.name
        return INVALID_STR

    @property
    def OfficePhone(self):
        if self.permissionList['office_phone'][0]:
            return self._employee.office_phone
        return INVALID_STR

    @property
    def EmpID(self):
        if self.permissionList['Emp_ID'][0]:
            return self._employee.Emp_ID
        return INVALID_STR

    @property
    def Password(self):
        if self.permissionList['hashed_password'][0]:
            return self._employee.hashed_password
        return INVALID_STR

    @Password.setter
    def Password(self, val: str):
        if self.permissionList['hashed_password'][1]:
            self._employee.setPwd(val)
            return True
        return False

    @property
    def PermittedLockOn(self):
        if self.permissionList['permitted_lock_on'][0]:
            return self._employee.permitted_lock_on
        return INVALID_STR

    @property
    def StartDate(self):
        if self.permissionList['Start_Date'][0]:
            return self._employee.Start_Date
        return INVALID_DATETIME

    @property
    def EndDate(self):
        if self.permissionList['End_Date'][0]:
            return self._employee.End_Date
        return INVALID_DATETIME

    @property
    def Title(self):
        if self.permissionList['Title'][0]:
            return self._employee.Title
        return INVALID_STR

    @property
    def Dept(self):
        if self.permissionList['Dept'][0]:
            return self._employee.Dept
        return INVALID_STR

    @property
    def OfficeEmail(self):
        if self.permissionList['Office_email'][0]:
            return self._employee.Office_email
        return INVALID_STR

    @property
    def Active(self):
        if self.permissionList['active'][0]:
            return self._employee.active
        raise Exception

    @property
    def Address(self):
        if self.PermittedLockOn:
            if self.permissionList['address'][0]:
                return self._employee.address
            else:
                return INVALID_STR
        return self._employee.address

    @property
    def Apartment(self):
        if self.PermittedLockOn:
            if self.permissionList['apartment'][0]:
                return self._employee.apartment
            else:
                return INVALID_STR
        return self._employee.apartment

    @property
    def City(self):
        if self.PermittedLockOn:
            if self.permissionList['city'][0]:
                return self._employee.city
            else:
                return INVALID_STR
        return self._employee.city

    @property
    def State(self):
        if self.PermittedLockOn:
            if self.permissionList['state'][0]:
                return self._employee.state
            else:
                return INVALID_STR
        return self._employee.state

    @property
    def Country(self):
        if self.PermittedLockOn:
            if self.permissionList['country'][0]:
                return self._employee.country
            else:
                return INVALID_STR
        return self._employee.country

    @property
    def Zip(self):
        if self.PermittedLockOn:
            if self.permissionList['zip'][0]:
                return self._employee.zip
            else:
                return INVALID_STR
        return self._employee.zip

    @property
    def HomeEmail(self):
        if self.PermittedLockOn:
            if self.permissionList['home_email'][0]:
                return self._employee.home_email
            else:
                return INVALID_STR
        return self._employee.home_email

    @property
    def HomePhone(self):
        if self.PermittedLockOn:
            if self.permissionList['home_phone'][0]:
                return self._employee.home_phone
            else:
                return INVALID_STR
        return self._employee.home_phone

    @property
    def DOB(self):
        if self.permissionList['D_O_B'][0]:
            return self._employee.D_O_B
        return INVALID_DATETIME

    @property
    def SSNum(self):
        if self.permissionList['SS_num'][0]:
            return self._employee.SS_num
        return -1

    @property
    def PermissionLevel(self):
        if self.permissionList['Permission_level'][0]:
            return self._employee.Permission_level
        return -1

    @property
    def PayMethod(self):
        if self.permissionList['pay_method'][0]:
            return self._employee.pay_method
        return INVALID_STR

    @property
    def BankInfo(self):
        if self.permissionList['bank_info'][0]:
            return self._employee.bank_info
        return INVALID_STR

    @property
    def Route(self):
        if self.permissionList['route'][0]:
            return self._employee.route
        return INVALID_STR

    @property
    def Salary(self):
        if self.permissionList['salary'][0]:
            return self._employee.salary
        return INVALID_STR

    @property
    def Hourly(self):
        if self.permissionList['hourly'][0]:
            return self._employee.hourly
        return INVALID_STR

    @property
    def Commission(self):
        if self.permissionList['commission'][0]:
            return self._employee.commission
        return INVALID_STR

    @Name.setter
    def Name(self, val: str):
        if self.permissionList['name'][1]:
            self._employee.set('name', val)
            return True
        return False

    @Address.setter
    def Address(self, val: str):
        if self.permissionList['address'][1]:
            self._employee.set('address', val)
            return True
        return False

    @Apartment.setter
    def Apartment(self, val: str):
        if self.permissionList['apartment'][1]:
            self._employee.set('apartment', val)
            return True
        return False

    @City.setter
    def City(self, val: str):
        if self.permissionList['city'][1]:
            self._employee.set('city', val)
            return True
        return False

    @State.setter
    def State(self, val: str):
        if self.permissionList['state'][1]:
            self._employee.set('state', val)
            return True
        return False

    @Country.setter
    def Country(self, val: str):
        if self.permissionList['country'][1]:
            self._employee.set('country', val)
            return True
        return False

    @Zip.setter
    def Zip(self, val: str):
        if self.permissionList['zip'][1]:
            self._employee.set('zip', val)
            return True
        return False

    @OfficePhone.setter
    def OfficePhone(self, val: str):
        if self.permissionList['office_phone'][1]:
            self._employee.set('office_phone', val)
            return True
        return False

    @PermittedLockOn.setter
    def PermittedLockOn(self, val: Boolean | str):
        if self.permissionList['permitted_lock_on'][1]:
            self._employee.set('permitted_lock_on', val)
            return True
        return False

    @EmpID.setter
    def EmpID(self, val: str):
        if self.permissionList['Emp_ID'][1]:
            self._employee.set('Emp_ID', val)
            return True
        return False

    @DOB.setter
    def DOB(self, val: datetime | str):
        if self.permissionList['D_O_B'][1]:
            self._employee.set('D_O_B', val)
            return True
        return False

    @SSNum.setter
    def SSNum(self, val: int | str):
        if self.permissionList['SS_num'][1]:
            self._employee.set('SS_num', val)
            return True
        return False

    @StartDate.setter
    def StartDate(self, val: datetime | str):
        if self.permissionList['Start_Date'][1]:
            self._employee.set('Start_Date', val)
            return True
        return False

    @EndDate.setter
    def EndDate(self, val: datetime | str):
        if self.permissionList['End_Date'][1]:
            self._employee.set('End_Date', val)
            return True
        return False

    @PermissionLevel.setter
    def PermissionLevel(self, val: int | str):
        if self.permissionList['Permission_level'][1]:
            self._employee.set('Permission_level', val)
            return True
        return False

    @Title.setter
    def Title(self, val: str):
        if self.permissionList['Title'][1]:
            self._employee.set('Title', val)
            return True
        return False

    @Dept.setter
    def Dept(self, val: str):
        if self.permissionList['Dept'][1]:
            self._employee.set('Dept', val)
            return True
        return False

    @OfficeEmail.setter
    def OfficeEmail(self, val: str):
        if self.permissionList['Office_email'][1]:
            self._employee.set('Office_email', val)
            return True
        return False

    @Active.setter
    def Active(self, val: Boolean | str):
        if self.permissionList['active'][1]:
            self._employee.set('active', val)
            return True
        return False

    @HomePhone.setter
    def HomePhone(self, val: str):
        if self.permissionList['home_phone'][1]:
            self._employee.set('home_phone', val)
            return True
        return False

    @HomeEmail.setter
    def HomeEmail(self, val: str):
        if self.permissionList['home_email'][1]:
            self._employee.set('home_email', val)
            return True
        return False

    @PayMethod.setter
    def PayMethod(self, val: str):
        if self.permissionList['pay_method'][1]:
            self._employee.set('pay_method', val)
            return True
        return False

    @BankInfo.setter
    def BankInfo(self, val: str):
        if self.permissionList['bank_info'][1]:
            self._employee.set('bank_info', val)
            return True
        return False

    @Route.setter
    def Route(self, val: str):
        if self.permissionList['route'][1]:
            self._employee.set('route', val)
            return True
        return False

    @Salary.setter
    def Salary(self, val: str):
        if self.permissionList['salary'][1]:
            self._employee.set('salary', val)
            return True
        return False

    @Hourly.setter
    def Hourly(self, val: str):
        if self.permissionList['hourly'][1]:
            self._employee.set('hourly', val)
            return True
        return False

    @Commission.setter
    def Commission(self, val: str):
        if self.permissionList['commission'][1]:
            self._employee.set('commission', val)
            return True
        return False


class EmployeeOther(EmployeeContainer):
    permissionList = MappingProxyType({'name': [True, False], 'address': [False, False], 'apartment': [False, False], 'city': [False, False], 'state': [False, False], 'country': [False, False], 'zip': [False, False], 'office_phone': [True, False], 'Emp_ID': [True, False], 'D_O_B': [False, False], 'SS_num': [False, False], 'Start_Date': [True, False], 'End_Date': [True, False], 'Permission_level': [False, False], 'Title': [True, False], 'Dept': [True, False], 'Office_email': [
        True, False], 'hashed_password': [False, False], 'active': [True, False], 'permitted_lock_on': [True, False], 'home_email': [False, False], 'home_phone': [False, False], 'pay_method': [False, False], 'bank_info': [False, False], 'route': [False, False], 'salary': [False, False], 'hourly': [False, False], 'commission': [False, False]})


class EmployeeSelf(EmployeeContainer):

    permissionList = MappingProxyType({'name': [True, True], 'address': [True, True], 'apartment': [True, True], 'city': [True, True], 'state': [True, True], 'country': [True, True], 'zip': [True, True], 'office_phone': [True, True], 'Emp_ID': [True, False], 'D_O_B': [True, False], 'SS_num': [True, False], 'Start_Date': [True, False], 'End_Date': [True, False], 'Permission_level': [True, False], 'Title': [True, False], 'Dept': [True, False], 'Office_email': [
        True, False], 'hashed_password': [True, True], 'active': [True, False], 'permitted_lock_on': [True, True], 'home_email': [True, True], 'home_phone': [True, True], 'pay_method': [True, False], 'bank_info': [True, False], 'route': [True, False], 'salary': [True, False], 'hourly': [True, False], 'commission': [True, False]})


class EmployeeAdmin(EmployeeContainer):
    permissionList = MappingProxyType({'name': [True, True], 'address': [True, True], 'apartment': [True, True], 'city': [True, True], 'state': [True, True], 'country': [True, True], 'zip': [True, True], 'office_phone': [True, True], 'Emp_ID': [True, True], 'D_O_B': [True, True], 'SS_num': [True, True], 'Start_Date': [True, True], 'End_Date': [True, True], 'Permission_level': [True, True], 'Title': [True, True], 'Dept': [True, True], 'Office_email': [
        True, True], 'hashed_password': [True, True], 'active': [True, True], 'permitted_lock_on': [True, True], 'home_email': [True, True], 'home_phone': [True, True], 'pay_method': [True, True], 'bank_info': [True, True], 'route': [True, True], 'salary': [True, True], 'hourly': [True, True], 'commission': [True, True]})
