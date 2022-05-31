def well(x):
    d = {0: 'Fail!', 1: 'Publish!', 2: 'Publish!', 3: 'I smell a series!'}
    return d.setdefault(x.count('good'), 'I smell a series!')


if __name__ == '__main__':
    print("Example:")

    # These "asserts" are used for self-checking and not for an auto-testing
    assert well(['bad', 'bad', 'bad']) == 'Fail!'
    assert well(['good', 'bad', 'bad', 'bad', 'bad']) == 'Publish!'
    assert well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']) == 'I smell a series!'

    print("Coding complete!")
