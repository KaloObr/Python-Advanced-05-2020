def get_negative_and_positive_sums(numbers):
    negative = 0
    positive = 0

    for num in numbers:
        if num < 0:
            negative += num

        else:
            positive += num

    return negative, positive


nums = [int(x) for x in input().split()]
negative_sum, positive_sum = get_negative_and_positive_sums(nums)

print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")

