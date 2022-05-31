def shortcut(s):
    return ''.join([i for i in s if i not in 'aeiou'])


if __name__ == '__main__':
    print("Example:")
    assert shortcut('hello') == 'hll'

    print("Coding complete!")
