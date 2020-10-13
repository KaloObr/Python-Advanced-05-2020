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



num = int(input())
matrix = []

for _ in range(num):
    matrix.append(
        read_int_list_from_input()
    )


primary_diagonal = calculate_primary_diagonal_sum(matrix)
secondary_diagonal = calculate_secondary_diagonal_sum(matrix)
difference = abs(primary_diagonal - secondary_diagonal)

print(difference)
