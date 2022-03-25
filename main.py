# This is the Chapter 3 example for denotational semantics
# Format is using a pair ('non-terminal or node name like <prog>/<cmd>', 'list of nodes')
#   If list of nodes is empty, then it is a leaf node.
#   Supposed to represent a tree.
# Prints out the translation

def translate_prog(tree):
    if len(tree[1]) == 1:  # The RHS 1 represents the rule starting at <prog>
        # <cmd>; rule where first [1] is <prog> and second [0] is <cmd>
        translate_cmd(tree[1][0])
    else:
        # <cmd>; <prog> where first [1] is <prog> and second [0] is <cmd>, [1] is ";" and [2] is <prog>
        translate_cmd(tree[1][0])
        translate_prog(tree[1][2])


def translate_cmd(tree):
    if tree[1][0] == "get":
        print("printf(\"Enter Number: \")")
        print(tree[1][1] + " = readInt")  # This is the name of the lexeme which represents ID
    elif tree[1][0] == "print":
        print("printf(\"%d\\\n\", " + translate_val(tree[1][1]) + ")")
    elif tree[1][0] == "sum":
        print(tree[1][3] + " = " + translate_sum(
            tree[1][1]))  # sum followed by val_list followed by arrow followed by ID, so it's the 4th element [3]
    elif tree[1][0] == "product":
        print(tree[1][3] + " = " + translate_product(tree[1][1]))
    elif tree[1][0] == "modulo":
        print("TMP1 = " + translate_val(tree[1][1]))
        print("TMP2 = " + translate_val(tree[1][2]))
        print(tree[1][4] + " = TMP1 % TMP2")
    elif tree[1][0] == "divide":
        print("TMP1 = " + translate_val(tree[1][1]))
        print("TMP2 = " + translate_val(tree[1][2]))
        print(tree[1][4] + " = TMP1 / TMP2")
    elif tree[1][0] == "if":
        print("if(" + translate_val(tree[1][2]) + " " + tree[1][1] + " 0) {")
        translate_prog(tree[1][3])
        print("}")
    elif tree[1][0] == "while":
        print("while(" + translate_val(tree[1][2]) + " " + tree[1][1] + " 0) {")
        translate_prog(tree[1][3])
        print("}")


def translate_val(tree):
    if len(tree[1]) == 2:
        return "-" + tree[1][1]
    else:
        return tree[1][0]


def translate_sum(tree):
    if len(tree[1]) == 1:
        return translate_val(tree[1][0])
    else:
        return translate_val(tree[1][0]) + " + " + translate_sum(tree[1][2])


def translate_product(tree):
    if len(tree[1]) == 1:
        return translate_val(tree[1][0])
    else:
        return translate_val(tree[1][0]) + " * " + translate_sum(tree[1][2])


if __name__ == "__main__":
    test = ("prog", ["cmd", ["get", "x"]])
        # ("prog", [("cmd", ["get", "x"]), ";", ("prog", [("cmd", ["get", "y"]), ";", ("prog", [("cmd", ["sum", ("val_list", [("val", ["x"]), ",", ()]), "->", "z"]), ";"()])])])
    translate_prog(test)
