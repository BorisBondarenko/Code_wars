def abbrev_name(name):
    return '.'.join([i[0].capitalize() for i in name.split(' ')])


if __name__ == '__main__':
    print("Example:")

    # These "asserts" are used for self-checking and not for an auto-testing
    assert abbrev_name("Sam Harris") == "S.H"
    assert abbrev_name("patrick feenan") == "P.F"
    assert abbrev_name("Evan C") == "E.C"
    assert abbrev_name("P Favuzzi") == "P.F"
    assert abbrev_name("David Mendieta") == "D.M"

    print("Coding complete!")
