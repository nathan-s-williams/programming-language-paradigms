import random


def fuzzer():
    sign = random.randint(1, 3)
    fuzz_int = ""
    if sign == 1:
        fuzz_int = "+"
    elif sign == 2:
        fuzz_int = "-"
    length = random.randint(0, 3)
    for i in range(0, length):
        fuzz_int = fuzz_int + str(random.randint(0, 10))
    return fuzz_int


print(fuzzer())
