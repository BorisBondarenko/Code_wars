def same_case(a, b):
    if a.isalpha() and b.isalpha():
        if a.islower() and b.islower():
            return 1
        elif a.isupper() and b.isupper():
            return 1
        else:
            return 0
    else:
        return -1

same_case("C", "B")

# if __name__ == '__main__':
#     print("Example:")
#     assert same_case('C', 'B') == 1
#     assert same_case('b', 'a') == 1
#     assert same_case('d', 'd') == 1
#     assert same_case('A', 's') == 0
#     assert same_case('c', 'B') == 0
#     assert same_case('b', 'Z') == 0
#     assert same_case('\t', 'Z') == -1
#     assert same_case('H', ':') == -1
#
#     print("Coding complete!")
