def generate_hashtag(s, res=''):
    res = '#' + ''.join(map(str.capitalize, s.split()))
    return res if 1 < len(res) <= 140 else False


text = 'Do We have A Hashtag'
print(generate_hashtag(text))
