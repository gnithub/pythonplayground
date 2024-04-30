def division(a,b):
   if b == 0 :
      raise ValueError
   else:
      return a/b

a = int(input("Enter a :"))
b = int(input("Enter b:"))

print("Result: ",division(a,b))

