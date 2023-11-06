import numpy as np

# Get data and produce matrix
initial_input = input()
n, m = map(int, initial_input.split())
matrix = np.empty((n, m), dtype=str)
for i in range(n):
    row = input().replace(" ", "")
    matrix[i] = list(row)
# print(matrix)


def kill_flies(matrix):
    count_F_in_rows = np.count_nonzero(matrix == "F", axis=1)
    count_F_in_columns = np.count_nonzero(matrix == "F", axis=0)
    # print(count_F_in_rows)
    # print(count_F_in_columns)
    row_indices, col_indices = np.where(matrix == "B")
    # print(row_indices,col_indices)
    num_of_flies = count_F_in_rows[row_indices] + count_F_in_columns[col_indices]
    # print(num_of_flies)
    max_flies = np.max(num_of_flies)

    return max_flies

print(kill_flies(matrix))
