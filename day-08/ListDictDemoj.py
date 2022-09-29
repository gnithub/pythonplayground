countyLog = [
   {"country" : "India", "visited": 4 , "cities": ["Indore", "Pune", "Mumbai", "Ujjain"] }
]

def addCityLog(country, timeVisisted, cities):
      print("Inside addCityLog")
      country_log = {}
      country_log["country"] = country
      country_log["visited"] = timeVisisted
      country_log["cities"] = cities
      countyLog.append(country_log)


print(f"Before adding {countyLog}")

addCityLog("Germany", 2, ["Duserdorf"])

print(f"After adding {countyLog}")
