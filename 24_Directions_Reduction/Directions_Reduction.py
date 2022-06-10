def recycle(seq):
    tmp = seq[:]
    for i in range(len(tmp) - 1):
        if tmp[i] == tmp[i + 1]:
            continue
        elif abs(tmp[i]) == abs(tmp[i + 1]):
            tmp.pop(i)
            tmp.pop(i)
            return recycle(tmp)
        else:
            continue
    if tmp == seq:
        return tmp


def dirReduc(arr):
    dir_val = {"EAST": -1, "WEST": 1, "NORTH": -2, "SOUTH": 2}
    val_dir = {v: k for k, v in dir_val.items()}
    return [val_dir.get(i) for i in recycle([dir_val[i] for i in arr])]


a = ["NORTH", "SOUTH", "EAST", "WEST"]
print(dirReduc(a))
