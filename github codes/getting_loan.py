# Doruk Ozar

age = int(input("Age: "))
if age <= 40:
  income = float(input("Income: "))
  if income > 166500:
    print("granted")
  elif income <= 166500:
    avg_save = float(input("Average montly savings amount: "))
    if avg_save > 657:
      print("granted")
    elif avg_save <= 657:
      print("not granted")

  
elif age > 40:
  avg_save = float(input("Average montly savings amount: "))
  if avg_save > 433:
    print("granted")
  elif avg_save <= 433:
    credit_dur = float(input("Credit duration: "))
    if credit_dur <= 38:
      print("granted")
    elif credit_dur > 38:
      print("not granted")

