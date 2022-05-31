def spin_words(sentance: str) -> str:
    tmp = map(list, sentance.split())
    return ' '.join(map(lambda x: ''.join(x) if len(x) < 5 else ''.join(x[::-1]), tmp))
