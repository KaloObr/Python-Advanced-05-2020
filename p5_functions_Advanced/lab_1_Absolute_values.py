def to_abs_list(value):
    return [abs(float(num)) for num in value]


print(to_abs_list(input().split()))



