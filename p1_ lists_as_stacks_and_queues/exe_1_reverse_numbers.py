def reverse_numbers(nums):
    stack = []
    for x in nums:
        stack.append(x)

    result = []
    while stack:
        result.append(stack.pop())

    return print(' '.join(result))


reverse_numbers([x for x in input().split()])
