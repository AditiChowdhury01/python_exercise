row = int(input("enter the number:"))                    
col = int(input("enter the number:"))
matrix = [[0 for c in range(col)] for r in range(row)]
for r in range(row):
    for c in range(col):
        matrix[r][c] = r*c
print(matrix)
