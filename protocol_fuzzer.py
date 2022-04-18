import random

select_keywords = ["then", "else", "end"]
loop_keywords = ["while", "do", "for", "end"]
operators = ["+", "-", "*", "/", "%", "not", "("]
logical_operators = ["<", ">", "<=", ">=", "==", "!=", "and", "or"]
io_keywords = ["print", "get"]
# Remaining operators: "=", ";", ")", "if"
stmt = ["print", "input", "assign", "if", "while", "for"]

if_while_count = 0


def if_while_limit_reached():
    global if_while_count
    # print(if_while_count)
    if if_while_count > 3:
        return True
    if_while_count = if_while_count + 1
    return False


def get_expr():
    return "test"


def get_stmt():
    output = random.choice([get_print(), get_input(), get_assign(), get_if(), get_while()])
    return output


def get_stmt_list(count):
    if count > 2:
        return "\n"
    count = count + 1
    output = get_stmt()
    return output + ";\n" + get_stmt_list(count)  # random.choice(["", get_stmt_list(count)])


# Functions to return statements


def get_while():
    # if if_while_limit_reached():
    #     return ""
    # return "while " + get_expr() + " do\n" + get_stmt_list(0) + "\nend"
    return "while " + get_expr() + "do" + get_stmt_list(1)


def get_if():
    if if_while_limit_reached():
        return ""
    return "if " + get_expr() + " then\n" + get_stmt_list(0) + "else " + get_stmt_list(0) + "\nend"


def get_assign():
    return get_id() + " = " + get_expr()


def get_input():
    return "input " + get_id()


def get_print():
    return "print " + random.choice([get_str(), get_expr()])


# Functions to return strings, id's, digits and comments
def get_str():
    return "\"" + get_id() + "\""


def get_id():
    output = ""
    alpha_char = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num_char = "0123456789"
    length = random.randint(1, 10)
    output = alpha_char[random.randint(0, 52)]
    for i in range(0, length):
        char_type = random.randint(1, 2)
        if char_type == 1:
            output = output + alpha_char[random.randint(0, 52)]
        else:
            output = output + num_char[random.randint(0, 9)]
    return output


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


# Driver
def prot_fuzzer():
    return get_stmt_list(0)

    # Break up the keywords into categories and make an if for each one. Structure each one appropriately.


# if __name__ == "__main__":
print(prot_fuzzer())
