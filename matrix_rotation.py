n = int(input("Enter size of square matrix: "))

matrix = []
for i in range(n):
    row = []
    for j in range(n):
        val = int(input("Enter element at row " + str(i+1) + ", col " + str(j+1) + ": "))
        row.append(val)
    matrix.append(row)

direction = input("Enter rotation direction (clockwise or anticlockwise): ")

rotated = []
for i in range(n):
    rotated.append([0]*n)

if direction == "clockwise":
    for i in range(n):
        for j in range(n):
            rotated[j][n-1-i] = matrix[i][j]
elif direction == "anticlockwise":
    for i in range(n):
        for j in range(n):
            rotated[n-1-j][i] = matrix[i][j]
else:
    print("Invalid direction")
    exit()

print("Rotated Matrix:")
for row in rotated:
    for val in row:
        print(val, end=" ")
    print()
