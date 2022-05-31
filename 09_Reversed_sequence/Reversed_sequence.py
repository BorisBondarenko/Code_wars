def reverse_seq(n):
    return [i for i in range(n, 0, -1)]


if __name__ == '__main__':
    print("Example:")

    # These "asserts" are used for self-checking and not for an auto-testing
    assert reverse_seq(5) == [5, 4, 3, 2, 1]
    print("Coding complete!")