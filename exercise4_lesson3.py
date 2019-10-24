id_employee = str(input("Type your ID Employee: "))
work_hours = int(input("Inform the total hours worked in the month: "))
amount_hours = float(input("Inform work hour amount:  "))

salary_calculation = work_hours*amount_hours

print("Employee ", id_employee, "you salary of the month is : $", salary_calculation)