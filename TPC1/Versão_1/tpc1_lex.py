import ply.lex as lex
import re

# * Frase Valida + [1 ; 3 ] [ 4 ; 6 ] . 

import ply.lex as lex

tokens = ['NUM', 'PONTO_VIRGULA', 'MAIS', 'MENOS', 'PONTO', 'PRETO_ABRIR', 'PRETO_FECHAR']

t_NUM = r'\d+(\.\d+)?'
t_PONTO_VIRGULA = r';'
t_MAIS = r'\+'
t_MENOS = r'\-'
t_PONTO = r'\.'
t_PRETO_ABRIR = r'\['
t_PRETO_FECHAR = r'\]'

t_ignore = ' \t\n\r' 

def t_error(t):
    print('CARÁTER ILEGAL:', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()



#while True:
#    data = input("Enter expression (or 'STOP' to exit): ")
#    if data == 'STOP':
#        break
#
#    lexer.input(data)
#
#    while True:
#        tok = lexer.token()
#        if not tok:
#            break  # No more input
#        else:
#            print(tok)
