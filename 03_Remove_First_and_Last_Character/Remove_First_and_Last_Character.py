def remove_char(s):
    return s[1:-1]


if __name__ == '__main__':
    print("Example:")

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_char('country') == 'ountr'
    assert remove_char('person') == 'erso'
    assert remove_char('place') == 'lac'
    assert remove_char('ok') == ''
    assert remove_char('ooopsss') == 'oopss'


    print("Coding complete!")