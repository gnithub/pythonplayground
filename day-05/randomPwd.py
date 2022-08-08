import random

pwdLen = int(input("Lenght of the pwd "))

pwd = ''
for x in range(pwdLen) :
   pwd += str(random.randint(0, 9))

print(f"Your pwd is {pwd}")