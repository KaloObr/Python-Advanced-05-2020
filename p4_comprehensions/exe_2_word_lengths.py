strings = input().split(', ')
strings_len = [len(word) for word in strings]

print(", ".join([f"{x} -> {len(x)}" for x in strings]))
