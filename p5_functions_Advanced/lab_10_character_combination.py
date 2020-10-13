def permutation(text, index):
    if index >= len(text):
        print("".join(text))
        return
    for i in range(index, len(text)):
        text[index], text[i] = text[i], text[index]
        permutation(text, index + 1)
        text[index], text[i] = text[i], text[index]


string = list(input())
permutation(string, 0)
