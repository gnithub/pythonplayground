import random

charList = ['b','n','a','b','s','a','#','$','@','^','&','!']

def generatePwd():
   print(charList)
   return random.shuffle(charList)

generatePwd()
print("Password is :", ''.join(charList)) 
