
row1 = ['0', '0', '0']
row2 = ['0', '0', '0']
row3 = ['0', '0', '0']

map = [row1, row2,row3]
print(str(map[0])+"\n"+str(map[1])+"\n"+str(map[2]))

coordinate = input('Input coordinates ? ')
x = int(coordinate[0])
y = int(coordinate[1])

map[x-1][y-1]="1"

print(str(map[0])+"\n"+str(map[1])+"\n"+str(map[2]))

