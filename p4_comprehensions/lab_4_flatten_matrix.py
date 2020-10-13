def read_matrix():
    rows_count = int(input())
    return [map(int, input().split(', ')) for _ in range(rows_count)]


matrix = read_matrix()
flattened = []

for sublist in matrix:
    [flattened.append(num) for num in sublist]

print(flattened)
