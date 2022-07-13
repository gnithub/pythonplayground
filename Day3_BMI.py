weight=float(input("Weight in kg:"))
height=float(input("Height in m:"))

bmi = round(weight/height**2)

print(f"bmi is {bmi}")

if bmi < 18.5:
   print("You are underwieght")
elif bmi < 25:
   print("You are healthy")
elif bmi < 30:
   print("You are overweight")
elif bmi < 35:
   print("You are obese")
else:
    print("You are clinically, Obese")

