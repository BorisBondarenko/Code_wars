def increment_string(strng):
    dig_s = []
    sym_s = []
    flag = True
    if strng.rstrip():
        for i in strng[::-1]:
            if i.isdigit() and flag:
                dig_s.append(i)
            else:
                sym_s.append(i)
                flag = False
        num = ''.join(dig_s[::-1]) if dig_s else '0'
        return f'{"".join(sym_s[::-1])}{str(int(num) + 1).rjust(len(num), "0")}'
    else:
        return '1'


text = 'foo012'
print(increment_string(text))
