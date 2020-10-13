def chair_combinations(names, size, result=[]):
    if len(result) == size:
        print(", ".join(result))
        return
    for i in range(len(names)):
        name = names[i]
        result.append(name)
        chair_combinations(names[i + 1:], size, result)
        result.pop()


names = input().split(', ')
size = int(input())
chair_combinations(names, size)
