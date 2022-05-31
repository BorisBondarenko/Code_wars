def uni_total(s):
    return sum(map(ord, s))


if __name__ == '__main__':
    print("Example:")
    assert uni_total("a") == 97
    assert uni_total("b") == 98
    assert uni_total("c") == 99
    assert uni_total("") == 0
    assert uni_total("aaa") == 291
    assert uni_total("abc") == 294
    assert uni_total("Mary Had A Little Lamb") == 1873
    assert uni_total("CodeWars rocks") == 1370
    assert uni_total("And so does Strive") == 1661

    print("Coding complete!")
