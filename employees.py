# employees.py
# Program to calculate weekly pay for employees
# Author: Anahita Tilaki
# Date: 10-06-2024

class Employee:
    def __init__(self, name, department):
        self.__name = name
        self.__department = department

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def pay(self):
        return 0.0

    def __str__(self):
        return f"Employee Name: {self.__name}, Department: {self.__department}"


class CommissionPaid(Employee):
    def __init__(self, name, department, base_pay, sales):
        super().__init__(name, department)
        self.__base_pay = base_pay
        self.__sales = sales

    def get_base_pay(self):
        return self.__base_pay

    def set_base_pay(self, base_pay):
        self.__base_pay = base_pay

    def get_sales(self):
        return self.__sales

    def set_sales(self, sales):
        self.__sales = sales

    def pay(self):
        if self.__sales > 8000:
            commission = self.__sales * 0.03
        elif 3000 <= self.__sales <= 8000:
            commission = self.__sales * 0.015
        else:
            commission = 0
        return self.__base_pay + commission

    def __str__(self):
        return f"Commission Paid: {self.get_name()}, {self.get_department()}, Weekly Pay: {self.pay():.2f}"


class HourlyPaid(Employee):
    def __init__(self, name, department, hourly_rate, hours_worked):
        super().__init__(name, department)
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def get_hourly_rate(self):
        return self.__hourly_rate

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

    def get_hours_worked(self):
        return self.__hours_worked

    def set_hours_worked(self, hours_worked):
        self.__hours_worked = hours_worked

    def pay(self):
        if self.__hours_worked > 40:
            overtime_hours = self.__hours_worked - 40
            overtime_pay = overtime_hours * self.__hourly_rate * 1.75
            return (40 * self.__hourly_rate) + overtime_pay
        else:
            return self.__hours_worked * self.__hourly_rate

    def __str__(self):
        return f"Hourly Paid: {self.get_name()}, {self.get_department()}, Weekly Pay: {self.pay():.2f}"
     

