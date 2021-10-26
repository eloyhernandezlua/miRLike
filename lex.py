from os import popen
import re
import sys 

#********************************
#Global variables
mainFuncTable = {}
globalVariables = {}
localVariables = {}

currentScope = 'g'
currentType = ''
usedNamesGlobal = []
usedNamesLocal = []
PilaO = []
POoper = []
Ptipos = []
Cuadruplos = [] 
Consts = []
tablaConstantes = {}


ariops = ['+', '-', '*', '/']
relops = ['>', '<', '>=', '<=', '==', '!=']
logicops = ['&&', '||']


contGlobI = 2000 - 1
contGlobF = 5000 - 1
contGlobC = 9000 -1
contLocI = 12000 - 1
contLocF = 20000 - 1
contLocC = 28000 -1
contTempI = 30000 - 1 
contTempF = 32000 - 1
contTempC = 34000 -1
contTempB = 36000 - 1
contConstI = 38000 - 1
contConstF = 40000 - 1

#Definir objeto cuadruplo 
class Cuad:
    def __init__(self, op, dir1, dir2, recep) -> None:
        global Cuadruplos
        self.count = len(Cuadruplos)
        self.op = op 
        self.dir1 = dir1 
        self.dir2 = dir2
        self.recep = recep

#Operaciones para cuádrupolos <<-- aquí es al revés TODO
Ops = {
    '' : -1,
    '+' : 1,
    '-' : 2,
    '*' : 3,
    '/' : 4,
    "==" : 5,
    '<' : 6,
    '>' : 7,
    '<=' : 8,
    ' >=' : 9,
     '!=' : 10,
     '=' : 11,
     'print' : 12,
     'read' : 13,
     'goto' : 14,
     'gotoF' : 15,
     'gotoT' : 16
}

#**********
#Plan para manejar las vdirs ---> al 23/10
# --------------------------
# | globales int   | 2000  |
# | globlaes float | 5000  |
# | globales char  | 9000  |
# | locales int    | 12000 |
# | locales float  | 20000 |
# | locales char   | 28000 |
# | temp int       | 30000 |
# | temp float     | 32000 |
# | temp char      | 34000 | 
# | temp bool      | 36000 | 
# | const int      | 38000 |
# | const float    | 40000 |
# -------------------------- 



def getVdirCTE(v):
    global contConstF
    global contConstI
    if type(v) == int:
        contConstI += 1
        return contConstI
    elif type(v) == float:
        contConstF += + 1
        return contConstF
    else: 
        ERROR("type error", str(v))

 

#***************************
#Fucniones de  manejo semántico

def ERROR(tipo, at = ""):
    
    extra = ""

    if tipo == "funcion repetida":
        extra = "FUNCION EXISTENTE REPETIDA"
    elif tipo == "nombre repetido":
        extra = "ID DE PROGRAMA O VARIABLE REPETIDO"
    elif tipo == "invalid op":
        extra = "INVALID OPERATION, TYPE MISMATCH"
    elif tipo == "variable repetida":
        extra = "VARIABLE PREVIAMENTE DECLARADA"
    elif tipo == "mal tipo":
        extra = "TIPO DE DATO NO ACEPTADO"
    elif tipo == "tipos distintos":
        extra = "TYPE MISMATCH"
    elif tipo == "no existe":
        extra = "NO EXISTE"
    elif tipo == "no value":
        extra = "VARIABLE SIN VALOR"
    elif tipo == "no tipo":
        extra = "VARIABLE SIN TIPO"
    elif tipo == "type error":
        extra = "ERROR EN TIPO DE DATO"
    elif tipo == "invalid op":
        extra = "INVALID OPERATION"

    print("ERROR: " + extra + "\n @ --> " + at)
    sys.exit()


def insertToFuncTable(id, tipo, scope, vars):
    if id in mainFuncTable:
        ERROR("funcion repetida")
    elif id in usedNamesGlobal:
        ERROR("nombre repetido")
    else:   
        mainFuncTable[id] = {'tipo' : tipo, 'scope': scope, 'vars': vars}
        usedNamesGlobal.append(id)

def getVDirTemp(type):
    global contTempB
    global contTempC
    global contTempF
    global contTempI

    if type == 'int':
        contTempI += 1
        return contTempI
    elif type == 'float':
        contTempF += 1
        return contTempF
    elif type == 'char' : 
        contTempC += 1
        return contTempC 
    elif type == 'bool':
        contTempB += 1
        return contTempB


## Baila mi hija con el señor ## 

def isValidOp(tipo1, tipo2, op):
    #tener los tipos y operación que se quiere hacer para ver si el válida
    validate = str(str(tipo1)+str(tipo2)+str(op))

    #combinaciones válidas
    valids = [
        'intint=',
        'floatfloat=',
        'charchar=',
        'boolbool=',
        'intint+',
        'intint-',
        'intint*',
        'intint/',
        'intint>',
        'intint<',
        'intint>=',
        'intint<=',
        'intint==',
        'intint!=',
        'intfloat+',
        'intfloat-',
        'intfloat*',
        'intfloat/',
        'intfloat>',
        'intfloat<',
        'intfloat>=',
        'intfloat<=',
        'intfloat==',
        'intfloat!=',
        'floatfloat+',
        'floatfloat-',
        'floatfloat*',
        'floatfloat/',
        'floatfloat>',
        'floatfloat<',
        'floatfloat>=',
        'floatfloat<=',
        'floatfloat==',
        'floatfloat!=',
        'charchar==',
        'charchar!=',
        'stringstring==',
        'stringstring!=',
        'boolbool==',
        'boolbool!=',
        'boolbool&&',
        'boolbool||',
    ]
    if validate not in valids:
        ERROR("invalid op", validate)
    
    #regresar el tipo de la operacion
    if op in ariops:
        if tipo1 == 'int' and tipo2 == 'int':
            return 'int'
        elif tipo1 == 'float' and tipo2 == 'float':
            return 'float'
        elif (tipo1 == 'float' and tipo2 == 'int') or (tipo1 == 'int' and tipo2 == 'float'):
            return 'float'
    elif op in relops or op in logicops:
        return 'bool'
    else :
        ERROR("invalid op")


def getvDirVars(tipo, scope):
    if scope == 'g':
        if tipo == 'int': 
            global contGlobI
            contGlobI += 1
            return contGlobI + 1
        elif tipo == 'float':
            global contGlobF
            contGlobF += 1
            return contGlobF + 1
        elif tipo == 'char':
            global contGlobC
            contGlobC += 1
            return contGlobC + 1
    else:
        if tipo == 'int': 
            return contLocI + 1
        elif tipo == 'float':
            return contLocF + 1
        elif tipo == 'char':
            return contLocC + 1


def insertToVarTable(id, vDir, tipo):

    if vDir < 12000:
        if id in usedNamesGlobal:
            ERROR("nombre repetido", str(id + " " + tipo))
        if id in globalVariables:
            ERROR("variable repetida", id)
        globalVariables[id] = {'vDir': vDir, 'tipo': tipo}
        usedNamesGlobal.append(id)

    else:
        if id in usedNamesLocal:
            ERROR("nombre repetido", str(id + " " + tipo))
        if id in localVariables:
            ERROR("variable repetida", id)
        localVariables[id] = {'vDir':vDir, 'tipo': tipo}
        usedNamesLocal.append(id)
    

def validateTypes(tipo1, tipo2):
    if tipo1 != tipo2:
        ERROR("tipos distintos", str(tipo1 + " --- " + tipo2))

def getValType(val):

    if val in localVariables:
        return localVariables[val]['tipo']

    if val in globalVariables:
        return globalVariables[val]['tipo']

    if val in mainFuncTable:
        return mainFuncTable[val]['tipo']

    try: 
        int(val)
        return 'int'
    except:
        try:
            float(val)
            return 'float'
        except:
            try:
                chr(val)
                return 'char'
            except:
                try:
                    str(val)
                    return 'string'
                except:
                    try:
                        bool(val)
                        return 'bool'
                    except:
                        ERROR("mal tipo", val)
    

def fetchVDir(val):
    if val in localVariables:
        return localVariables[val]['vDir']
    elif val in globalVariables:
        return globalVariables[val]['vDir']
    elif val in tablaConstantes:
        return tablaConstantes[val]
    else :
        ERROR("no existe", val)

def asignar(val1, val2):
    if val1 not in localVariables and val1 not in globalVariables:
        ERROR("no existe", val1)
    tipoVal2 = getValType(val2)
    if currentScope == 'l':
        
        if val1 in localVariables:
            validateTypes(localVariables[val1]['tipo'], tipoVal2)
            localVariables[val1]['value'] = val2
        else: 
            validateTypes(globalVariables[val1]['tipo'], tipoVal2)
            globalVariables[val1]['value'] = val2

    elif currentScope == 'g':
        validateTypes(globalVariables[val1]['tipo'], tipoVal2)
        globalVariables[val1]['value'] = val2
    
    recep = fetchVDir(val1)
    dir1 = fetchVDir(val2)
    
    Cuadruplos.append(
        Cuad(
            Ops['='],
            dir1,
            -1,
            recep
        )
    )

def isVar(val):
    if val in globalVariables or val in localVariables:
        return True
    else:
        return False

def getVal(var):
    if var in localVariables:
        try: 
            return localVariables[var]['value']
        except:
            ERROR("no value", var)
    elif var in globalVariables:
        try: 
            return globalVariables[var]['value']
        except:
            ERROR("no value", var)
    else:
        ERROR("no existe", var)

def getType(var):
    if var in localVariables:
        try: 
            return localVariables[var]['tipo']
        except:
            ERROR("no tipo", var)
    elif var in globalVariables:
        try: 
            return globalVariables[var]['tipo']
        except:
            ERROR("no tipo", var)
    else:
        ERROR("no existe", var)

#*********************************
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
    'to' : 'TO',
    '&&' : 'AND',
    '||' : 'OR'
}

#***********************************
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
    'DIF',
    'NOT'
] + list(reserved.values())

#************************************
#types
t_ignore = "\t | '' | \n"

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

t_PTCOMA = r'\;'
t_APAR = r'\('
t_CPAR = r'\)'
t_ALLA = r'\{'
t_CLLA = r'\}'
t_COMA = r'\,'
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
t_NOT = r'\!'

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

#*********************************************
#Build lexer
import ply.lex as lex
lexer = lex.lex()

#*********************************************
#Gramatic rules

def p_program(t):
    'program : PROGRAM agregarTablaFunciones varss funcs MAIN APAR CPAR ALLA estatutos CLLA'
    print('Código aceptado')

def p_agregarTablaFunciones(t):
    'agregarTablaFunciones : ID PTCOMA'
    insertToFuncTable(t[1], 'void', currentScope, globalVariables)

# estructura mínima de cualquier programa, imprime mensaje si es válida la sintaxis

#------------------------------------
def p_varss(t):
    '''varss : VARS vars
             | empty
    '''
# palabra reservada de vars para iniciar declaraciones

def p_vars(t):
    '''vars : tipo DOSPNTS ID varsppp varspp vars
            | empty
    '''
    if len(t) > 2:
        vDir = getvDirVars(t[1], currentScope)
        insertToVarTable(t[3], vDir, t[1])

# formato tipo : id, id[n] ;

def p_varsppp(t):
    '''varsppp : ACOR CTEI CCOR
               | empty
    '''
# recibir dimension del vector
# fue variable simple

def p_varspp(t):
    '''varspp : PTCOMA
              | COMA ID varsppp varspp
    '''
    if len(t) > 2:
        vDir = getvDirVars(currentType, currentScope)
        insertToVarTable(t[2], vDir, currentType)

# fin de las declaraciones
# múltiples variables del mismo tipo

#------------------------------------
def p_funcs(t):
    '''funcs : FUNCTION funcsp ID funcspp
             | empty
    '''
    global currentScope
    global localVariables
    global currentType
    global usedNamesLocal
    if len(t) > 2: 
        currentScope = 'l'
        insertToFuncTable(t[3], currentType, currentScope, localVariables) #Supongo que aquí no debe ser localVariables, sino un pointer a la variable
    else:
        currentScope= 'g'
        #
        localVariables = {}
        usedNamesLocal = []

def p_funcspp(t):
    'funcspp : APAR params CPAR PTCOMA varss ALLA estatutos CLLA funcs'
    global currentScope
    currentScope = 'l'

# formato --> function void/tipo nombre función(int: id, float: id[]) 
# / espacio de declaracion de variables /
#{ Estatutos }
# mas funciones con el mismo formato

def p_funcsp(t):
    '''funcsp : VOID
              | tipo
    '''
    global currentType
    global currentScope
    currentType = t[1]
    currentScope = 'l'
    

# para funciones void
# funciones no void

#------------------------------------
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
# todos los posibles estatutos

def p_estatutop(t):
    '''estatutop : estatutos
                 | empty
    '''
# múltiples estatutos
# fin de los estatutos

#------------------------------------
def p_tipo(t):
    '''tipo : INT
            | FLOAT
            | CHAR
    '''
    global currentType
    currentType = t[1]
    t[0] = t[1]


# tipos soportados por el lenguaje

#------------------------------------
def p_params(t):
    '''params : tipo DOSPNTS ID ididx paramsp
              | empty
    '''
    global currentScope
    currentScope = 'l'
    insertToVarTable(t[3], t[1], currentScope)

# parametros para las funciones  --> int: var1, float: var2[]

def p_paramsp(t):
    '''paramsp : COMA params
               | empty
    '''
# múltiples parámetros
# fin de parámetros

#------------------------------------
def p_asig(t):
    'asig : ID ididx IGUAL asigpp PTCOMA'
    asignar(t[1], t[4])

# asignación id = expresion, expresion booleana, char, string y arreglos
# id = 123 ;
# id = 123.21 ;
# id = var1 ;
# id = var1[2] ;
# id = func(1, 2) ;
# id = 'c' ;
# id = [1,2,3] ;

def p_asigp(t):
    '''asigp : exp asigppp
             | CTEC asigppp
             | empty
    '''
    

# formar vectores de cualquier tipo de dato
# ultimo caso para declarar un vector vacio

#//// NOTA: en semantica habrá que validar que sean todos los elementos del mismo tipo y que coincidan con el tipo de la declaración inicial

def p_asigppp(t):
    '''asigppp : COMA asigp
               | empty
    '''
# múltiples elementos en el vector
# fin de elementos

def p_asigpp(t):
    '''asigpp : exp
              | CTEC
              | ACOR asigp CCOR
    '''
    print("Aqqui el id -->" + t[1])
    if len(t) < 3:
        t[0] = t[1]
# asignaciones para todo tipo de dato y arreglos

#------------------------------------
def p_ididx(t):
    '''ididx : ACOR exp CCOR
             | empty
    '''
# vertiente para ver si es id simple o si tiene indice

#------------------------------------
def p_llamada(t):
    'llamada : ID APAR args CPAR PTCOMA'

# llamada --> func(12, var, var[3]);

#------------------------------------
def p_args(t):
    '''args : ctes argsp
            | exp argsp
            | CTEC argsp
    '''
# aceptar todo tipo de dato para llamar a funciones en argumentos

def p_argsp(t):
    '''argsp : COMA args
             | empty
    '''
# multiples argumentos en llamada

#------------------------------------
def p_return(t):
    'return : RETURN APAR asigpp CPAR PTCOMA'
# return --> return(lo que sea);
# se usa asigpp porque cubre de manera neutra cualquier tipo de dato

#------------------------------------
def p_lectura(t):
    'lectura : READ APAR ID ididx lecturapp CPAR PTCOMA'
# leer de usuario y guardar sobre una variable o indice de un vector

def p_lecturapp(t):
    '''lecturapp : COMA ID ididx lecturapp
                 | empty
    '''
# lectura de múltiples elementos
# fin de elementos a leer

#------------------------------------
def p_escritura(t):
    'escritura : WRITE APAR escriturap escriturapp CPAR PTCOMA'
# escribir todo tipo de dato menos arreglo (suponiendo que si se quiere imprimir, ya debería de estar en una variable)

def p_escriturap(t):
    '''escriturap : STRING
                  | exp
                  | CTEC
    '''
# todos los tipos de datos

def p_escriturapp(t):
    '''escriturapp : COMA escriturap
                   | empty
    '''
# escribir varias cosas a la vez

#------------------------------------
def p_cond(t):
    'cond : IF APAR condp CPAR THEN ALLA estatutos CLLA condpp'
# estructura sencilla de if con opcional de un else

def p_condp(t):
    '''condp : exp
             | TRUE
             | FALSE
    '''
# lo unico que puede procesar la condición son cosas que sean booleanas

def p_condpp(t):
    '''condpp : ELSE ALLA estatutos CLLA
              | empty
    '''
# hay un else dentro de la condición

#------------------------------------
def p_while(t):
    'while : WHILE APAR condp CPAR DO ALLA estatutos CLLA'
# igual que la condición, para que inicie o no solo valora booleanos
# usamos condp porque tiene lo mismo de manera neutral

#------------------------------------
def p_for(t):
    'for : FOR ID ididx IGUAL exp TO exp DO ALLA estatutos CLLA'
# estructura básica de un for --> for i ([0]) = 0 to 10 do { estatutos }

#------------------------------------

def p_exp(t):
    'exp : texp expp'
    t[0] = t[1]

def p_expp(t):
    '''expp : OR exp
            | empty
    '''
    if t[1] == 'or':
        t[0] = t[0] or t[2]

def p_texp(t):
    'texp : gexp texpp'
    t[0] = t[1]

def p_texpp(t):
    '''texpp : AND texp
             | empty
    '''
    if t[1] == 'and':
        t[0] = t[0] and t[2]

def p_gexp(t):
    'gexp : mexp gexpp'
    t[0] = t[1]

def p_gexpp(t):
    '''gexpp : MAYQ mexp
             | MENQ mexp
             | MAYI mexp
             | MENI mexp
             | IGUALIGUAL mexp
             | DIF mexp
             | empty
    '''
    if t[1] == '>':
        t[0] = t[0] > t[2]
    elif t[1] == '<':
        t[0] = t[0] < t[2]
    elif t[1] == '>=':
        t[0] = t[0] >= t[2]
    elif t[1] == '<=':
        t[0] = t[0] <= t[2]
    elif t[1] == '==':
        t[0] = t[0] == t[2]
    elif t[1] == '!=':
        t[0] = t[0] != t[2]


def p_mexp(t):
    'mexp : termino mexpp'
    t[0] = t[1]
# terminos de menor jerarquía

def p_mexpp(t):
    '''mexpp : MAS mexp
            | MENOS mexp
            | empty
    '''
    if t[1] == '+':
        t[0] = t[0] + t[2]
        POoper.append(t[1])
    elif t[1] == '-':
        t[0] = t[0] - t[2]
        POoper.append(t[1])
# solo sumas o restas de terminos

#------------------------------------
def p_termino(t):
    'termino : factor terminop'
    if len(POoper) > 0:
        if POoper[-1] == '+' or POoper[-1] == '-':
            rOp = PilaO.pop()
            rType = Ptipos.pop()
            lOp = PilaO.pop()
            lType = Ptipos.pop()
            op = POoper.pop()
            resType = isValidOp(rType, lType, op)
            resVdir = getVDirTemp(resType)
            Cuadruplos.append(Cuad(Ops[op], lOp, rOp, resVdir))
            PilaO.append(resVdir)
    t[0] = t[1]
# segundo nivel de jerarquía

def p_terminop(t):
    '''terminop : POR termino
                | DIV termino
                | empty
    '''
    if t[1] == '*':
        t[0] = t[0] * t[2]
        POoper.append(t[1])
    elif t[1] == "/":
        t[0] = t[0] / t[2]
        POoper.append(t[1])
# solo multiplicaciones y divisiones de factores

#--------------------------
def p_factor(t): 
    '''factor : APAR exp CPAR
              | ID factorp
              | ctes
    '''
    if len(t) == 2:
        t[0] = t[1]
    if len(t) == 3:
        vDir = fetchVDir(t[1])
        PilaO.append(vDir)
        Ptipos.append(getValType(t[1]))
        t[0] = t[1]
    
    if len(POoper) > 0:
        if  POoper[-1] == '*' or POoper[-1] == '/':
            rOp = PilaO.pop()
            rType = Ptipos.pop()
            lOp = PilaO.pop()
            lType = Ptipos.pop()
            op = POoper.pop()
            resType = isValidOp(rType, lType, op)
            resVdir = getVDirTemp(resType)
            Cuadruplos.append(Cuad(Ops[op], lOp, rOp, resVdir))
            PilaO.append(resVdir)

# para expresiones anidadas entre paréntesis
# para id's , elemento de vector y llamadas de función
# constantes directas

def p_factorp(t):
    '''factorp : APAR exp factorpp CPAR
               | ACOR exp CCOR
               | empty
    '''
    
# parametros de funcion
# indice de vector
# fue id sencillo

def p_factorpp(t):
    '''factorpp : COMA exp factorpp
                | empty
    '''
# múltiples parámetros
# salir de bucle

#----------------------------------
def p_ctes(t):
    '''ctes : ID factorp
            | CTEI
            | CTEF
    '''
    if len(t) == 2:
        tablaConstantes[t[1]] = getVdirCTE(t[1])
        t[0] = t[1]

# id, indice vector o llamada de función
    # se usa factorp porque tiene exactamente la misma función, no altera en nada
# constante int
# constante float


#--------------------------
def p_empty(t):
    'empty :'
    pass
# Epsilon

#---------------------------
def p_error(t):
    print("Error sintáctico en '%s'" % t.value)
    print(t)
# decir en dónde hubo error de sintaxis

#****************************
# procesar archivo de input
import ply.yacc as yacc
parser = yacc.yacc()
f = open("./pass3.txt", "r")
input = f.read()
#print(input)
parser.parse(input, debug=0)
for c in Cuadruplos:
    print(str(c.count) + " " + "Cuad --> " + str(c.op) + " " + str(c.dir1) + " " + str(c.dir2) + " " + str(c.recep))