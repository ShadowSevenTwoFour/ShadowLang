# parser.py
import ply.yacc as yacc
from my_lexer import tokens

# AST Nodes
class Program:
    def __init__(self, statements):
        self.statements = statements

class LetNode:
    def __init__(self, var_name, value):
        self.var_name = var_name
        self.value = value

class PrintNode:
    def __init__(self, value):
        self.value = value

class IfNode:
    def __init__(self, condition, then_block, else_block=None):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

# Grammar rules
def p_program(p):
    '''program : statements'''
    p[0] = Program(p[1])

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    p[0] = p[1] if len(p) == 2 else p[1] + [p[2]]

def p_statement_let(p):
    '''statement : LET ID BE expression NEWLINE'''
    p[0] = LetNode(p[2], p[4])

def p_statement_shout(p):
    '''statement : SHOUT STRING NEWLINE'''
    p[0] = PrintNode(p[2])

def p_statement_if(p):
    '''statement : IF expression LBRACE statements RBRACE
                 | IF expression LBRACE statements RBRACE ELSE LBRACE statements RBRACE'''
    if len(p) == 6:
        p[0] = IfNode(p[2], p[4])
    else:
        p[0] = IfNode(p[2], p[4], p[8])

def p_expression(p):
    '''expression : NUMBER
                  | ID
                  | expression PLUS expression
                  | expression LESS expression'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])  # Operator, left operand, right operand

def p_error(p):
    print("Yikes! Something doesn't add up.")

# Build the parser
parser = yacc.yacc()
