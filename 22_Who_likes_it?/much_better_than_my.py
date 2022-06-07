vars = {0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'}


def likes(names):
    return vars.get(len(names), vars[4]).format(*names, others=len(names) - 2)