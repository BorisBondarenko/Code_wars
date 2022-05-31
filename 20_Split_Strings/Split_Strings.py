def solution(txt: str):
    x = len(txt)
    if x % 2 != 0:
        txt = txt.ljust(x + 1, '_')
    return [txt[i: i + 2] for i in range(0, x, 2)]
