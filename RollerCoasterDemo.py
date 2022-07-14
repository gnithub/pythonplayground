height = int(input("Enter height : "))
bill = 0
if height < 120 :
  print("Please grow taller.")
else:
  age = int(input("Enter age : "))

  if age < 12:
     bill =12
     print("Pay $5")
  elif age < 18:
     bill = 7
     print("Pay $7")
  else:
     bill = 10
     print("Pay $10")
  want_photo=input("Do you want photo : y/n : ")

  if want_photo=="Y":
     bill +=3

  print(f"Final bill is ${bill}")
