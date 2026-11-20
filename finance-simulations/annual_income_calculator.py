def calculate_annual_income(monthly_salary,month_in_a_year):
  total_amount_peryear = monthly_salary * month_in_a_year
  return total_amount_peryear

compony_name = "Teach SG"
monthly_salary = 12000
month_in_a_year = 12

try:
  total = calculate_annual_income(monthly_salary,month_in_a_year)
except ValueError:
  print("ERRORRRRRR!!!")

#output
print(f"COMPONY NAME               : {compony_name}")
print(f"SALARY                     : RM {monthly_salary:.2f}/month")
print(f"TOTAL AMOUNT FOR ONE YEARS : RM {total:.2f}/years")
