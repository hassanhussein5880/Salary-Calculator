name = input("Enter your name:")
hours_worked = int(input("Enter hours worked:"))
hourly_rate = int(input("Enter hourly rate:"))
Gross_pay = hours_worked * hourly_rate
Tax = 22 / 100
Tax_deducted= Gross_pay * Tax
Net_pay = Gross_pay - Tax_deducted



print(f"Employee: {name}")
print(f"Hours: {hours_worked}")
print(f"Rate: {hourly_rate}")
print(f"Gross Salary: {Gross_pay}")
print(f"Tax 22%: {Tax_deducted}")
print(f"Net Pay: {Net_pay}")
