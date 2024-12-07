from employee import Employee


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def print_employees(self):
        for employee in self.employees:
            print(f"{employee.first_name}, {employee.last_name}")

    def pay_employee(self):
        for employee in self.employees:
            print(f"Paycheck for: {employee.first_name}, {employee.last_name}")
            print(f"Amount: {employee.bi_weekly_rate()}")
            print("------------")

    def pay_monthly_amount(self):
        for employee in self.employees:
            print(f"Paycheck for: {employee.first_name}, {employee.last_name}")
            print(f"Monthly Amount: {employee.monthly_rate()}")
            print("------------")


def main():
    enterprise_llc = Company()
    employee1 = Employee("John", "Doe", 250000)
    enterprise_llc.add_employee(employee1)
    employee2 = Employee("Jane", "Doe", 150000)
    enterprise_llc.add_employee(employee2)
    employee3 = Employee("Smith", "Doe", 50000)
    enterprise_llc.add_employee(employee3)
    employee4 = Employee("Jade", "Doe", 70000)
    enterprise_llc.add_employee(employee4)

    enterprise_llc.pay_employee()

    # enterprise_llc.pay_monthly_amount()


main()
