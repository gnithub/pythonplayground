import random

choice = int(input("Enter your choice: "))

print(choice)

if choice > 2:
    print("invalid choice")
else:
    comp_choice = random.randint(0,2)
    print(comp_choice)
    if choice > comp_choice:
       print('You win')
    elif choice == comp_choice:
        print("Draw")
    else:
        print("You lose")



