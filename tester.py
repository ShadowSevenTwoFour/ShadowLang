from my_lexer import lexer
from my_parser import parser

if __name__ == "__main__":
    with open("examples/test.lang", "r") as file:
        code = file.read()
    
    print("Lexing...")
    lexer.input(code)
    for token in lexer:
        print(token)

    print("\nParsing...")
    ast = parser.parse(code)
    print(ast)
