# This lexer is used to parse the tokens and lexemes of a given programming language. It includes at least
# one additional change to the program language's original requirements.
# Created by Nathan Williams
import sys

# Keywords
keywords = ["print", "get", "if", "then", "else", "end", "while", "do", "end", "and", "or", "not", "for"]
line = 1

# Lexemes and Tokens
SEMICOLON = 0
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
FLOAT = 16
ID = 17
KEYWORD = 18
STRING = 19
END_OF_INPUT = 20
INPUT_ERROR = 21
LEFT_BRACKET = 22
RIGHT_BRACKET = 23
COMMA = 24


# Add a newline counter to print the location of errors when they occur.
def new_line():
    global line
    line = line + 1


# Error function that prints the line number where the error occurred and msg to the user.
def lex_error(error_msg):
    return INPUT_ERROR, "Error on line " + str(line) + ": " + error_msg


# Clean spaces and newlines between symbols. Also cleans the comments located in the code.
def clean_space_comment(input):
    i = 0
    while i < len(input) and (input[i].isspace() or input[i] == "/" or input[i] == "\n"):
        i = i + 1
        if input[i - 1] == "\n":  # Add newline when \n is encountered.
            new_line()
        elif input[i - 1] == "/":
            if i >= len(input) or input[i] != "/":  # Check for comment.
                i = i - 1
                break
            else:
                while i < len(input) and input[i] != "\n":  # Consume all input after // to the next \n character.
                    i = i + 1
                new_line()
    return input[i:]


# Lex INT tokens
def lex_int(input):
    i = 0
    decimal_count = 0
    lexeme_num = ""
    if input[i] == "-" or input[i] == "+":  # If preceded by +/- then print - but consume +.
        if input[i] == "-":
            lexeme_num = lexeme_num + input[i]
        i = i + 1
    # Continue appending lexeme while i < lenth of input and there is a digit or period.
    while i < len(input) and (input[i].isdigit() or input[i] == "."):
        if input[i] == ".":  # Count the number of decimals appended
            decimal_count = decimal_count + 1
        lexeme_num = lexeme_num + input[i]
        i = i + 1
    if decimal_count > 1:  # If decimals are > 1 then output input error.
        return lex_error("Unable to read float value."), input[i + 1:]
    elif decimal_count == 1:  # If only one decimal then return FLOAT with lexeme.
        return (FLOAT, lexeme_num), input[i:]
    else:  # If no decimal then return INT
        return (INT, lexeme_num), input[i:]


# Lex ID and Keywords
def lex_id_or_keyword(input):
    i = 0
    lexeme_id = ""
    while i < len(input) and (input[i].isalpha() or input[i].isdigit() or input[i] == "_"):
        lexeme_id = lexeme_id + input[i]  # non-digit is found.
        i = i + 1
    for iterator in keywords:
        if iterator == lexeme_id:
            return (KEYWORD, lexeme_id), input[i:]
    return (ID, lexeme_id), input[i:]


# Lex String
def lex_string(input):
    i = 0
    lexeme_string = ""
    if input[i] == "\"":  # Consumer beginning quotation mark.
        i = i + 1
    while i < len(input) and input[i] != "\"":  # Continue lexeme until EOF or ending quotation is found.
        i = i + 1
        if input[i - 1] == "\\":
            i = i + 1
            if input[i - 1] == "\\":  # Skip escape character and add \.
                lexeme_string = lexeme_string + "\\"
            elif input[i - 1] == "\"":  # Skip escape character and add ".
                lexeme_string = lexeme_string + "\""
            elif input[i - 1] == "n":  # Skip escape character and add newline.
                lexeme_string = lexeme_string + "\n"
            elif input[i - 1] == "t":  # Skip escape character and add tab.
                lexeme_string = lexeme_string + '\t'
            else:  # Skip escape character and add next one.
                lexeme_string = lexeme_string + input[i - 1]
        else:
            lexeme_string = lexeme_string + input[i - 1]
    if i >= len(input) and input[i - 1] != "\"":  # Output error if no ending quotation is found.
        return lex_error("Missing ending quotation. Cannot process remaining input."), input[i:]
    else:
        return (STRING, lexeme_string), input[i + 1:]


# Lex Input
def lex(input):
    input = clean_space_comment(input)  # Clean spaces, comments and newlines.
    i = 0
    if i >= len(input):  # Return END_OF_INPUT if EOF found. Otherwise, return token else unexpected char error.
        return (END_OF_INPUT, None), []
    elif input[i] == ";":
        return (SEMICOLON, None), input[i + 1:]
    elif input[i] == ",":
        return (COMMA, None), input[i + 1:]
    elif input[i] == "*":
        return (MULTIPLICATION, None), input[i + 1:]
    elif input[i] == "%":
        return (MODULUS, None), input[i + 1:]
    elif input[i] == "(":
        return (LEFT_PAREN, None), input[i + 1:]
    elif input[i] == ")":
        return (RIGHT_PAREN, None), input[i + 1:]
    elif input[i] == "[":
        return (LEFT_BRACKET, None), input[i + 1:]
    elif input[i] == "]":
        return (RIGHT_BRACKET, None), input[i + 1:]
    elif input[i] == "/":
        return (DIVISION, None), input[i + 1:]
    elif input[i] == "!":
        i = i + 1
        if i < len(input) and input[i] == "=":
            return (NOT_EQUAL, None), input[i + 1:]
        else:  # Return error if = does not follow !.
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
            return lex_int(input)
        elif i < len(input) and input[i - 1] == "+":
            return (PLUS, None), input[i:]
        else:
            return (MINUS, None), input[i:]
    elif input[i].isdigit():
        return lex_int(input)
    elif input[i].isalpha() or input[i] == "_":
        return lex_id_or_keyword(input)
    elif input[i] == "\"":
        return lex_string(input)
    else:  # Return unexpected character error as no matching token was found.
        return lex_error("Unexpected Character \'" + input[i] + "\'."), input[i + 1:]


# Driver program
# Read user input from the terminal or by a file.
# Output is formatted as string to incorporate newlines and tabs for STRINGS.
if __name__ == "__main__":
    input_method = input("Please choose which mode you would like the lexer to run. Console(1) or File(2): ")
    while len(input_method) > 1 or (input_method != "1" and input_method != "2"):
        input_method = input("Invalid input. Please choose which mode you would like the lexer to run. Console(1) or "
                             "File(2): ")
    input_method = int(input_method)
    if input_method == 2:
        while True:
            try:
                path = input("Input file path: ")
                if path == "-1":
                    sys.exit("Lexer program ended successfully.")
                file = open(path, "r")
                break
            except Exception:
                print("Unable to find file. Please ensure the path name is correct or type \"-1\" to exit the program.")
        userInput = list(file.read())
        file.close()
    else:
        userInput = list(sys.stdin.read())
    adjInput = lex(userInput)
    while adjInput[0][0] != EOFError and adjInput[0][0] != END_OF_INPUT:
        print(":\t".join([str(v) for v in adjInput[0]]))
        adjInput = lex(adjInput[1])
    print(":\t".join([str(v) for v in adjInput[0]]))

