def get_elements_set(number):
    elements_set = set()
    for _ in range(number):
        elements = input().split(' ')

        for element in elements:
            if element not in elements_set:
                elements_set.add(element)

    return elements_set


def print_result(collection):
    [print(element) for element in collection]


print_result(get_elements_set(int(input())))
