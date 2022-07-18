height = int(input("Enter height : "))

if height < 120 :
  print("Please grow taller.")
else:
  age = int(input("Enter age : "))
  if age < 12:
     print("Pay $5")
  elif age < 18:
     print("Pay $7")
  elif age < 55 and age > 45:
     print("enjoy free ride")
  else:
     print("Pay $10")

