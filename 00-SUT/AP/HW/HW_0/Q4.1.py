def checking(i: int, j: int, matrix: list, n, m):
    num_of_fly = 0
    for k in range(j, m):
        if matrix[i][k] == "F":
            num_of_fly += 1
        elif matrix[i][k] == "C":
            break
    for k in range(j - 1, -1, -1):
        if matrix[i][k] == "F":
            num_of_fly += 1
        elif matrix[i][k] == "C":
            break
    for k in range(i, n):
        if matrix[k][j] == "F":
            num_of_fly += 1
        elif matrix[k][j] == "C":
            break
    for k in range(i - 1, -1, -1):
        if matrix[k][j] == "F":
            num_of_fly += 1
        elif matrix[k][j] == "C":
            break
    return num_of_fly


def kill_flies(matrix: list, n, m):
    max_fly = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "B":
                num_of_fly = checking(i, j, matrix, n, m)
                if max_fly < num_of_fly:
                    max_fly = num_of_fly
    return max_fly


# Get data and produce matrix
initial_input = input()
n, m = map(int, initial_input.split(" "))
matrix = []
for i in range(n):
    row = list(input().split(" "))
    matrix.append(row)

print(kill_flies(matrix, n, m))
