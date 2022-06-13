def make_readable(sec):
    return f'{sec//3600:02d}:{(sec%3600)//60:02d}:{sec%60:03d}'