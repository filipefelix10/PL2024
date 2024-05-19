import sys
import io
import re
import ply.lex as lex

tokens = (
    'SELECT',
    'ID',
    'FROM',
    'WHERE',
    'NUMBER',
)

literals = [';', ',', '=', '(', ')', '<', '>', '!', '+', '-', '*', '/']

def t_SELECT(t):
    r'SELECT'
    return t

def t_FROM(t):
    r'FROM'
    return t

def t_WHERE(t):
    r'WHERE'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

entrada = """SELECT id, name FROM table WHERE id = 10;"""

def parse(entrada):
    lexer.input(entrada)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

parse(entrada)

