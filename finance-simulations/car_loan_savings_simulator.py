salary = 12000
car_price = 729000
month = 1
total_savings = 0
month = 1

try:
  if salary >= 15000:
    print("Status: Eligible for a full loan immediately!")
  elif salary >= 12000:
    print("Status: Conditionally eligible; a promotion is required to qualify for the full loan amount.")
  else:
    print("Status: Salary is too low; need to upskill.")
  while total_savings < car_price:
    monthly_saving = salary * 0.35
    total_savings = total_savings + monthly_saving

    if month == 12:
      salary = salary * 1.10
      print(f"salary : {salary}")
      month = 0

    month = month + 1
  print("you can purchase your new car!!")

except:
  print("ERRORRR!")
