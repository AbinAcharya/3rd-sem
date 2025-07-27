n = int(input("enter the number of elements: "))
matrix = []
for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input("enter the elements: ")))
    matrix.append(a)

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = '')
    print()

count = 0
normal = 0
for i in matrix:
    for j in i:
        if j == 0:
            count = count+1
        else:
            normal = normal+1

if count>normal:
    print("yes")
else:
    print("no")
    