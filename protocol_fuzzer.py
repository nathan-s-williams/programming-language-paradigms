import random

select_keywords = ["then", "else", "end"]
loop_keywords = ["while", "do", "for", "end"]
operators = ["+", "-", "*", "/", "%", "not", "("]
logical_operators = ["<", ">", "<=", ">=", "==", "!=", "and", "or"]
io_keywords = ["print", "get"]
# Remaining operators: "=", ";", ")", "if"
stmt = ["print", "input", "assign", "if", "while", "for"]


def get_operator():
    pass

def get_logical_operator():
    pass

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

# def get_select_stmt():
#     length = random.randint(0, 2)
#     for i in range(0, length):
#         if i == 0:
#             stmt = stmt + "if"
#         else:
#             stmt = stmt + " if"
#         stmt = stmt + " " + random.choice(get_id(),get_digit())
#         stmt = stmt + " " +



def prot_fuzzer():
    output = ""
    length = random.randint(1, 10)
    for i in range(0, length):
        output = output + (random.choice(keywords) + " " + random.choice([get_id, get_digit, get_comment])() + "\n")
    return output

    # Break up the keywords into categories and make an if for each one. Structure each one appropriately.


print(prot_fuzzer())
