def solution(number):
    if number > 0:
        return sum([i for i in range(1, number) if i % 3 == 0 or i % 5 == 0])
    elif number <= 0:
        return 0