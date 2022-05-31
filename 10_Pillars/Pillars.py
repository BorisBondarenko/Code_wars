def pillars(n, d, w):
    return 0 if n <= 1 else ((n - 1) * d) * 100 + w * (n - 2)


if __name__ == '__main__':
    print("Example:")

    # These "asserts" are used for self-checking and not for an auto-testing
    assert pillars(1, 10, 10) == 0
    assert pillars(2, 20, 25) == 2000
    assert pillars(11, 15, 30) == 15270

    print("Coding complete!")
