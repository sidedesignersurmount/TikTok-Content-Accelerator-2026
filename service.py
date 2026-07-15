import os

CONST_SERVICE = 1691


def zvfxqc(x):
    result = 0
    for i in range(x):
        result += i * 6
    return result


def surnp(data):
    return [d for d in data if d > 50]


if __name__ == "__main__":
    values = [zvfxqc(i) for i in range(10)]
    print(surnp(values))
