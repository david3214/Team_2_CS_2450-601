import os
from abc import ABC, abstractmethod
from functools import reduce


class Employee(object):
    """Represents an individual employee"""

    def __init__(self, eid, name, addr, city, st, code, clss, meth, slry, hrly, comm, rout, acct):
        """Creates an Employee object from provided information"""

        self.emp_id = eid
        self.name = name
        self.address = addr
        self.city = city
        self.state = st
        self.zipcode = code
        self.classification = clss
        self.pay_method = meth

        self.hourly = hrly
        self.salary = slry
        self.commission = comm
        self.rout_num = rout
        self.acct_num = acct

    def classify(self):
        """Assigns Employees' classifications based on instance variable"""

        if self.classification == '1':
            self.make_hourly(float(self.hourly))
        elif self.classification == '2':
            self.make_salaried(float(self.salary))
        else:
            self.make_commissioned(float(self.salary), float(self.commission))

        if self.pay_method == '1':
            self.direct_method(self.rout_num, self.acct_num)
        else:
            self.mail_method()

    def make_hourly(self, rate):
        """Creates Hourly object from provided rate"""

        self.classification = Hourly(self.emp_id, rate)

    def make_salaried(self, slry):
        """Creates Salaried object from provided salary"""

        self.classification = Salaried(self.emp_id, slry)

    def make_commissioned(self, slry, rate):
        """Creates Commissioned object from provided salary/rate"""

        self.classification = Commissioned(self.emp_id, slry, rate)

    def direct_method(self, rout, acct):
        """Creates DirectMethod object from routing/account numbers"""

        self.pay_method = DirectMethod(self.emp_id, rout, acct)

    def mail_method(self):
        """Creates MailMethod object from address information"""

        self.pay_method = MailMethod(self.emp_id, self.address, self.city, self.state, self.zipcode)

    def issue_payment(self):
        """Calculates/delivers employee payments"""

        self.classification.compute_pay()


class Classification(ABC):
    """Abstract class serving as template for classifications"""

    def __init__(self, eid):
        """Provides subclasses with instances of associated Employees"""

        self.emp = find_employee_by_id(eid)
        self.total_pay = 0.0

    @abstractmethod
    def compute_pay(self):
        """Template for subclasses' compute_pay method"""

        pass


class Hourly(Classification):
    """Represents an hourly payment classification"""

    def __init__(self, eid, rate):
        """Calls parent's __init__, giving access to Employee reference
        Each Employee has unique rate and time_cards"""

        super().__init__(eid)
        self.rate = rate
        self.time_cards = []

    def add_timecard(self, hrs):
        """Adds entry to time_cards list"""

        self.time_cards.append(float(hrs))

    def compute_pay(self):
        """Totals hours, then multiplies them by rate
        Sends total_pay to payment method"""

        hours = reduce(lambda x, y: x + y, [float(card) for card in self.time_cards])
        self.total_pay = self.rate * hours
        self.time_cards.clear()

        self.emp.pay_method.pay(self.emp.name, self.total_pay)


class Salaried(Classification):
    """Represents a salaried payment classification"""

    def __init__(self, eid, slry):
        """Calls parent's __init__, giving access to Employee reference
        Each Employee has unique salary"""

        super().__init__(eid)
        self.salary = slry

    def compute_pay(self):
        """Calculates a bimonthly salary
        Sends total_pay to payment method"""

        self.total_pay = self.salary / 24

        self.emp.pay_method.pay(self.emp.name, self.total_pay)


class Commissioned(Salaried):
    """Represents a commissioned payment classification
    Parented by Salaried, as similarities are shared"""

    def __init__(self, eid, slry, rate):
        """Calls parent's __init__, giving access to Employee reference
        Each Employee has unique salary, rate, and receipts"""

        super().__init__(eid, slry)
        self.rate = rate / 100
        self.receipts = []

    def add_receipt(self, amnt):
        """Adds entry to receipts list"""

        self.receipts.append(amnt)

    def compute_pay(self):
        """Converts rate to percentage, using it to calculate commission
        Adds commission to bimonthly salary
        Sends total_pay to payment method"""

        commission = map(lambda x: x * self.rate, [float(rec) for rec in self.receipts])
        com_total = reduce(lambda x, y: x + y, commission)
        self.total_pay = (self.salary / 24) + com_total
        self.receipts.clear()

        self.emp.pay_method.pay(self.emp.name, self.total_pay)


class PaymentMethod(ABC):
    """Abstract class serving as template for methods"""

    def __init__(self, eid):
        """Provides subclasses with instances of associated Employees"""

        self.emp = find_employee_by_id(eid)

    @abstractmethod
    def pay(self, name, amnt):
        """Template for subclasses' pay method"""

        pass


class DirectMethod(PaymentMethod):
    """Represents a direct payment method"""

    def __init__(self, eid, rout, acct):
        """Calls parent's __init__, giving access to Employee reference
        Routing/account numbers are provided"""

        super().__init__(eid)
        self.rout_num = rout
        self.acct_num = acct

    def pay(self, name, amnt):
        """Writes payment to text file using provided information"""

        with open(PAY_LOGFILE, 'a') as pay_file:
            pay_file.write(f"Transferred {'%.2f' % amnt} for {name} to {self.acct_num} at {self.rout_num}\n")
        pay_file.close()


class MailMethod(PaymentMethod):
    """Represents a mailed payment method"""

    def __init__(self, eid, addr, city, st, code):
        """Calls parent's __init__, giving access to Employee reference
        Address information is provided"""

        super().__init__(eid)
        self.address = addr
        self.city = city
        self.state = st
        self.zipcode = code

    def pay(self, name, amnt):
        """Writes payment to file using provided information"""

        with open(PAY_LOGFILE, 'a') as pay_file:
            pay_file.write(f"Mailing {'%.2f' % amnt} to {name} at {self.address} {self.city} "
                           f"{self.state} {self.zipcode}\n")
        pay_file.close()


def load_employees():
    """Extracts information from text file, line by line
    Places ',' separated items in list, then plugged in as Employee arguments
    Assigns classifications to Employee objects"""

    with open("employees.csv", 'r') as emp_list:
        for line in emp_list.readlines()[1:]:
            args = [arg.strip() for arg in line.split(',')]
            emp = Employee(*args)
            employees.append(emp)
            emp.classify()


def process_timecards():
    """Extracts information from text file, line by line
    provides default time cards for Employee Hourly objects"""

    with open("timecards.csv", 'r') as time_list:
        for line in time_list:
            time_cards = []
            for card in line.split(','):
                time_cards.append(card.strip())
            emp = find_employee_by_id(time_cards[0])
            emp.classification.time_cards = time_cards[1:]


def process_receipts():
    """Extracts information from text file, line by line
    provides default time cards for Employee Commissioned objects"""

    with open("receipts.csv", 'r') as rec_list:
        for line in rec_list:
            receipts = []
            for rec in line.split(','):
                receipts.append(rec.strip())
            emp = find_employee_by_id(receipts[0])
            emp.classification.receipts = receipts[1:]


def run_payroll():
    """Deletes old paylog file if it exists
    Writes down every employee's payment to text file"""

    if os.path.exists(PAY_LOGFILE):
        os.remove(PAY_LOGFILE)
    for emp in employees:
        emp.issue_payment()


def find_employee_by_id(eid):
    """Uses unique employee id to find Employee object"""

    for emp in employees:
        if emp.emp_id == eid:
            return emp


employees = []
PAY_LOGFILE = "paylog.txt"
