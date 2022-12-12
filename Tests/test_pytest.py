from Config.Database import Database
import Employee.Employee as EmployeeModule
from Employee.Employee import Employee
from Employee.EmployeeContainer import EmployeeContainer, EmployeeAdmin, EmployeeOther, EmployeeSelf
import pytest
from pathlib import Path
import filecmp
import copy
from tkinter import messagebox
from datetime import datetime
from Employee.Address import Address
from GUI.Components.Panels.GeneralInfo import GeneralInfo
from GUI.Screens.AddEmployee import AddEmployee
import tkinter as tk


@pytest.fixture(params=["Resources/database.csv", ])
def database(request):
    return Database(Path(request.param))


def genericVal(paramType: type):
    # don't use match case. it is awful
    if paramType == int:
        return 263547645
    elif paramType == str:
        return "bviojnvdfu jhvdfbnkj"
    elif paramType == datetime:
        return datetime.now()
    elif paramType == bool:
        return False
    else:
        raise TypeError


@pytest.fixture()
def empFullParamNorm():
    return dict([(k, genericVal(EmployeeModule.EMP_FIELDS[k]))for k in EmployeeModule.EMP_FIELDS])


def test_name_set():
    emp = Employee(name="bob")
    assert emp.name == "bob"
    empC = EmployeeAdmin(emp)
    assert empC.Name == "bob"
    empC.Name = "joe"
    assert emp.name == "joe" == empC.Name


def test_database_import_export(database: Database, tmp_path, monkeypatch):
    database.exportDB(tmp_path / "db1.csv", True)
    Database(database.initFPath).exportDB(tmp_path / "db2.csv", True)
    assert database == Database(database.initFPath)
    db: Database = copy.deepcopy(database)
    db.exportDB(tmp_path / "db3.csv", True)

    def usr_clicks_ovrwrt_yes(*args, **kwargs):
        return True
    monkeypatch.setattr(messagebox, "askyesno", usr_clicks_ovrwrt_yes)
    database.importDB(database.initFPath)
    assert db == database
    assert filecmp.cmp(tmp_path / "db1.csv", tmp_path / "db2.csv", False)
    assert filecmp.cmp(tmp_path / "db2.csv", tmp_path / "db3.csv", False)


def test_db_init_empty():
    dbFull = Database()
    assert dbFull.empCount() == 0


def test_database_import_export_full_norm(empFullParamNorm: dict, tmp_path, monkeypatch):
    dbFull = Database()
    assert dbFull.empCount() == 0
    dbFull.addEmployee(**empFullParamNorm)
    assert dbFull.empCount() == 1
    dbFull.exportDB(tmp_path/"norm1.csv", True)
    dbFull2 = Database(tmp_path/"norm1.csv")
    assert dbFull == dbFull2


def test_genericValFunc():
    assert genericVal(type(69)).__class__ is int
    assert genericVal(bool).__class__ is bool
    assert genericVal(datetime).__class__ is datetime
