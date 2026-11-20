total_savings = 0
month = 0
percent_saving = 0
year = 0
bonus = 0

try:
  salary = int(input("how much your salary per month? : RM"))
  target_amount = int(input("how much your target amount? : RM"))

  if salary >= 15000:
    percent_saving = 0.45
    print("Tier: Aggressive Wealth Builder")
  elif salary >= 10000:
    percent_saving = 0.35
    print("Tier: Steady Growth")
  else:
    percent_saving = 0.20
    print("Tier: Foundation Phase")
  
  goal_reached = False

  while total_savings < target_amount:
    total_savings += salary * percent_saving
    month += 1
    if month == 12:
      salary = salary * 1.12
      year += 1
      bonus = salary * 0.50
      total_savings += bonus
      print(f"total savings : RM{total_savings:.2f} for {year} years")
      month = 0
    if year >= 30:
      print("Target not reached within 30 years.")
      break
  
  if total_savings >= target_amount:
    print("goal reached!")
  else:
    print("goal not reached yet!!")

except ValueError:
  print("ERRORR!!!")

else:
  print(f"salary        : {round(salary)}")
  print(f"total savings : RM{total_savings:.2f}")
  print(f"years         : {year}")
  print(f"months        : {month}")
