from datetime import datetime
from xmlrpc.client import Boolean
from Employee import INVALID_DATETIME, INVALID_STR, Employee
from EmployeeContainer import EmployeeContainer, EmployeeAdmin, EmployeeOther, EmployeeSelf
from pathlib import Path
import csv
from tkinter import messagebox


class Database:
    def __init__(self, initFPath: Path = Path("")) -> None:
        self.employeeList: list[Employee] = list()
        if initFPath == "":
            return
        elif initFPath.is_file():
            with initFPath.open() as csvfile:
                csvReader = csv.DictReader(csvfile)
                for row in csvReader:
                    # test what happens if there are different fields from Employee class
                    self.employeeList.append(Employee(**row))
        elif initFPath != "":
            print("not a filepath\n")

    # do we need to do any validity checks before adding?
    def addEmployee(self, **kwargs) -> Boolean:
        if len(self.search(Employee_ID=kwargs["Emp_ID"])) > 0:
            return False
        self.employeeList.append(Employee(**kwargs))
        return True

    def search(self, Department: str = INVALID_STR, fName: str = INVALID_STR, lName: str = INVALID_STR, Employee_ID: str = INVALID_STR, Title: str = INVALID_STR, oPhone: str = INVALID_STR, StartDate: datetime = INVALID_DATETIME, EndDate: datetime = INVALID_DATETIME) -> list:
        foundList = list()
        for emp in self.employeeList:
            # when user sessions are implemented, this needs to be replaced with a proper switch
            emp = EmployeeOther(emp)
            if (Department == INVALID_STR or Department == emp.getDept()) and (fName == INVALID_STR or fName == emp.getFName()) and (lName == INVALID_STR or lName == emp.getLName()) and (Employee_ID == INVALID_STR or Employee_ID == emp.getEmpID()) and (Title == INVALID_STR or Title == emp.getTitle()) and (oPhone == INVALID_STR or oPhone == emp.getOfficePhone()) and (StartDate == INVALID_DATETIME or StartDate == emp.getStartDate()) and (EndDate == INVALID_DATETIME or EndDate == emp.getEndDate()):
                foundList.append(emp)
        return foundList

    def importDB(self, importFPath: Path = Path("")) -> None:
        if importFPath.is_file():
            impList: list[Employee] = list()
            with importFPath.open() as csvfile:
                csvReader = csv.DictReader(csvfile)
                for row in csvReader:
                    # test what happens if there are different fields from Employee class
                    impList.append(Employee(**row))
            for emp in impList:
                dupeList: list[Employee] = list()
                for employee in self.employeeList:
                    if emp.Emp_ID == employee.Emp_ID:
                        dupeList.append(employee)
                if len(dupeList) == 0:
                    self.employeeList.append(emp)
                else:
                    overwrite = messagebox.askyesno(
                        "Overwrite", "Employee with ID " + emp.Emp_ID + " already exists. Do you wish to overwrite it?")
                    if overwrite:
                        self.employeeList.remove(dupeList[0])
                        self.employeeList.append(emp)

        elif importFPath != "":
            print("not a filepath\n")
