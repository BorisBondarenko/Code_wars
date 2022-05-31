def remove(s):
    return s[:-1] if len(s) > 0 and s[-1] == '!' else s


if __name__ == '__main__':
    print("Example:")

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove("Hi!") == "Hi"
    assert remove("Hi!!!") == "Hi!!"
    assert remove("!Hi") == "!Hi"
    assert remove("!Hi!") == "!Hi"
    assert remove("Hi! Hi!") == "Hi! Hi"
    assert remove("Hi") == "Hi"


    print("Coding complete!")