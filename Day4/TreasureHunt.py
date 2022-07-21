choice1=input("Left or right..? ").lower()
choice2=input("Swim or wait for boat ").lower()
choice3=input("Which door red,green or yellow ").lower()

if "yellow" == choice3 and "wait" == choice2 and "left" == choice1:
     print('''You won the "game" .. bingo's ''')
else:
     print("Wrong choice .. game OVER.. ")
