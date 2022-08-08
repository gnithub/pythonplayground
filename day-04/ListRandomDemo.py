import random

friendList = input("enter your friends name").split(',')

print(friendList)

randomname = random.randint(0,len(friendList)-1)

print(friendList[randomname])

print(random.choice(friendList))