def read_int_list_from_input(seperator=' '):
    return [int(x) for x in input().split(seperator)]


def calculate_primary_diagonal_sum(raw_matrix):
    diagonal_sum = 0
    for i in range(len(raw_matrix)):
        diagonal_sum += raw_matrix[i][i]
    return diagonal_sum


def calculate_secondary_diagonal_sum(raw_matrix):
    diagonal_sum = 0
    n = len(raw_matrix)
    for i in range(n):
        diagonal_sum += raw_matrix[i][- i - 1]
    return diagonal_sum


def calculate_below_primary_diagonal_sum(raw_matrix):
    n = len(raw_matrix)
    the_sum = 0
    for row in range(n):
        for col in range(row + 1):
            the_sum += raw_matrix[row][col]
    return the_sum


def calculate_below_secondary_diagonal_sum(raw_matrix):
    n = len(raw_matrix)
    the_sum = 0
    for row in range(n):
        for col in range(n - row - 1, n):
            the_sum += raw_matrix[row][col]
    return the_sum


num = int(input())
matrix = []

for _ in range(num):
    matrix.append(
        read_int_list_from_input()
    )


print(calculate_primary_diagonal_sum(matrix))
print(calculate_secondary_diagonal_sum(matrix))
print(calculate_below_primary_diagonal_sum(matrix))
print(calculate_below_secondary_diagonal_sum(matrix))
