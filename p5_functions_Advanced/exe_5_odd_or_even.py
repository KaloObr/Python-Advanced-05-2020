def get_odd_or_even_sum(numbers, num_type):
    n = len(numbers)

    if num_type == "Odd":
        odd = sum([x for x in numbers if x % 2 != 0])
        return odd * n
    else:
        even = sum([x for x in numbers if x % 2 == 0])
        return even * n


command = input()
nums = [int(x) for x in input().split()]

print(get_odd_or_even_sum(nums,command))


