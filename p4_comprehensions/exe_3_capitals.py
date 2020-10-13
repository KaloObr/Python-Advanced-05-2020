def print_result():
    return {print(f"{key} -> {value}") for (key, value) in result.items()}


capitals = input().split(", ")
cities = input().split(", ")
result = dict(zip(capitals, cities))

print_result()
