import random

keywords = ["print", "get", "if", "then", "else", "end", "while", "do", "end", "and", "or", "not", "for"]


def get_id():
    var = ""
    alpha_char = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num_char = "0123456789"
    length = random.randint(1, 10)
    var = alpha_char[random.randint(0, 52)]
    for i in range(0, length):
        char_type = random.randint(1, 2)
        if char_type == 1:
            var = var + alpha_char[random.randint(0, 52)]
        else:
            var = var + num_char[random.randint(0, 9)]
    return var


def get_digit():
    var = ""
    sign = ["", "+", "-"]
    num_char = "0123456789"
    length = random.randint(1, 10)
    var = sign[random.randint(0, 2)]
    for i in range(0, length):
        var = var + num_char[random.randint(0, 9)]
    return var


def get_comment():
    comm = random.randint(0, 20)
    if comm == 0:
        return "// This is comment number 1"
    elif comm == 1:
        return "// This is comment number 2"
    elif comm == 2:
        return "// This is comment number 3"
    elif comm == 3:
        return "// This is comment number 4"
    elif comm == 4:
        return "// This is comment number 5"
    else:
        return ""



def prot_fuzzer():
    output = ""
    length = random.randint(1, 10)
    for i in range(0, length):
        output = output + (random.choice(keywords) + " " + random.choice([get_id, get_digit, get_comment])() + "\n")
    return output

    # Break up the keywords into categories and make an if for each one. Structure each one appropriately.

    # return get_id()
    # return get_comment()


print(prot_fuzzer())
