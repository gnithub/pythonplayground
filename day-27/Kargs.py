def calc(n,**kargs):
   for k,v in kargs.items():
       print(k)
       print(v)
    
   n += kargs["add"]
   n *= kargs.get("multiply")
   return n
  
print(calc(4, add=5, multiply=9))

