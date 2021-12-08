# Doruk Ozar 

income = float(input("Enter your taxable income: "))




if income > 0 and income <= 9700:
  tax = income * 0.1
  print(round(tax, 2))
elif income <= 39475:
  tax = (0.1 * 9700) + (income - 9700) * 0.12
  print(round(tax, 2))
elif income <= 84200:
  tax = (0.1 * 9700) + (0.12 * (39475 - 9700)) + (income - 39475) * 0.22
  print(round(tax, 2))
elif income <= 160725:
  tax = (0.1 * 9700) + (0.12 * (39475 - 9700)) + (0.22 * (84200 - 39475)) + (income - 84200) * 0.24
  print(round(tax, 2))
elif income <=  204100:
  tax = (0.1 * 9700) + (0.12 * (39475 - 9700)) + (0.22 * (84200 - 39475)) + (0.24 * (160725- 84200)) + (income - 160725) * 0.32
  print(round(tax, 2))
elif income <= 510300:
  tax = (0.1 * 9700) + (0.12 * (39475 - 9700)) + (0.22 * (84200 - 39475)) + (0.24 * (160725- 84200)) + (0.32 * (204100 - 160725)) + (income - 204100) * 0.35
  print(round(tax, 2))
else:
   tax = (0.1 * 9700) + (0.12 * (39475 - 9700)) + (0.22 * (84200 - 39475)) + (0.24 * (160725- 84200)) + (0.32 * (204100 - 160725)) + (income - 510300) * 0.37
   print(round(tax, 2))

