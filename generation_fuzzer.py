import random


def get_code():
    character = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ()not->>=<<===!=*/%+-andor"
    num_char = "0123456789"
    length = random.randint(1, 6)
    output = character[random.randint(0, 78)]
    for i in range(0, length):
        char_type = random.randint(1, 2)
        if char_type == 1:
            output = output + character[random.randint(0, 52)]
        else:
            output = output + num_char[random.randint(0, 9)]
    return output


if __name__ == "__main__":
    gen_code = ""
    code_length = random.randint(3, 20)
    for i in range(0, code_length):
        gen_code = gen_code + " " + get_code()
    f = open("generated_fuzz.txt", "w")
    f.write(gen_code)