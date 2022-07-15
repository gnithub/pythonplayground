# Pizza order system
size = input("Size S/M/L: ")
add_pep = input("Add pep y/n: ")
add_cheeze = input("Add cheese y/n: ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
     bill += 25

if add_pep == "Y":
    if size=="S":
        bill += 2
    else:
        bill +=3

if add_cheeze == "Y" :
    bill +=1

print(f"You final bill is {bill}")
