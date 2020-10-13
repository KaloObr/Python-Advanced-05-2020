def get_even_word(string):
    words = string.split()
    return [word for word in words if len(word) % 2 == 0]


even_words = get_even_word(input())
[print(word) for word in even_words]

