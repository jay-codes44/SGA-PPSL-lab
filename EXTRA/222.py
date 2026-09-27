month = int(input("enter the number of month (1-12) :"))

if month == 2:
  print("28 days in month")

 elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
  print("31 days in month")
 else:
  print("30 days in month")
