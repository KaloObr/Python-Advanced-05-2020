def get_list_from_input(count):
    return [input() for _ in range(count)]


def get_list_from_input_until_command(command):
    not_arrived = set()
    while True:
        guests = input()
        if guests == command:
            break
        else:
            not_arrived.add(guests)

    return not_arrived


def get_guests_arrived(arrived, not_arrived):
    return set(arrived) - set(not_arrived)


def print_result(result):
    result = sorted(result)

    print(len(result))
    [print(guest) for guest in result if guest[0].isdigit()]
    [print(guest) for guest in result if not guest[0].isdigit()]


print_result(
    get_guests_arrived(
        get_list_from_input(int(input())),
        get_list_from_input_until_command('END')
    )
)


