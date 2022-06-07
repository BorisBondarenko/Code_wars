def likes(names):
    vars = {0: 'no one likes this',
            1: f'xx likes this',
            2: f'xx and xx like this',
            3: f'xx, xx and xx like this',
            4: f'xx, xx and nn others like this'}

    res = vars[len(names)] if len(names) < 5 else vars[4]
    for name in names:
        res = res.replace('xx', name, 1)
        if 'nn' in res:
            res = res.replace('nn', f'{len(names) - 2}')

    return res