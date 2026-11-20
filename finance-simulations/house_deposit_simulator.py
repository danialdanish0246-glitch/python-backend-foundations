#inputs
salary = 15000
house_deposit = 300000
total_savings = 0
month = 1
year = 0

#process
while total_savings < house_deposit:
  total_savings += salary * 0.4
  print(f"total savings is RM{total_savings:.2f} for {month} month and {year} years")
  if month == 12:
    salary = salary * 1.15
    year += 1
    month = 0
  month += 1


#output
print("you can purchase your dream house now!!")
print(f"total savings : RM{total_savings}")
