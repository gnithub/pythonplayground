# Pizza order system
yourname = input("Your name ")
theirname = input("Their name")

yourname = yourname.lower() + theirname.lower()


t = yourname.count('t')
r = yourname.count('r')
u = yourname.count('u')
e = yourname.count('e')

l = yourname.count('l')
o = yourname.count('o')
v = yourname.count('v')
e = yourname.count('e')

score = int(str(t+r+u+e) + str(l+o+v+e))

print(f"your score is {score}")

if (score<10) or (score > 90) :
   print("You are cola and mentos")
elif (score>=40) and ( score <= 50):
   print("You are great match")
else:
   print("You are okay")

