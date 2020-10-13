def even_odd(*args):
    for ch in args[::-1]:
        print(ch)
        if ch == 'even':
            result = [num for num in range(1, len(args))]
            return [num for num in result if num % 2 == 0]
        else:
            result = [num for num in args]
            return [num for num in result if num % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
