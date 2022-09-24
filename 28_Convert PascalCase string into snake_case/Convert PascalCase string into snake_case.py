def to_underscore(string: str) -> str:
    """This func transform string from CamelCase to underscore case"""

    string = str(string)
    for sym in string:
        if sym.isupper():
            string = string.replace(sym, f'_{sym.lower()}')
    return string.lstrip('_')


text = 'App7Test'
print(to_underscore(text))
