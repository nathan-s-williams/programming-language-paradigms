# Lexer program used to identify lexemes and tokens
import sys

keywords = ["print", "get", "if", "then", "else", "end", "while", "do", "end", "and", "or", "not", "for"]
line = 1

SEMICOLON = 00
ASSIGN = 1
PLUS = 2
MINUS = 3
MULTIPLICATION = 4
DIVISION = 5
MODULUS = 6
GT = 7
GT_OR_EQUAL = 8
LT = 9
LT_OR_EQUAL = 10
EQUAL = 11
NOT_EQUAL = 12
LEFT_PAREN = 13
RIGHT_PAREN = 14
INT = 15
ID = 16
KEYWORD = 17
STRING = 18
END_OF_INPUT = 19
INPUT_ERROR = 20


def new_line():
    global line
    line = line + 1


def lex_error(error_msg):
    return INPUT_ERROR, "Error on line " + str(line) + ": " + error_msg


def clean_space_comment(input):
    i = 0
    while i < len(input) and (input[i].isspace() or input[i] == "/" or input[i] == "\n"):
        i = i + 1
        if input[i - 1] == "\n":
            new_line()
        elif input[i - 1] == "/":
            if i >= len(input) or input[i] != "/":
                break
            else:
                while i < len(input) and input[i] != "\n":
                    i = i + 1
                new_line()
    return input[i:]


def lex_int(input):
    i = 0
    lexeme_int = ""
    while i < len(input) and input[i].isdigit():
        lexeme_int = lexeme_int + input[i]
        i = i + 1
    return (INT, lexeme_int), input[i:]


def lex_id_or_keyword(input):
    i = 0
    lexeme_id = ""
    while i < len(input) and (input[i].isalpha() or input[i].isdigit()):
        lexeme_id = lexeme_id + input[i]
        i = i + 1
    for iterator in keywords:
        if iterator == lexeme_id:
            return (KEYWORD, lexeme_id), input[i:]
    return (ID, lexeme_id), input[i:]


def lex_string(input):
    i = 0
    lexeme_string = ""
    if input[i] == "\"":
        i = i + 1
    while i < len(input) and input[i] != "\"":
        i = i + 1
        if input[i - 1] == "\\":
            i = i + 1
            if input[i - 1] == "\\":
                lexeme_string = lexeme_string + "\\"
            elif input[i - 1] == "\"":
                lexeme_string = lexeme_string + "\""
            elif input[i - 1] == "n":
                lexeme_string = lexeme_string + "\n"
            elif input[i - 1] == "t":
                lexeme_string = lexeme_string + '\t'
            else:
                lexeme_string = lexeme_string + input[i]
        else:
            lexeme_string = lexeme_string + input[i - 1]
    return (STRING, lexeme_string), input[i + 1:]


def lex(input):
    input = clean_space_comment(input)
    i = 0
    if i >= len(input):
        return (END_OF_INPUT, None), []
    elif input[i] == ";":
        return (SEMICOLON, None), input[i + 1:]
    elif input[i] == "*":
        return (MULTIPLICATION, None), input[i + 1:]
    elif input[i] == "%":
        return (MODULUS, None), input[i + 1:]
    elif input[i] == "(":
        return (LEFT_PAREN, None), input[i + 1:]
    elif input[i] == ")":
        return (RIGHT_PAREN, None), input[i + 1:]
    elif input[i] == "*":
        return (MULTIPLICATION, None), input[i + 1:]
    elif input[i] == "/":
        return (DIVISION, None), input[i + 1:]
    elif input[i] == "!":
        i = i + 1
        if i < len(input) and input[i] == "=":
            return (NOT_EQUAL, None), input[i:]
        else:
            return lex_error("Unexpected Character \'" + input[i] + "\' after \'!\'. Expect \'=\'"), input[i:]
    elif input[i] == "<":
        i = i + 1
        if i < len(input) and input[i] == "=":
            return (LT_OR_EQUAL, None), input[i + 1:]
        else:
            return (LT, None), input[i:]
    elif input[i] == ">":
        i = i + 1
        if i < len(input) and input[i] == "=":
            return (GT_OR_EQUAL, None), input[i + 1:]
        else:
            return (GT, None), input[i:]
    elif input[i] == "=":
        i = i + 1
        if i < len(input) and input[i] == "=":
            return (EQUAL, None), input[i + 1:]
        else:
            return (ASSIGN, None), input[i:]
    elif input[i] == "+" or input[i] == "-":
        i = i + 1
        if i < len(input) and input[i].isdigit():
            return (INT, lex_int(input)), input[i + 1:]
        elif i < len(input) and input[i] == "+":
            return (PLUS, None), input[i:]
        else:
            return (MINUS, None), input[i:]
    elif input[i].isdigit():
        return lex_int(input)
    elif input[i].isalpha() or input[i] == "_":
        return lex_id_or_keyword(input)
    elif input[i] == "\"":
        return lex_string(input)
    else:
        return lex_error("Unexpected Character \'" + input[i] + "\'."), input[i + 1:]


if __name__ == "__main__":
    userInput = list(sys.stdin.read())
    adjInput = lex(userInput)
    while adjInput[0][0] != EOFError and adjInput[0][0] != END_OF_INPUT:
        print(":\t".join([str(v) for v in adjInput[0]]))
        adjInput = lex(adjInput[1])
print(":\t".join([str(v) for v in adjInput[0]]))