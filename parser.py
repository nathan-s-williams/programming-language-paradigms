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
    if nextToken == "print":
        lex()
        if nextToken[0] == lexer.STRING:
            return True
        else:
            return parse_expr()
    elif nextToken == "input":
        pass
    elif nextToken == "assign":
        pass
    elif nextToken == "assign":
        pass
    elif nextToken == "if":
        pass
    elif nextToken == "while":
        pass
    elif nextToken == "for":
        pass
    else:
        return False


def parse_expr():
    pass

lex_input = list(sys.stdin.read())
lex()
parse_prog()
