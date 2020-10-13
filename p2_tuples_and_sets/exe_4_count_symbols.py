def get_symbol_count(line):
    symbols = sorted(line)
    symbols_count = {}

    for char in symbols:
        if char not in symbols_count:
            symbols_count[char] = 0
        symbols_count[char] += 1

    return symbols_count


def print_result(collection):
    for char, count in collection.items():
        print(f'{char}: {count} time/s')


print_result(
    get_symbol_count(input())
)

