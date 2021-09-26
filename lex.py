import re

#reserved words

reserved = {
    'Program' : 'PROGRAM',
    'VARS' : 'VARS',
    'main' : 'MAIN',
    'function' : 'FUNCTION',
    'void' : 'VOID',
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    'str' : 'STR',
    'bool' : 'BOOL',
    'return' : 'RETURN',
    'read' : 'READ',
    'write' : 'WRITE',
    'if' : 'IF',
    'true': 'TRUE',
    'false': 'FALSE',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'do' : 'DO',
    'for' : 'FOR',
    'to' : 'TO'
}

#tokens

tokens = [
    'ID',
    'PTCOMA',
    'APAR',
    'CPAR',
    'ALLA',
    'CLLA',
    'COMA',
    'ACOR',
    'CCOR',
    'IGUAL',
    'DOSPNTS',
    'STRING',
    'MAS',
    'MENOS',
    'DIV',
    'POR',
    'CTEI',
    'CTEF',
    'CTEC',
    'MAYQ',
    'MENQ',
    'MAYI',
    'MENI',
    'IGUALIGUAL',
    'DIF'
] + list(reserved.values())


#types
t_ignore = "[\t '' \n]"

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

t_PTCOMA = r'\;'
t_APAR = r'\('
t_CPAR = r'\)'
t_ALLA = r'\{'
t_CLLA = r'\}'
t_COMMA = r'\,'
t_ACOR = r'\['
t_CCOR = r'\]'
t_IGUAL = r'\='
t_DOSPNTS = r'\:'
t_STRING = r'\".*\"'
t_MAS = r'\+'
t_MENOS = r'\-'
t_DIV = r'\/'
t_POR = r'\*'
t_CTEC = r"\'.\'"
t_MAYQ = r'\>'
t_MENQ = r'\<'
t_MAYI = r'\>\='
t_MENI = r'\<\='
t_IGUALIGUAL = r'\=\='
t_DIF = r'\!\='

def t_CTEF(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_CTEI(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#Build lexer
import ply.lex as lex

#Gramatic rules

def p_empty(t):
    'empty :'
    pass

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

def p_program(t):
    'program : PROGRAM ID PTCOMA varss funcs MAIN APAR CPAR ALLA estatutos CLLA'
    print('Código aceptado')

def p_varss(t):
    '''varss : VARS vars
             | empty
    '''

def p_vars(t):
    '''vars : tipo DOSPNTS ID varsp vars
            | empty
    '''

def p_varsp(t):
    '''varsp : PTCOMA
             | COMA varsp
             | ACOR CTEI CCOR varsp
    '''

def p_funcs(t):
    '''funcs : FUNCION funcsp ID APAR params CPAR PTCOMA varss ALLA estatutos CLLA funcs
             | empty
    '''

def p_funcsp(t):
    '''funcsp : VOID
              | tipo
    '''

def p_estatutos(t):
    '''estatutos : asig estatutop
                 | llamada estatutop
                 | return estatutop
                 | lectura estatutop
                 | escritura estatutop
                 | cond estatutop
                 | while estatutop
                 | for estatutop
                 | exp estatutop
    '''
    # ^ Aquí falta agregar lo que vayan a ser los estatutos especiales: media, moda, stddev, etc ...

def p_estatutop(t):
    '''estatutop : estatutos
                 | empty
    '''

def p_tipo(t):
    '''tipo : INT
            | FLOAT
            | CHAR
            | STR
            | BOOL
    '''
def p_params(t):
    '''params : tipo ID paramsp
              | empty
    '''

def p_paramsp(t):
    '''paramsp : COMA params
               | ACOR CCOR params
               | empty
    '''

def p_asig(t):
    '''asig : ID ididx IGUAL asigpp PTCOMA
    '''

def p_ididx(t):
    '''ididx : ACOR exp CCOR
             | empty
    '''

def p_asigpp(t):
    '''asigpp : exp
              | expbool
    '''

def p_llamada(t):
    '''llamada : ID APAR args CPAR PTCOMA
    '''

def p_args(t):
    '''args : ctes argsp
            | ID ididx argsp
            | exp argsp
            | expbool argsp
            | STRING argsp
            | CTEC argsp
    '''

def p_argsp(t):
    '''argsp : COMA
             | empty
    '''

def p_return(t):
    '''return : RETURNAPAR returnp CPAR PTCOMA
    '''

def p_returnp(t):
    '''returnp : exp
               | expbool
    '''

def p_lectura(t):
    '''lectura : READ APAR ID ididx lecturapp CPAR PTCOMA
    '''

def p_lecturapp(t):
    '''lecturapp : COMA
                 | empty
    '''

def p_escritura(t):
    '''escritura : WRITE APAR escriturap escriturapp CPAR PTCOMA
    '''

def p_escriturap(t):
    '''escriturap : STRING
                  | exp
                  | expbool
                  | CTEC
    '''

def p_escriturapp(t):
    '''escriturapp : COMA
                   | empty
    '''

def p_cond(t):
    '''cond : IF APAR condp CPAR THEN ALLA estatutos CLLA condpp
    '''
def p_condp(t):
    '''condp : expbool
             | TRUE
             | FALSE
    '''

def p_condpp(t):
    '''condpp : ELSE ALLA estatutos CLLA
              | empty
    '''

def p_while(t):
    '''while : WHILE APAR whilep CPAR DO ALLA estatutos CLLA
    '''

def p_whilep(t):
    '''whilep : expbool
             | TRUE
             | FALSE
    '''

def p_for(t):
    '''for : FOR ID ididx IGUAL exp TO exp DO ALLA estatutos CLLA
    '''

def p_exp(t):
    '''exp : termino expp
    '''

def p_expp(t):
    '''expp : MAS exp
            | MENOS exp
    '''

def p_termino(t):
    '''termino : factor terminop
    '''

def p_terminop(t):
    '''terminop : POR termino
                | DIV termino
    '''

def p_factor(t): 
    '''factor : APAR exp CPAR
              | factorp ctes
    '''

def p_factorp(t):
    '''factorp : MAS
               | MENOS
               | empty
    '''

def p_expbool(t):
    '''expbool : exp expboolp exp
    '''
def p_expboolp(t):
    '''expboolp : MAYQ
                | MENQ
                | MAYI
                | MENI
                | IGUALIGUAL
                | DIF
    '''

def p_ctes(t):
    '''ctes : ID
            | CTEI
            | CTEF
    '''

import ply.yacc as yacc
parser = yacc.yacc()

f = open("./pass.txt", "r")
input = f.read()
print(input)
parser.parse(input)