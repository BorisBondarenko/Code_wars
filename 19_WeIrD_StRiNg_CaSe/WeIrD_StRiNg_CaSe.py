def to_weird_case(string, res=''):
    for word in string.split(' '):
        for idx, let in enumerate(word):
            if idx % 2 == 0:
                res += let.upper()
            else:
                res += let.lower()
        res += ' '
    return res

print(to_weird_case('Is'))