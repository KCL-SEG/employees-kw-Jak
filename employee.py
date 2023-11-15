"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        return 0

    def __str__(self):
        return self.name


class SalariedEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def get_pay(self):
        return self.monthly_salary

    def __str__(self):
        return (f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.monthly_salary}.")


class HourlyEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def get_pay(self):
        return self.hours_worked * self.hourly_rate

    def __str__(self):
        return (f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour. Their total pay is {self.get_pay()}.")


class SalariedCommissionEmployee(SalariedEmployee):
    def __init__(self, name, month_salary, contracts_completed=0, contract_rate=0, bonus=0):
        super().__init__(name, month_salary)
        self.contracts_completed = contracts_completed
        self.contract_rate = contract_rate
        self.bonus = bonus

    def get_pay(self):
        return self.monthly_salary + (self.contracts_completed * self.contract_rate) + self.bonus

    def __str__(self):
        print_str = f"{self.name} works on a monthly salary of {self.monthly_salary} and "
        if self.bonus:
            print_str += f"receives a bonus commission of {self.bonus}. "
        else:
            print_str += (f"receives a commission for {self.contracts_completed} contract(s) at {self.contract_rate}/contract. ")

        print_str += f"Their total pay is {self.get_pay()}."
        return print_str


class HourlyCommissionEmployee(HourlyEmployee):
    def __init__(self, name, hours_worked, hourly_rate, contracts_completed=0, contract_rate=0, bonus=0):
        super().__init__(name, hours_worked, hourly_rate)
        self.contracts_completed = contracts_completed
        self.contract_rate = contract_rate
        self.bonus = bonus

    def get_pay(self):
        return self.hours_worked * self.hourly_rate + self.contracts_completed * self.contract_rate + self.bonus

    def __str__(self):
        print_str = f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour and "
        if self.bonus:
            print_str += f"receives a bonus commission of {self.bonus}. "
        else:
            print_str += (f"receives a commission for {self.contracts_completed} contract(s) at {self.contract_rate}/contract. ")

        print_str += f"Their total pay is {self.get_pay()}."
        return print_str


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalariedEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total
# pay is 3800.
renee = SalariedCommissionEmployee('Renee', 3000, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their
# total pay is 4410.
jan = HourlyCommissionEmployee('Jan', 150, 25, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalariedCommissionEmployee('Robbie', 2000, 0, 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyCommissionEmployee('Ariel', 120, 30, 0, 0, 600)
