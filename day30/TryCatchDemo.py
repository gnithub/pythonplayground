
try:
   file = open("temp.txt")
   a_dict = {"key":"value"}
   # print(a_dict["keyDoesNotExt"])
   print(a_dict["key"])
except FileNotFoundError as error:
  print(f"THere is an error: {error}")
  file = open("temp.txt", "w")
  file.write("Something")
except KeyError as error:
  print(f"Key error as {error}")
else:
  print("Works fine")
finally:
  print("Finally")
  file.close()

