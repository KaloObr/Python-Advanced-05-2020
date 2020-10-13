def generate_number_ranges(collection):
    generated_ranges = []
    range_start = int(collection[0])
    range_finish = int(collection[1])

    for number in range(range_start, range_finish+1):
        generated_ranges.append(number)

    return generated_ranges


def get_intersection(n):
    intersections = []

    for _ in range(n):
        intersected_numbers = []
        range_of_numbers = input().split('-')

        for numbers in range_of_numbers:
            intersected_numbers.append(generate_number_ranges(numbers.split(',')))

        set_one = set(intersected_numbers[0])
        set_two = set(intersected_numbers[1])
        intersections.append(set_one.intersection(set_two))

    return intersections


def print_results(collection_of_intersections):
    longest_range = None
    longest_length = 0

    for x in collection_of_intersections:
        if len(x) > longest_length:
            longest_range = list(x)
            longest_length = len(x)

    print(f'Longest intersection is {longest_range} with length {longest_length}')


print_results(
    get_intersection(int(input()))
)
