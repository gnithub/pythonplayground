def is_leapyear(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
 
leap_year = is_leapyear(int(input("Please input year: ")))

if leap_year:
   print ("THis is leap year")
else:
  print("This is not leap year")

