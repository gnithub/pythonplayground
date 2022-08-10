scores = [324,34,23,34,324,35,45,345,4534,3,345]

max = 0
for s in scores:
    if max < s:
        max = s


print(f"Max score is {max}")