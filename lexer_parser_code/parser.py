# This parser program parses files with code in our language specification. It will output if the program is
# correct or incorrect based on the syntax. It utilizes our lexer program to correctly parse through the code.
# Created by Nathan Williams

import sys
import lexer


nextToken = ""
if_while_flag = False

INPUT_ERROR = 0
FILE_EMPTY_ERROR = 1


def error(msg, err_type):
    if err_type == INPUT_ERROR:
        print("\nError on line " + str(lexer.line) + ": " + msg)
    elif err_type == FILE_EMPTY_ERROR:
        print("\nFile warning: " + msg)
    else:
        print("\nError: Unknown reason.")


def lex():
    global lex_input
    global nextToken
    (nextToken, lex_input) = lexer.lex(lex_input)
    if nextToken[0] == lexer.INPUT_ERROR:
        error("Error in input.", INPUT_ERROR)


def parse_prog():
    return parse_stmt_list()


def parse_stmt_list():
    global nextToken
    result = parse_stmt()
    if result:
        if nextToken[0] == lexer.SEMICOLON:
            lex()
        if nextToken[1] == "else" or nextToken[1] == "end":
            if not if_while_flag:
                result = False
            return result
        if nextToken[0] != lexer.END_OF_INPUT:
            result = parse_stmt_list()
    return result


def parse_stmt():
    global nextToken
    global if_while_flag
    if nextToken[1] == "print":
        lex()
        if nextToken[0] == lexer.STRING:
            lex()
            return True
        else:
            return parse_expr()
    elif nextToken[1] == "get":
        lex()
        if nextToken[0] == lexer.ID:
            lex()
            return True
    elif nextToken[0] == lexer.ID:
        lex()
        if nextToken[0] == lexer.ASSIGN:
            lex()
            if nextToken[0] == lexer.LEFT_BRACKET:
                lex()
                if parse_int_array():
                    if nextToken[0] == lexer.RIGHT_BRACKET:
                        lex()
                        return True
            else:
                return parse_expr()
    elif nextToken[1] == "if":
        if_while_flag = True  # Start the if execution
        lex()
        if parse_expr():
            if nextToken[1] == "then":
                lex()
                if parse_stmt_list():
                    if nextToken[1] == "else":
                        lex()
                        if parse_stmt_list():
                            if nextToken[1] == "end":
                                lex()
                                if_while_flag = False  # End the if execution
                                return True
    elif nextToken[1] == "while":
        if_while_flag = True  # Start the while execution
        lex()
        if parse_expr():
            if nextToken[1] == "do":
                lex()
                if parse_stmt_list():
                    if nextToken[1] == "end":
                        lex()
                        if_while_flag = True  # Start the while execution
                        return True
    elif nextToken[1] == "for":
        if_while_flag = True  # Start the for execution
        lex()
        if nextToken[0] == lexer.LEFT_PAREN:
            lex()
            if nextToken[0] == lexer.ID:
                lex()
                if nextToken[0] == lexer.ASSIGN:
                    lex()
                    if parse_expr():
                        if nextToken[0] == lexer.SEMICOLON:
                            lex()
                            if parse_expr():
                                if nextToken[0] == lexer.SEMICOLON:
                                    lex()
                                    if nextToken[0] == lexer.ID:
                                        lex()
                                        if nextToken[0] == lexer.ASSIGN:
                                            lex()
                                            if parse_expr():
                                                if nextToken[0] == lexer.RIGHT_PAREN:
                                                    lex()
                                                    if parse_stmt_list():
                                                        if nextToken[1] == "end":
                                                            lex()
                                                            if_while_flag = False  # Start the for execution
                                                            return True
    elif nextToken[0] == lexer.END_OF_INPUT:  # Reached end-of-input prematurely. Throw warning.
        if not if_while_flag:
            error("File empty.", FILE_EMPTY_ERROR)
        return True
    elif nextToken[0] == lexer.INPUT_ERROR:  # Input error found.
        lex()
        return False
    return False  # No match for parse_stmt(). Return False.


def parse_expr():
    return parse_n_expr() and parse_b_expr()


def parse_n_expr():
    return parse_term() and parse_t_expr()


def parse_b_expr():
    global nextToken
    if nextToken[1] == "and":
        lex()
        return parse_n_expr()
    elif nextToken[1] == "or":
        lex()
        return parse_n_expr()
    return True


def parse_term():
    return parse_factor() and parse_f_expr()


def parse_t_expr():
    global nextToken
    if nextToken[0] == lexer.PLUS:
        lex()
        return parse_n_expr()
    elif nextToken[0] == lexer.MINUS:
        lex()
        return parse_n_expr()
    return True


def parse_factor():
    return parse_value() and parse_v_expr()


def parse_f_expr():
    global nextToken
    if nextToken[0] == lexer.MULTIPLICATION:
        lex()
        return parse_term()
    elif nextToken[0] == lexer.DIVISION:
        lex()
        return parse_term()
    elif nextToken[0] == lexer.MODULUS:
        lex()
        return parse_term()
    return True


def parse_value():
    global nextToken
    if nextToken[0] == lexer.LEFT_PAREN:
        lex()
        if parse_expr():
            if nextToken[0] == lexer.RIGHT_PAREN:
                lex()
                return True
    elif nextToken[1] == "not":
        lex()
        return parse_expr()
    elif nextToken[0] == lexer.INT and nextToken[1][0] == "-":
        lex()
        return True
    elif nextToken[0] == lexer.ID:
        lex()
        return True
    elif nextToken[0] == lexer.INT:
        lex()
        return True
    elif nextToken[0] == lexer.FLOAT:
        lex()
        return True
    return False  # There must be a value or a function call at this level.


def parse_int_array():
    global nextToken
    if nextToken[0] == lexer.INT:
        lex()
        if nextToken[0] == lexer.COMMA:
            lex()
            return parse_int_array()
        else:
            return True
    return False


def parse_v_expr():
    global nextToken
    if nextToken[0] == lexer.GT:
        lex()
        return parse_value()
    elif nextToken[0] == lexer.GT_OR_EQUAL:
        lex()
        return parse_value()
    elif nextToken[0] == lexer.LT:
        lex()
        return parse_value()
    elif nextToken[0] == lexer.LT_OR_EQUAL:
        lex()
        return parse_value()
    elif nextToken[0] == lexer.EQUAL:
        lex()
        return parse_value()
    elif nextToken[0] == lexer.NOT_EQUAL:
        lex()
        return parse_value()
    return True


if __name__ == "__main__":
    while True:
        try:
            path = input("Input file path: ")
            if path == "-1":
                sys.exit("Parser program ended successfully.")
            file = open(path, "r")
            break
        except Exception:
            print("Unable to find file. Please ensure the path name is correct or type \"-1\" to exit the program.")
    lex_input = list(file.read())
    file.close()

    # lex_input = list(sys.stdin.read())
    lex()
    if parse_prog():
        print("\nThis program is correct.")
    else:
        print("\nThis program is not correct.")
