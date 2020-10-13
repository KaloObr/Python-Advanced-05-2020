def get_values_count(values):
    collection = {}
    for value in values:
        if value not in collection:
            collection[value] = 0
        collection[value] += 1

    return collection


def print_values(values_count):
    for k, v in values_count.items():
        print(f'{k} - {v} times')


print_values(get_values_count(map(float, input().split(' '))))

