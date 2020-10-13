def is_number_valid(number):
    return any([number % d == 0 for d in range(2, 11)])


start_num = int(input())
end_num = int(input())

print(
    [x for x in range(start_num, end_num + 1) if is_number_valid(x)]
)

