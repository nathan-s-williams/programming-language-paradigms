import sys
import lexer


def error(msg):
    print("Error on line " + str(lexer.line) + ": " + msg)


def lex():
    global lex_input
    global nextToken
    (nextToken, lex_input) = lexer.lex(lex_input)
    if nextToken[0] == lexer.INPUT_ERROR:
        error("Error in input.")


def parse_prog():
    return parse_stmt_list()


def parse_stmt_list():
    result = parse_stmt()
    if result:
        if nextToken != lexer.END_OF_INPUT:
            result = parse_stmt_list()
    return True


def parse_stmt():
    global nextToken
    if nextToken[1] == "print":
        lex()
        if nextToken[0] == lexer.STRING:
            return True
        else:
            return parse_expr()
    elif nextToken[1] == "get":
        lex()
        if nextToken[0] == lexer.ID:
            return True
    elif nextToken[0] == lexer.ID:
        lex()
        if nextToken[0] == lexer.ASSIGN:
            lex()
            return parse_expr()
    elif nextToken[1] == "if":
        lex()
        if parse_expr():
            lex()
            if nextToken[1] == "then":
                lex()
                if parse_stmt_list():
                    lex()
                    if nextToken[1] == "else":
                        lex()
                        if parse_stmt_list():
                            lex()
                            if nextToken[1] == "end":
                                return True
    elif nextToken[1] == "while":
        lex()
        if parse_expr():
            lex()
            if nextToken[1] == "do":
                lex()
                if parse_stmt_list():
                    lex()
                    if nextToken[1] == "end":
                        return True
    elif nextToken[1] == "for":    # Finish for loop
        print("for loop")
    elif nextToken[0] == lexer.INPUT_ERROR:  # Input error found.
        return False
    return False    # Parser cannot parse input. Return False.


def parse_expr():
    return


lex_input = list(sys.stdin.read())
lex()
if parse_prog():
    print("This program is correct.")
else:
    print("This program is not correct.")
