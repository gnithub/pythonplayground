def isPrimeNumber(number):
    isAPrimeNumber = True
    for i in range(2,number-1):
        if number%i == 0:
            isAPrimeNumber = False

    if isAPrimeNumber:
        print(f"This {number}  is a prime number")
    else:
        print(f"This {number} is not a prime number")

number=int(input("Input a number: "))
isPrimeNumber(number)
