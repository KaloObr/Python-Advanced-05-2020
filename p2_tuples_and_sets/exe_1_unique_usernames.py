n = int(input())
collection = set()

for _ in range(n):
    names = input()
    if names not in collection:
        collection.add(names)

[print(names) for names in collection]

