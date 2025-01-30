# payroll_Tilaki_Anahita.py
# Main program to test the Employee and Payroll 
# Author: Anahita Tilaki
# Date: 10-06-2024

from employees import Employee, CommissionPaid, HourlyPaid

def total_pay(employee_list):
    return sum([employee.pay() for employee in employee_list])

def print_employee_list(employee_list):
    print("Employee Type     Employee Name       Department     Weekly Pay")
    print("---------------------------------------------------------------")
    for employee in employee_list:
        print(f"{str(employee):<20}")

def main():
    # Create CommissionPaid objects
    emp1 = CommissionPaid("Fname1 Lname1", "Finance", 500, 15000)
    emp2 = CommissionPaid("Fname2 Lname2", "Sales", 1000, 8000)

    # Create HourlyPaid objects
    emp3 = HourlyPaid("Fname3 Lname3", "Accounting", 20.5, 60)
    emp4 = HourlyPaid("Fname4 Lname4", "Marketing", 35, 30)

    # Add employees to a list
    employee_list = [emp1, emp2, emp3, emp4]

    # Print employee information and total pay
    print_employee_list(employee_list)
    print(f"Total Pay for the Week: ${total_pay(employee_list):.2f}")

if __name__ == "__main__":
    main()

input("Press Enter to exit")
