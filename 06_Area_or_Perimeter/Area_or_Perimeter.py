def area_or_perimeter(l , w):
    return l*w if l == w else (l+w)*2

if __name__ == '__main__':
    print("Example:")

    # These "asserts" are used for self-checking and not for an auto-testing
    assert area_or_perimeter(4, 4) == 16
    assert area_or_perimeter(6, 10) == 32


    print("Coding complete!")