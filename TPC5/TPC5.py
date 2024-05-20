import sys
import io
import re
import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'LISTAR',
    'SELECIONAR',
    'MOEDA',
    'SAIR',
    'NUMBER',
)

literals = [';', ',', '=', '(', ')', '<', '>', '!', '+', '-', '*', '/']

def t_LISTAR(t):
    r'(?i:listar)'
    return t

def t_SELECIONAR(t):
    r'(?i:selecionar)'
    return t

def t_MOEDA(t):
    r'(?i:moeda)'
    return t

def t_SAIR(t):
    r'(?i:sair)'
    return t

def t_NUMBER(t):
    r'\d+e'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# GIC

"""
SHOP : comandos
comandos : comandos comando
         | comando
comando : LISTAR
        | SELECIONAR
        | MOEDA 
        | NUMBER
        | SAIR
        """


def p_comandos(p):
    """SHOP : comandos comando
            | comando"""
    pass

entrada = """
moeda 1e,10e,5e
listar
sair
"""

def parse(entrada):
    lexer.input(entrada)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

parse(entrada)

