def set_number_counts(collection):
    (set_one, set_two) = map(int, collection.split())
    set_one_numbers = set()
    set_two_numbers = set()

    for i in range(set_one):
        numbers = int(input())
        if numbers not in set_one_numbers:
            set_one_numbers.add(numbers)

    for _ in range(set_two):
        numbers = int(input())
        if numbers not in set_two_numbers:
            set_two_numbers.add(numbers)

    return set_one_numbers.intersection(set_two_numbers)


def print_result(some_set):
    [print(number) for number in some_set]


print_result(
    set_number_counts(input())
)



