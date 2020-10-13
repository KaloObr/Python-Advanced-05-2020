def get_even_number(x):
    if x % 2 == 0:
        return True
    else:
        return False


nums = [int(x) for x in input().split()]
even = list(filter(get_even_number, nums))

print(even)
