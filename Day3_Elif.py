height = int(input("Enter height : "))

if height < 120 :
  print("Please grow taller.")
else:
  age = int(input("Enter age : "))
  if age < 12:
     print("Pay $5")
  elif age < 18:
     print("Pay $7")
  else:
     print("Pay $10")

