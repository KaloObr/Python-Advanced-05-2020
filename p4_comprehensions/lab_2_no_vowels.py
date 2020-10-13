vowels = {'a', 'o', 'u', 'e', 'i'}
string = ''.join([x for x in input() if x not in vowels])

print(string)
