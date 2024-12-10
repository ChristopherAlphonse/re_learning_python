from employee import HourlyEmployee, SalaryEmployee, CommissionEmployee


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employee(self):
        print("______________")
        print("Current Employees:")
        for employee in self.employees:
            print(f"{employee.first_name}, {employee.last_name}")
        print("______________")

    def pay_employee(self):
        print("______________")
        print("Paying Employee:")
        for paycheck in self.employees:
            print(
                f"{paycheck.first_name}, {paycheck.last_name}: {paycheck.calculate_paycheck():,.2f}"
            )
        print("______________")


def main():
    enterprise_llc = Company()
    employee1 = SalaryEmployee("John", "Doe", 250000)
    enterprise_llc.add_employee(employee1)
    employee2 = HourlyEmployee("Jane", "Doe", 32, 45)
    enterprise_llc.add_employee(employee2)
    employee3 = CommissionEmployee("Smith", "Doe", 40000, 20, 200)
    enterprise_llc.add_employee(employee3)
    enterprise_llc.display_employee()
    enterprise_llc.pay_employee()


main()
