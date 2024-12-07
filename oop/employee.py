class Employee:
    def __init__(self, first_name: str, last_name: str, salary: float):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def hourly_rate(self):
        return f"${self.salary / (40 * 52):,.2f}"

    def bi_weekly_rate(self):
        return f"${self.salary / 52 * 2:,.2f}"

    def monthly_rate(self):
        return f"${self.salary / 12:,.2f}"

    def weekly_rate(self):
        return f"${self.salary / 52 :,.2f}"

    def formatted_weekly_rate(self):
        return f"${self.weekly_rate():,.2f}"
