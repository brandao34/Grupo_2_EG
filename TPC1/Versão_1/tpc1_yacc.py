from tpc1_lex import tokens, lexer,re
import ply.yacc as yacc

# TOKENS = ['NUM', 'PONTO_VIRGULA', 'MAIS', 'MENOS', 'PONTO', 'PRETO_ABRIR', 'PRETO_FECHAR']

#NT = { S, Is, RI, I }
#P = { p1: Sentence  : Signal Intervals '.'
#         p6: Signal : '+'
#parser.sentido = 1
#         p7: Signal : '-'		
#parser.sentido = -1
#         p2: Intervals : Interval RemainingIntervals
#         p3: RemainingIntervals : 
#         p4: RemainingIntervals : Interval RemainingIntervals
#         p5: Interval  : '[' num ';' num ']'   
#		CC1:    p[4] > p[2]  &
#		CC2:    p[2] >= parser.anterior
#		parser.anterior = p[4]
#		parser.erro = not (CC1) or not (CC2)
#
#
#*###############################################################
#
# Z : Sentence '$' 
# Sentence : MAIS Intervals PONTO
#          | MENOS Intervals PONTO
#
# Intervals : Interval RemainingIntervals

# RemainingIntervals : Interval RemainingIntervals
#                    | 

# Interval : PRETO_ABRIR NUM PONTO_VIRGULA NUM PRETO_FECHAR
#
diferenca  = 0 
erro = True

def p_1(p): 

    'Z : Sentence  '
    p[0] = f'{p[1]}'
    if (erro):
        print(f"Frase Correta\nCom um intervalo de: {diferenca}")

def p_2(p): 
    '''Sentence : MAIS Intervals PONTO'''
    intervals = p[2]  
    
    intervals = [
    [float(val) for val in interval.split(';')] for interval in intervals]
    print(intervals)
    if all(intervals[i][0] <= intervals[i + 1][0] and intervals[i][1] <= intervals[i + 1][1] for i in range(len(intervals) - 1)):
        global diferenca 
        diferenca =  intervals[-1][1]   -  intervals[0][0] 
        p[0] = f'{p[1]}{p[2]}{p[3]}'
    else:
        print("Erro: Intervalos devem estar em ordem crescente")
        global erro
        erro = False
        p[0] = None


def p_2_1(p): 
    '''Sentence :  MENOS Intervals PONTO '''
    intervals = p[2]  

    intervals = [
    [float(val) for val in interval.split(';')] for interval in intervals]

    if all(intervals[i][0] >= intervals[i + 1][0] and intervals[i][1] >= intervals[i + 1][1] for i in range(len(intervals) - 1)):
        global diferenca
  
        diferenca = intervals[0][0] -  intervals[-1][1] 
        p[0] = f'{p[1]}{p[2]}{p[3]}'
    else:
        print("Erro: Intervalos devem estar em ordem decrescente")
        p[0] = None

def p_3(p): 
    'Intervals : Interval RemainingIntervals'
    p[0] = [p[1]] + p[2]


def p_4(p): 
    '''  RemainingIntervals : Interval RemainingIntervals
                            | '''
    
    if len(p) > 1: 
       p[0] = [p[1]] + p[2]
    else:
        p[0] = []


def p_5(p): 
    'Interval : PRETO_ABRIR NUM PONTO_VIRGULA NUM PRETO_FECHAR'
    p[0] = f'{p[2]}{p[3]}{p[4]}'



def p_error(p):
    print("Erro sintático no input!")
    print(p)

parser = yacc.yacc()


while True:
    entrada = input("Pressa 's' para terminar:\n>")

    if entrada.lower() == 's':
        break
    else:
        conversor = parser.parse(entrada)
        diferenca = 0 
        erro = True