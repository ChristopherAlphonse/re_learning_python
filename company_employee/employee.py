class Employee:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class SalaryEmployee(Employee):
    def __init__(self, first_name: str, last_name: str, salary: float):
        super().__init__(first_name, last_name)
        self.salary = salary

    def calculate_paycheck(self) -> float:
        return self.salary / 52


class HourlyEmployee(Employee):
    def __init__(
        self, first_name: str, last_name: str, weekly_hours: float, hourly_rate: float
    ):
        super().__init__(first_name, last_name)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def calculate_paycheck(self) -> float:
        return self.weekly_hours * self.hourly_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(
        self,
        first_name: str,
        last_name: str,
        salary: float,
        sales: float,
        commission_rate: float,
    ):
        super().__init__(first_name, last_name, salary)
        self.sales = sales
        self.commission_rate = commission_rate

    def calculate_paycheck(self) -> float:
        normal_salary = super().calculate_paycheck()
        total_commission = self.sales * self.commission_rate
        return normal_salary + total_commission
