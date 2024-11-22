# lexer.py
import ply.lex as lex

# List of token names
tokens = [
    'LET', 'BE', 'ID', 'NUMBER', 'SHOUT', 'IF', 'ELSE',
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE',
    'LESS','GREATER' , 'LBRACE', 'RBRACE', 'STRING', 'NEWLINE'
]

# Token definitions (regex)
t_LET = r'let'
t_BE = r'be'
t_SHOUT = r'shout'
t_IF = r'if'
t_ELSE = r'else'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LESS = r'<'
t_GREATER = r'>'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_STRING = r'"[^"]*"'

# Handle newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# Identifiers and numbers
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Convert to integer
    return t

# Ignore spaces and tabs
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Oops! I don't recognize '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
