numbers = [int(x) for x in input().split(', ')]

positive = [num for num in numbers if num >= 0]
negative = [num for num in numbers if num < 0]
even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]

print(f"Positive: {', '.join([str(num) for num in positive])}")
print(f"Negative: {', '.join([str(num) for num in negative])}")
print(f"Even: {', '.join([str(num) for num in even])}")
print(f"Odd: {', '.join([str(num) for num in odd])}")

