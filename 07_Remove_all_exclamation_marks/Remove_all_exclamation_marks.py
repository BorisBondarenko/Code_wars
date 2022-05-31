def remove(s):
    return f"{s.replace('!', '')}!"

if __name__ == '__main__':
    print("Example:")

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove("Hi!") == "Hi!"
    assert remove("Hi!!!") == "Hi!"
    assert remove("!Hi") == "Hi!"
    assert remove("!Hi!") == "Hi!"
    assert remove("Hi! Hi!") == "Hi Hi!"
    assert remove("Hi") == "Hi!"


    print("Coding complete!")