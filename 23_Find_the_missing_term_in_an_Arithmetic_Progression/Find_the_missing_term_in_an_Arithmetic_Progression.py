def find_missing(seq):
    all_steps = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
    step = max(set(all_steps), key=lambda x: all_steps.count(x))
    start, *_, finish = seq

    return list(set(range(start, finish + step, step)) - set(seq))[0]
