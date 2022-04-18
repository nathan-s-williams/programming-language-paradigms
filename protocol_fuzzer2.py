import random

select_keywords = ["then", "else", "end"]
loop_keywords = ["while", "do", "for", "end"]
operators = ["+", "-", "*", "/", "%", "not", "("]
logical_operators = ["<", ">", "<=", ">=", "==", "!=", "and", "or"]
io_keywords = ["print", "get"]

value = ["(", "not", "-"]
v_expr = [">", ">=", "<", "<=", "==", "!="]
f_expr = ["*", "/", "%"]
t_expr = ["+", "-"]
b_expr = ["and", "or"]

def gen_code():
    fuzz = ""
    length = random.randint(1, 5)
    for i in range(0, length):
        choice = random.randint(1, 5)
        if choice <= 3:
            fuzz = fuzz + std_cmd(choice, fuzz)
        elif choice == 4:
            if_length = random.randint(1, 3)
            fuzz = fuzz + "if " + get_expr() + " then\n"
            for y in range(0, if_length):
                sub_choice = random.randint(1, 3)
                fuzz = fuzz + std_cmd(sub_choice, fuzz) + "\n"
            fuzz = fuzz + "else\n"
            for y in range(0, if_length):
                sub_choice = random.randint(1, 3)
                fuzz = fuzz + std_cmd(sub_choice, fuzz) + "\n"
            fuzz = fuzz + "end;\n"

    return fuzz


def std_cmd(choice, fuzz):
    if choice == 1:
        fuzz = fuzz + "print "
        sub_choice = random.randint(1, 2)
        if sub_choice == 1:
            fuzz = fuzz + get_str() + ";\n"
        else:
            fuzz = fuzz + get_expr() + ";\n"
    elif choice == 2:
        fuzz = fuzz + "get " + get_id() + ";\n"
    elif choice == 3:
        fuzz = fuzz + get_id() + " = " + get_expr() + ";\n"
    return fuzz

# Expressions
def get_expr():
    return get_n_expr() + " " + get_b_expr()


def get_b_expr():
    choice = random.randint(0, 8)
    if choice > 1:
        return ""
    return b_expr[choice] + " " + get_n_expr()


def get_n_expr():
    return get_term() + " " + get_t_expr()


def get_t_expr():
    choice = random.randint(0, 8)
    if choice > 1:
        return ""
    return t_expr[choice] + " " + get_n_expr()


def get_term():
    return get_factor()


def get_f_expr():
    choice = random.randint(0, 6)
    if choice > 2:
        return ""
    return f_expr[choice] + " " + get_term()


def get_factor():
    return get_value(False) + " " + get_v_expr()


def get_v_expr():
    choice = random.randint(0, 10)
    if choice > 5:
        return "" + get_f_expr()  # Call f_expr because there is no logical expression
    return v_expr[choice] + " " + get_value(False)


def get_value(term):
    if term:
        choice = random.randint(0, 1)
        if choice == 0:
            return get_id()
        else:
            return get_digit()
    else:
        choice = random.randint(0, 4)
        if choice == 0:
            return value[choice] + get_expr() + ")"
        elif choice == 3:
            return get_id()
        elif choice == 4:
            return get_digit()
        else:
            return value[choice] + get_value(True)


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
    num_char = "0123456789"
    length = random.randint(1, 10)
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


print(gen_code())
