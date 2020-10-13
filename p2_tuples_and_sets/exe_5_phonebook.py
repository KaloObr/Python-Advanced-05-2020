def get_phone_book():
    count = None
    phone_book = {}

    while True:
        details = input()
        if details.isdigit():
            count = details
            break

        (name, number) = details.split('-')
        if name in phone_book:
            phone_book[name] = number
            continue

        phone_book[name] = number

    return count, phone_book


def print_result(collection):
    count, phone_book = collection

    for _ in range(int(count)):
        name = input()
        if name not in phone_book:
            print(f'Contact {name} does not exist.')
            continue

        print(f'{name} -> {phone_book[name]}')


print_result(get_phone_book())

