import main
import Employee
import EmployeeContainer


def test_name_set():
    emp = Employee.Employee(name="bob")
    assert emp.name == "bob"
    empC = EmployeeContainer.EmployeeAdmin(emp)
    assert empC.Name == "bob"
    empC.Name = "joe"
    assert emp.name == "joe" == empC.Name
