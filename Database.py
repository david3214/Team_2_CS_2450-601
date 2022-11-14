from datetime import datetime
from xmlrpc.client import Boolean
from Employee import INVALID_DATETIME, INVALID_STR, Employee, PERMISSION_LEVELS, INVALID_PATH
from EmployeeContainer import EmployeeContainer, EmployeeAdmin, EmployeeOther, EmployeeSelf, adminFields
from pathlib import Path
import csv
from tkinter import messagebox

usrAcc = EmployeeSelf(Employee(**{"ID": 101, "Permission Level": 1}))

class Database:
    def __init__(self, initFPath: Path = INVALID_PATH) -> None:
        """_summary_

        Args:
            initFPath (Path, optional): _description_. Defaults to INVALID_PATH.
        """
        self.employeeList: list[Employee] = list()
        self.initFPath = initFPath
        if str(initFPath) == str(INVALID_PATH):
            return
        elif initFPath.is_file():
            with initFPath.open() as csvfile:
                csvReader = csv.DictReader(csvfile)
                for row in csvReader:
                    # if there are different fields from Employee class they are treated as the param **garbage
                    self.employeeList.append(Employee(**row))
        elif str(initFPath) != str(INVALID_PATH):
            print("not a filepath\n")

    # do we need to do any validity checks before adding?
    def addEmployee(self, **kwargs) -> Boolean:
        """_summary_

        Returns:
            Boolean: true if add success
        """
        if len(self.search(Employee_ID=kwargs["EmpID"])) > 0:
            return False
        emp = Employee(**kwargs)
        if emp.hashed_password == INVALID_STR and emp.Emp_ID != INVALID_STR:
            emp.setPwd(str(emp.Emp_ID))
        self.employeeList.append(emp)
        return True

    def search(self, Department: str = INVALID_STR, name: str=INVALID_STR, fName: str = INVALID_STR, lName: str = INVALID_STR, Employee_ID: str = INVALID_STR, Title: str = INVALID_STR, oPhone: str = INVALID_STR, StartDate: datetime = INVALID_DATETIME, EndDate: datetime = INVALID_DATETIME, Archived: bool = True) -> list:
        """_summary_

        Args:
            Department (str, optional): _description_. Defaults to INVALID_STR.
            fName (str, optional): _description_. Defaults to INVALID_STR.
            lName (str, optional): _description_. Defaults to INVALID_STR.
            Employee_ID (str, optional): _description_. Defaults to INVALID_STR.
            Title (str, optional): _description_. Defaults to INVALID_STR.
            oPhone (str, optional): _description_. Defaults to INVALID_STR.
            StartDate (datetime, optional): _description_. Defaults to INVALID_DATETIME.
            EndDate (datetime, optional): _description_. Defaults to INVALID_DATETIME.

        Returns:
            list: _description_
        """
        from config import userSession
        foundList = list()
        for emp in self.employeeList:
            emp = self.__employeeContainment(emp, userSession)
            valid: bool = True
            valid = valid and (Department == INVALID_STR or Department.lower() in emp.Dept.lower())
            valid = valid and (name == INVALID_STR or name.lower() in emp.Name.lower())
            valid = valid and (fName == INVALID_STR or fName.lower() in emp.getFName().lower())
            valid = valid and (lName == INVALID_STR or lName.lower() in emp.getLName().lower())
            valid = valid and (Employee_ID == INVALID_STR or Employee_ID == emp.EmpID)
            valid = valid and (Title == INVALID_STR or Title.lower() in emp.Title.lower())
            valid = valid and (oPhone == INVALID_STR or oPhone == emp.OfficePhone)
            valid = valid and (StartDate == INVALID_DATETIME or StartDate == emp.StartDate)
            valid = valid and (EndDate == INVALID_DATETIME or EndDate == emp.EndDate)
            valid = valid and (Archived or (not Archived and emp.Active))
            # if any of the statements after "valid and not" are True then valid will be False
            if valid:
                foundList.append(emp)
        foundList.sort(key = lambda x: x.Name)
        return foundList

    def importDB(self, importFPath: Path = INVALID_PATH) -> None:
        """_summary_

        Args:
            importFPath (Path, optional): _description_. Defaults to INVALID_PATH.
        """
        if importFPath.is_file():
            impList: list[Employee] = list()
            with importFPath.open() as csvfile:
                csvReader = csv.DictReader(csvfile)
                for row in csvReader:
                    # if there are different fields from Employee class they are treated as the param **garbage
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
            self.exportDB(self.initFPath, adminInfo=True,
                          showArchivedEmployees=True)
        elif importFPath != str(INVALID_PATH):
            print("not a filepath\n")

    def exportDB(self, exportPath: Path = INVALID_PATH, adminInfo: Boolean = False, showArchivedEmployees: Boolean = True) -> None:
        """_summary_

        Args:
            exportPath (Path, optional): _description_. Defaults to INVALID_PATH.
            adminInfo (Boolean, optional): _description_. Defaults to False.
            showArchivedEmployees (Boolean, optional): _description_. Defaults to True.
        """
        from config import userSession
        with open(exportPath, 'w', newline='') as csvfile:
            fieldnames = dir(EmployeeContainer)
            # Switched to this because it was getting hard to keep track of all the functions on the employee container
            badnames = [method for method in fieldnames if callable(
                getattr(EmployeeContainer, method))] + ['permissionList']
            badnames = badnames if adminInfo else adminFields + badnames
            fieldnames = list(
                filter(lambda x: x[:1] != "_" and x not in badnames, fieldnames))

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, restval='')
            writer.writeheader()
            for emp in self.employeeList:
                if adminInfo:
                    emp = self.__employeeContainment(emp, userSession)
                else:
                    emp = EmployeeOther(emp)

                if not showArchivedEmployees and not emp.Active:
                    continue
                out = dict([(k, emp.__getattribute__(k)) for k in fieldnames])
                writer.writerow(out)

    def __employeeContainment(self, targetEmployee: Employee, selfEmployee: EmployeeSelf):
        """takes employee and puts it in a container based on who the user is

        Args:
            targetEmployee (Employee): _description_
            selfEmployee (EmployeeSelf): _description_

        Returns:
            _type_: _description_
        """
        if PERMISSION_LEVELS[int(selfEmployee.PermissionLevel)] == 'admin':
            return EmployeeAdmin(targetEmployee)
        elif targetEmployee is selfEmployee._employee:
            return EmployeeSelf(targetEmployee)
        else:
            return EmployeeOther(targetEmployee)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def empCount(self):
        return len(self.employeeList)
