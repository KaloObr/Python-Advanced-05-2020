n = int(input())
numbers = []

for _ in range(n):
    tokens = input().split(" ")
    command = int(tokens[0])

    if command == 1:
        numbers.append(int(tokens[1]))
    elif command == 2:
        if len(numbers) > 0:
            numbers.pop()
    elif command == 3:
        if numbers:
            print(max(numbers))
    elif command == 4:
        if numbers:
            print(min(numbers))

print(", ".join([str(n) for n in reversed(numbers)]))
