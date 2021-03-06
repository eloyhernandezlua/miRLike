from os import pipe, popen, truncate
import re
import sys 

arch = input("Ingresa el nombre del archivo a compilar: ")

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
PJumps = []
Cuadruplos = [] 
Consts = []
ParameterTable = {}
ParameterTableList = []
tablaConstantes = {}
VControl = 0
VFinal = 0
contTemps = 0
contParams = []

isArray = False
PDim = []
funcName = ''
filaParams = []

especiales = []
especialesAux = []
contEspeciales = -1

ariops = ['+', '-', '*', '/']
relops = ['>', '<', '>=', '<=', '==', '!=']
logicops = ['and', 'or']

#Inicialización de los contadores para direcciones virtuales

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
contConstC = 43000 - 1
contFuncV = 46000 - 1
contPointers = 50000 - 1
contParamsInt = 60000 - 1
contParamsFloat = 63000 - 1
contParamsChar = 66000 - 1

#Definir objeto cuadruplo 
class Cuad:
    def __init__(self, op, dir1, dir2, recep):
        global Cuadruplos
        self.count = len(Cuadruplos) + 1
        self.op = op 
        self.dir1 = dir1 
        self.dir2 = dir2
        self.recep = recep

# Operadores para usar en los cuádruplos

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
    '>=' : 9,
    '!=' : 10,
    '=' : 11,
    'print' : 12,
    'read' : 13,
    'goto' : 14,
    'gotoF' : 15,
    'gotoT' : 16,
    'return' : 17,
    'and' : 18,
    'or' : 19,
    'endFunc' : 20,
    'era' : 21,
    'parameter' : 22,
    'gosub' : 23,
    'ver' : 24,
    'media' : 25,
    'mediahar' : 26,
    'mediana' : 27,
    'medianagroup' : 28,
    'moda' : 29,
    'pstdev' : 30,
    'stdev' : 31,
    'pvariance' : 32,
    'variance' : 33,
    'plotx' : 34
}

#**********
#Plan para manejar las vdirs ---> al 12/11
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
# | const char     | 43000 |
# | fun vars       | 46000 |
# | pointers       | 50000 |
# -------------------------- 

# Para obtener direcciones virutales para las variables globales que se llamen igual a funciones (el parche guadalupano)

def getFuncVDir():
    global contFuncV
    contFuncV += 1
    return contFuncV

# Resetear todo lo necesario cuando se termina de compilar una función

def endFuncReset():
    global contLocI
    global contLocF
    global contLocC 
    global contTempI
    global contTempF
    global contTempC
    global contTempB
    global contPointers
    global currentScope
    global localVariables
    global usedNamesLocal
    global contTemps
    global contParamsInt
    global contParamsFloat
    global contParamsChar
    global ParameterTable
    global ParameterTableList

    contLocI = 12000 - 1
    contLocF = 20000 - 1
    contLocC = 28000 -1
    contTempI = 30000 - 1 
    contTempF = 32000 - 1
    contTempC = 34000 -1
    contTempB = 36000 - 1
    contPointers = 50000 - 1
    contParamsInt = 60000 - 1
    contParamsFloat = 63000 - 1
    contParamsChar = 66000 - 1

    currentScope= 'g'
    localVariables = {}
    usedNamesLocal = []
    contTemps = 0

#obtener direcciones virtuales para cuando son constantes, int, float y char

def getVdirCTE(v):
    global contConstF
    global contConstI
    global contConstC
    if type(v) == int:
        contConstI += 1
        return contConstI
    elif type(v) == float:
        contConstF += + 1
        return contConstF
    elif type(v) == str: 
        contConstC += 1
        return contConstC
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
    elif tipo == "function had no parameters":
        extra = "FUNCTION EXPECTED NO PARAMETERS"
    elif tipo == "Missing or too much parameters":
        extra = "MISSING OR TOO MUCH PARAMETERS"
    elif tipo == "no dims":
        extra = "VAR HAS NO DIMESIONS"
    elif tipo == "only ints and floats allowed":
        extra = "ONLY NUMBERS ARE ALLOWED"

    print("ERROR: " + extra + "\n @ --> " + str(at))
    sys.exit() # se imprime el error en pantalla y se detiene la ejecución del código


#Insertar en la tabla de funciones, se necesita el nombre de la función, su tipo, scope y que mapa de variables le corresponde

def insertToFuncTable(id, tipo, scope, vars):
    global mainFuncTable
    global usedNamesGlobal
    global usedNamesLocal

    #validar que la funcion no haya sido declarada o que no sea ya el nombre de otra variable
    if id in mainFuncTable:
        ERROR("funcion repetida")
    elif id in usedNamesGlobal:
        ERROR("nombre repetido")
    else:   
        mainFuncTable[id] = {'tipo' : tipo, 'scope': scope, 'vars': vars}
        usedNamesGlobal.append(id)


#Obtener direcciones virtuales para los contadores de temporales
def getVDirTemp(type):
    global contTempB
    global contTempC
    global contTempF
    global contTempI
    global contPointers
    global contTemps

    contTemps += 1

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
    elif type == 'pointer':
        contPointers += 1
        return contPointers


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
        'floatint+',
        'floatint-',
        'floatint*',
        'floatint/',
        'floatint>',
        'floatint<',
        'floatint>=',
        'floatint<=',
        'floatint==',
        'floatint!=',
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
        'boolbooland',
        'boolboolor',
        'boolbool>',
        'boolbool<',
        'boolbool>=',
        'boolbool<=',
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

#Obtener direccion virutal para las variables, dependiendo su tipo y su scope
def getvDirVars(tipo, scope):
    global contGlobI
    global contGlobF
    global contGlobC
    global contLocI
    global contLocF
    global contLocC

    if scope == 'g':
        if tipo == 'int': 
            contGlobI += 1
            return contGlobI + 1
        elif tipo == 'float':
            contGlobF += 1
            return contGlobF + 1
        elif tipo == 'char':
            contGlobC += 1
            return contGlobC + 1
    else:
        if tipo == 'int': 
            contLocI += 1
            return contLocI
        elif tipo == 'float':
            contLocF += 1
            return contLocF
        elif tipo == 'char':
            contLocC += 1
            return contLocC 

#Insertar varible a su tabla de variables correspondiente, global o local. Checando que no exista 
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


#Validar que 2 tipos de datos sean del mismo
def validateTypes(tipo1, tipo2):
    if tipo1 != tipo2:
        ERROR("tipos distintos", str(tipo1 + " --- " + tipo2))

# Obtener el tipo de un valor, buscándolo en las tablas de variables o constantes dependiendo su identificador en las mismas
def getValType(val):
    if val in localVariables:
        return localVariables[val]['tipo']

    if val in globalVariables:
        return globalVariables[val]['tipo']

    if val in mainFuncTable:
        return mainFuncTable[val]['tipo']

    if type(val) == int:
        return 'int'
    if type(val) == float:
        return 'float'
    if type(val) == str:
        return 'char'
    
#Buscar la dirección virtual de algún id ya declarado en cualquier lado con la prioridad Local -> global -> constantes
def fetchVDir(val):
    global tablaConstantes
    global localVariables
    global globalVariables
    global mainFuncTable

    if val in localVariables:
        return localVariables[val]['vDir']
    elif val in globalVariables:
        return globalVariables[val]['vDir']
    else:
        if type(val) == int:
            return tablaConstantes[int(val)]
        if type(val) == float:
            return tablaConstantes[float(val)]
        if type(val) == str:
            return tablaConstantes[str(val)]

#Verifica si el id dado existe dentro de las variables conocidas
def isVar(val):
    if val in globalVariables or val in localVariables:
        return True
    else:
        return False

#obtener el tipo de variable
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

#Valida que el id se haya declarado en algún lado, donde sea
def validateExistance(id):
    global localVariables
    global globalVariables
    global tablaConstantes
    global mainFuncTable

    if id not in tablaConstantes and id not in globalVariables and id not in localVariables and id not in mainFuncTable:
        ERROR("no existe", id)

#Para manejar arreglos, dependiendo el scope, y su tipo, se desplazará el contador a la siguiente + el tamaño del arreglo declarado
def setNextVDir(cScope, cType, size):
    global contLocI
    global contLocF
    global contLocC

    global contGlobI
    global contGlobF
    global contGlobC

    if cScope == 'l':
        if cType == 'int':
            contLocI += size
        elif cType == 'float':
            contLocF += size
        elif cType == 'char':
            contLocC += size
    elif cScope == 'g':
        if cType == 'int':
            contGlobI += size
        elif cType == 'float':
            contGlobF += size
        elif cType == 'char':
            contGlobC += size

#Checar si una variable es un arreglo
def checkForDims(id):
    global localVariables
    global globalVariables
    try:
        localVariables[id]['isArray']
    except:
        try:
            globalVariables[id]['isArray']
        except:
            ERROR("no dims")


def isarray(id):
    global localVariables
    global globalVariables
    try:
        localVariables[id]['isArray']
        return True
    except:
        try:
            globalVariables[id]['isArray']
            return True
        except:
            return False


#Validar si los valores ingresados son exclusivamente numericos
def isNum(val):
    tipo = getValType(val)
    if tipo == 'int' or tipo == 'float':
        return True
    else:
        return False

#Actualizar la propiedad de tamaño de una variable dimensionada 
def setSizeArr(id, scope, size):
    global localVariables
    global globalVariables

    if scope == 'g':
        globalVariables[id]['size'] = size
    elif scope == 'l':
        localVariables[id]['size'] = size

#Encontrar el límite superior de un arreglo
def fetchLimit(id):
    global globalVariables
    global localVariables

    try: 
        return localVariables[id]['size']
    except:
        return globalVariables[id]['size']

#Encontrar la direccion inicial de un arrelo que se esté utilizando
def fetchInitDir(id):
    global localVariables
    global globalVariables

    try: 
        return localVariables[id]['vDir']
    except:
        return globalVariables[id]['vDir']


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
    'and' : 'AND',
    'or' : 'OR',
    'media' : 'MEDIA',
    'mediahar' : 'MEDIAHAR',
    'mediana' : 'MEDIANA',
    'medianagroup' : 'MEDIANAG',
    'moda' : 'MODA',
    'pstdev' : 'PSTDEV',
    'stdev' : 'STDEV',
    'pvariance' : 'PVARIANCE',
    'variance' : 'VARIANCE',
    'plotx' : 'PLOTX'
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
t_ignore = ' \t'

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
    r'-?\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_CTEI(t):
    r'-?\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
    r'[A-Za-z]([A-Za-z]|[0-9])*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
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

#----------------------------------------------
#PROGRAMA PRINCIPAL

# estructura mínima de cualquier programa, imprime mensaje si es válida la sintaxis
def p_program(t):
    'program : PROGRAM agregarTablaFunciones varss funcs MAIN APAR CPAR ALLA poptomain estatutos CLLA'
    print('Código aceptado \n\n')

    global contGlobI
    global contTempI
    global contGlobF
    global contTempF
    global contGlobC
    global contTempC
    global contTempB
    global contPointers
    global contConstC
    global contConstI
    global contConstF
    global contFuncV    

    nombreFunc = t[2]
    # Calcular y guardar el tamaño del programa principal
    mainFuncTable[nombreFunc]['numInts'] = (contGlobI - (2000-1)) + (contTempI - (30000 -1))
    mainFuncTable[nombreFunc]['numFloats'] = (contGlobF - (5000-1)) + (contTempF - (32000 -1))
    mainFuncTable[nombreFunc]['numChars'] = (contGlobC - (9000-1)) + (contTempC - (34000 -1))
    mainFuncTable[nombreFunc]['numBools'] = (contTempB - (36000-1))
    mainFuncTable[nombreFunc]['numPointers'] = (contPointers - (50000-1))

def p_agregarTablaFunciones(t):
    'agregarTablaFunciones : ID PTCOMA'
    global currentScope
    global globalVariables
    global Cuadruplos
    global Ops
    global PJumps
    global tablaConstantes

    t[0] = t[1]
    #Agregar el nombre del programa a la tabla de funciones y generar el goto a main
    insertToFuncTable(t[1], 'void', currentScope, globalVariables)
    Cuadruplos.append(Cuad(Ops['goto'], -1, -1, -99))
    PJumps.append(len(Cuadruplos))
    tablaConstantes[0] = getVdirCTE(0)
    tablaConstantes[1] = getVdirCTE(1)

#llenar el cuadruplo pendiente de donde empieza el main
def p_poptomain(t):
    '''poptomain : '''
    global Cuadruplos
    global PJumps

    if PJumps:
        end = PJumps.pop()
        cuadToChange = Cuadruplos[end - 1]
        cuadToChange.recep = len(Cuadruplos) + 1

#------------------------------------
#VARIABLES
def p_varss(t):
    '''varss : VARS vars
             | empty
    '''
# palabra reservada de vars para iniciar declaraciones

def p_vars(t):
    '''vars : tipo DOSPNTS insertVar varsppp varspp vars
            | empty
    '''

#Meter conforme son leidas las variable a la tabla de variables y consiguiendo sus direcciones virtuales
def p_insertVar(t):
    'insertVar : ID'
    global currentScope
    global currentType
    t[0] = t[1]
    vDir = getvDirVars(currentType, currentScope)
    insertToVarTable(t[1], vDir, currentType)

# formato tipo : id, id[n] ;

# Para variables dimensionadas
def p_varsppp(t):
    '''varsppp : initDim CTEI setDim
               | empty
    '''

#En el corchete que cierra guardar cual fue el número del tamaño, guardarlo en tabla de constantes si no existía
# guardar la propiedad de tamaño y setear el proximo numero de direccion virutal acorde al arreglo 
def p_setDim(t):
    '''setDim : CCOR'''
    global currentScope
    global currentType
    global tablaConstantes

    size = int(t[-1])
    id = t[-3]

    if not t[-1] in tablaConstantes:
        tablaConstantes[size] = getVdirCTE(size)

    setSizeArr(id, currentScope, size) #checar
    setNextVDir(currentScope, currentType, size)    

# En el corchete que abre, definir que esa variable ahora es tratada como un arreglo
def p_initDim(t):
    '''initDim : ACOR'''
    global localVariables
    global globalVariables
    global currentScope

    id = t[-1]
    if currentScope == 'l':
        localVariables[id]['isArray'] = True
    elif currentScope == 'g':
        globalVariables[id]['isArray'] = True


# recibir dimension del vector
# fue variable simple

def p_varspp(t):
    '''varspp : PTCOMA
              | COMA insertVar varsppp varspp
    '''
# fin de las declaraciones
# múltiples variables del mismo tipo

#------------------------------------
#FUNCIONES

# formato --> function void/tipo nombre función(int: id, float: id[]) 
# / espacio de declaracion de variables /
#{ Estatutos }
# mas funciones con el mismo formato

def p_funcs(t):
    '''funcs : FUNCTION funcsp insertFunc funcspp
             | empty
    '''

#guardar nombre de la función en la tabla de funciones
def p_insertFunc(t):
    'insertFunc : ID'
    global currentScope
    global currentType
    global localVariables
    global globalVariables
    global funcName

    funcName = t[1]

    t[0] = t[1]
    currentScope = 'l'
    vDir = getFuncVDir()
    globalVariables[funcName] = {'vDir': vDir, 'tipo': currentType}
    insertToFuncTable(funcName, currentType, currentScope, localVariables)

#Cambiar a un scope local
def p_funcspp(t):
    'funcspp : APAR params CPAR updateParamTable PTCOMA varss ALLA addinit estatutos CLLA addsize endfunction funcs'
    global currentScope
    currentScope = 'l'


def p_updateParamTable(t):
    '''updateParamTable : '''
    global ParameterTableList
    global ParameterTable
    id = t[-4]
    

#llevar a cabo las labores del endfunc
def p_endfunciton(t):
    '''endfunction : '''

    global mainFuncTable 
    global contTemps
    global Cuadruplos
    global Ops
    global funcName
    
    idfunc = funcName
    mainFuncTable[idfunc]['numTemps'] = contTemps
    Cuadruplos.append(Cuad(Ops['endFunc'], -1, -1, -1))
    endFuncReset()


#guardar el tamaño de la nueva funcion
def p_addsize(t):
    '''addsize : '''
    global ParameterTable
    global mainFuncTable
    global localVariables
    global Cuadruplos
    global contLocI
    global contTempI
    global contLocF
    global contTempF
    global contLocC
    global contTempC
    global contTempB
    global contPointers
    global funcName

    nombreFunc = funcName
    mainFuncTable[nombreFunc]['numParamsVars'] = len(localVariables)
    mainFuncTable[nombreFunc]['numInts'] = (contLocI - (12000-1)) + (contTempI - (30000 -1))
    mainFuncTable[nombreFunc]['numFloats'] = (contLocF - (20000-1)) + (contTempF - (32000 -1))
    mainFuncTable[nombreFunc]['numChars'] = (contLocC - (28000-1)) + (contTempC - (34000 -1))
    mainFuncTable[nombreFunc]['numBools'] = (contTempB - (36000-1))
    mainFuncTable[nombreFunc]['numPointers'] = (contPointers - (50000-1))

#guardar el cuadruplo de inicio para la función    
def p_addinit(t):
    '''addinit : '''
    global funcName
    global Cuadruplos

    nombreFunc = funcName
    mainFuncTable[nombreFunc]['initFunc'] = len(Cuadruplos) + 1

#definir el tipo de la función
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
#ESTATUTOS

def p_estatutos(t):
    '''estatutos : asig estatutop
                 | return estatutop
                 | lectura estatutop
                 | escritura estatutop
                 | cond estatutop
                 | while estatutop
                 | for estatutop
                 | exp estatutop
                 | media estatutop
                 | plotx estatutop
                 | variance estatutop
                 | pvariance estatutop
                 | stdev estatutop
                 | pstdev estatutop
                 | moda estatutop
                 | medianag estatutop
                 | mediana estatutop
                 | mediahar estatutop


    '''
# todos los posibles estatutos

def p_estatutop(t):
    '''estatutop : estatutos
                 | empty
    '''
# múltiples estatutos
# fin de los estatutos


#-----------------------------------
#FUNCIONES ESPECIALES

#meida
def p_media(t):
    '''media : MEDIA APAR numeros CPAR appendlist PTCOMA'''
    global Cuadruplos
    global Ops
    global especialesAux
    global especiales
    global contEspeciales

    contEspeciales += 1

    Cuadruplos.append(Cuad(Ops['media'], -1, -1, contEspeciales))
    especialesAux = []

#media harmonizada 
def p_mediahar(t):
    '''mediahar : MEDIAHAR APAR numeros CPAR appendlist PTCOMA'''
    global Cuadruplos
    global Ops
    global especialesAux
    global especiales
    global contEspeciales

    contEspeciales += 1

    Cuadruplos.append(Cuad(Ops['mediahar'], -1, -1, contEspeciales))
    especialesAux = []

#mediana
def p_mediana(t):
    '''mediana : MEDIANA APAR numeros CPAR appendlist PTCOMA'''
    global Cuadruplos
    global Ops
    global especialesAux
    global especiales
    global contEspeciales

    contEspeciales += 1

    Cuadruplos.append(Cuad(Ops['mediana'], -1, -1, contEspeciales))
    especialesAux = []

#mediana grupal
def p_medianag(t):
    '''medianag : MEDIANAG APAR numeros CPAR appendlist PTCOMA'''
    global Cuadruplos
    global Ops
    global especialesAux
    global especiales
    global contEspeciales

    contEspeciales += 1

    Cuadruplos.append(Cuad(Ops['medianagroup'], -1, -1, contEspeciales))
    especialesAux = []

#moda
def p_moda(t):
    '''moda : MODA APAR numeros CPAR appendlist PTCOMA'''
    global Cuadruplos
    global Ops
    global especialesAux
    global especiales
    global contEspeciales

    contEspeciales += 1

    Cuadruplos.append(Cuad(Ops['moda'], -1, -1, contEspeciales))
    especialesAux = []

#desviación estandar poblacional
def p_pstdev(t):
    '''pstdev : PSTDEV APAR numeros CPAR appendlist PTCOMA'''
    global Cuadruplos
    global Ops
    global especialesAux
    global especiales
    global contEspeciales

    contEspeciales += 1

    Cuadruplos.append(Cuad(Ops['pstdev'], -1, -1, contEspeciales))
    especialesAux = []

#desviación estandar
def p_stdev(t):
    '''stdev : STDEV APAR numeros CPAR appendlist PTCOMA'''
    global Cuadruplos
    global Ops
    global especialesAux
    global especiales
    global contEspeciales

    contEspeciales += 1

    Cuadruplos.append(Cuad(Ops['stdev'], -1, -1, contEspeciales))
    especialesAux = []

#varianza poblacional
def p_pvariance(t):
    '''pvariance : PVARIANCE APAR numeros CPAR appendlist PTCOMA'''
    global Cuadruplos
    global Ops
    global especialesAux
    global especiales
    global contEspeciales

    contEspeciales += 1

    Cuadruplos.append(Cuad(Ops['pvariance'], -1, -1, contEspeciales))
    especialesAux = []

#varianza
def p_variance(t):
    '''variance : VARIANCE APAR numeros CPAR appendlist PTCOMA'''
    global Cuadruplos
    global Ops
    global especialesAux
    global especiales
    global contEspeciales

    contEspeciales += 1

    Cuadruplos.append(Cuad(Ops['variance'], -1, -1, contEspeciales))
    especialesAux = []

#plot
def p_plotx(t):
    '''plotx : PLOTX APAR numeros CPAR appendlist PTCOMA'''
    global Cuadruplos
    global Ops
    global especialesAux
    global especiales
    global contEspeciales

    contEspeciales += 1

    Cuadruplos.append(Cuad(Ops['plotx'], -1, -1, contEspeciales))
    especialesAux = []


def p_appendlist(t):
    '''appendlist : '''

    global especiales
    global especialesAux

    especiales.append(especialesAux)


def p_numeros(t):
    '''numeros : CTEI addnum numerosp
               | CTEF addnum numerosp
    '''

def p_addnum(t):
    '''addnum : '''

    global especialesAux

    especialesAux.append(t[-1])


def p_numerosp(t):
    '''numerosp : COMA numeros
                | empty
    '''

#------------------------------------
#TIPOS

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
#PARAMETROS

def p_params(t):
    '''params : tipo DOSPNTS insertParams ididx paramsp
              | empty
    '''

# añadir los parametros sus nuevas direcciones virtuales y agregarlos a la fila de parametros, guardar sus tipos para la firma
def p_insertParams(t):
    '''insertParams : ID
    '''
    global currentScope
    global currentType
    global ParameterTableList
    global filaParams

    currentScope = 'l'
    vDir = getvDirVars(currentType, currentScope)
    filaParams.append(vDir)
    insertToVarTable(t[1], vDir, currentType)
    ParameterTableList.append(currentType)

def p_paramsp(t):
    '''paramsp : COMA params
               | empty
    '''
# múltiples parámetros
# fin de parámetros

#------------------------------------
#ASIGNACIONES

def p_asig(t):
    'asig : varAs ididx igualAs asigpp PTCOMA'
    global PilaO
    global Ptipos
    global Ops

    # sacar los ultimos 2 operandos con sus tipos, validar que sean asignables y generar su cuádruplo
    if PilaO and Ptipos:
        res = PilaO.pop()
        tipoR = Ptipos.pop()
        ladoIzq = PilaO.pop()
        tipoI = Ptipos.pop()
        validateTypes(tipoR, tipoI)
        Cuadruplos.append(Cuad(Ops['='], res, -1, ladoIzq))

# llevar tracking de la variable a la que se le quiere asignar algo
def p_varAs(t):
    'varAs : ID'
    global PilaO
    global Ptipos
    t[0] = t[1]
    vDir = fetchVDir(t[1])
    PilaO.append(vDir)
    Ptipos.append(getValType(t[1]))

#añadir el operador = a la pila    
def p_igualAs(t):
    'igualAs : IGUAL'
    global POoper
    global Cuadruplos

    POoper.append(t[1])
    
# asignación id = expresion, expresion booleana, char, string y arreglos
# id = 123 ;
# id = 123.21 ;
# id = var1 ;
# id = var1[2] ;
# id = func(1, 2) ;
# id = 'c' ;


def p_asigp(t):
    '''asigp : exp asigppp
             | empty
    '''
    

# formar vectores de cualquier tipo de dato
# ultimo caso para declarar un vector vacio

def p_asigppp(t):
    '''asigppp : COMA asigp
               | empty
    '''
# múltiples elementos en el vector
# fin de elementos

def p_asigpp(t):
    '''asigpp : exp'''
    
    t[0] = t[1]
# asignaciones para todo tipo de dato y arreglos

#------------------------------------
#MANEJO DE DIMENSIONES

def p_ididx(t):
    '''ididx : corArr exp ver CCOR
             | empty
    '''
    global PilaO
    global Cuadruplos
    global Ops
    global globalVariables
    global POoper
    global tablaConstantes
    global Ptipos

    #Si SÍ HAY dimeiones hay que hacer las operaciones de una nueva direccion virtual de pointer y sumar el offset (en cuadruplo)
    if len(t) > 2:
        if PilaO and POoper:
            aux1 = PilaO.pop()
            initDir = fetchInitDir(t[-1])

            if not initDir in tablaConstantes:
                tablaConstantes[initDir] = getVdirCTE(initDir)

            initDirVal = tablaConstantes[initDir]

            pointer = getVDirTemp('pointer')

            Cuadruplos.append(Cuad(Ops['+'], aux1, initDirVal, pointer))
            PilaO.append(pointer)
            POoper.pop()




# Comenzar manejo de arreglos, metiendo fondo falso para que no se pase
def p_corArr(t):
    '''corArr : ACOR'''
    global PDim
    global POoper
    global PilaO
    global Ptipos

    if PilaO:
        id = PilaO.pop()
        tipo = Ptipos.pop()
        idName = t[-1]
        checkForDims(idName)
        DIM = 1
        PDim.append((id, DIM))
        POoper.append("~") #fake bottom


#Gernerar cuadruplo para verificar el rango dentro de los arrelgos

def p_ver(t):
    '''ver : '''
    
    global PilaO
    global Cuadruplos
    global Ops
    global tablaConstantes

    
    val = PilaO[-1]
    id = t[-3]
    lim = fetchLimit(id)
    limSup = fetchVDir(lim)
    limInf = fetchVDir(0)

    Cuadruplos.append(Cuad(Ops['ver'], val, limInf, limSup))


#------------------------------------
#RETURN

#Crea el cuadruplo con lo que esté al final de la pila y como parche guadalupano, lleva la dirección virutal de la función que lo ejecutó
def p_return(t):
    'return : RETURN APAR exp CPAR PTCOMA'
    global PilaO
    global Cuadruplos
    global Ops
    global globalVariables
    retVal = PilaO.pop()
    Ptipos.pop()
    funcDir = globalVariables[funcName]['vDir']
    Cuadruplos.append(Cuad(Ops['return'], retVal, -1, funcDir))

#------------------------------------
#LECTURA

def p_lectura(t):
    'lectura : READ APAR readId ididx lecturapp CPAR PTCOMA'
# leer de usuario y guardar sobre una variable o indice de un vector

def p_readId(t):
    '''readId : ID
    '''
    global Cuadruplos
    global Ops
    var = fetchVDir(t[1])
    Cuadruplos.append(Cuad(Ops['read'], -1, -1, var))

def p_lecturapp(t):
    '''lecturapp : COMA readId ididx lecturapp
                 | empty
    '''
# lectura de múltiples elementos
# fin de elementos a leer

#------------------------------------
#ESCRITURA

def p_escritura(t):
    'escritura : WRITE APAR escriturap escriturapp CPAR PTCOMA'

# escribir todo tipo de dato menos arreglo (suponiendo que si se quiere imprimir, ya debería de estar en una variable)

#Generar directamente el cuadruplo, con la última expresion o el letrero
def p_escriturap(t):
    '''escriturap : pushEsc
                  | exp
    '''
    global PilaO
    global Cuadruplos
    global Ops

    res = PilaO.pop()
    Cuadruplos.append(Cuad(Ops['print'], -1, -1, res))  

# Meter a la escritura un char o un letrero string
def p_pushEsc(t):
    '''pushEsc : STRING
               | CTEC
    '''
    global PilaO
    PilaO.append(t[1])

# escribir varias cosas a la vez
def p_escriturapp(t):
    '''escriturapp : COMA escriturap escriturapp
                   | empty
    '''

#------------------------------------
#CONDICIONALES

# estructura sencilla de if con opcional de un else
def p_cond(t):
    'cond : IF APAR exp checkCond THEN ALLA estatutos CLLA condpp'
    
    global PJumps
    global Cuadruplos

    if PJumps:
        end = PJumps.pop()
        cuadToChange = Cuadruplos[end - 1]
        cuadToChange.recep = len(Cuadruplos) + 1


#chechar si la expresion trae un else o si es un if sencillo 
def p_condpp(t):
    '''condpp : checkElse ALLA estatutos CLLA
              | empty
    '''

#hacer los cuadruplos para llenar el salto del if y generar el nuevo salto solo si hay else
def p_checkElse(t):
    '''checkElse : ELSE
    '''
    global Cuadruplos
    global PJumps
    global Ops

    if PJumps:
        Cuadruplos.append(Cuad(Ops['goto'], -1, -1, -99))
        false = PJumps.pop()
        PJumps.append(len(Cuadruplos))

        cuadToChange = Cuadruplos[false - 1]
        cuadToChange.recep = len(Cuadruplos) + 1

#verificar la condicion, que sea bool y hacer el cuadruplo del goto en falso
def p_checkCond(t):
    '''checkCond : CPAR
    '''
    global Ptipos
    global PilaO
    global Cuadruplos
    global PJumps
    global Ops

    if Ptipos and PilaO:
        expType = Ptipos.pop()
        validateTypes(expType, 'bool')
        result = PilaO.pop()
        Cuadruplos.append(Cuad(Ops['gotoF'], result, -1, -99))
        PJumps.append(len(Cuadruplos))


#------------------------------------
#WHILE

# llenar el cuadruplo goto automatico y llenar el goto en falso pendiente de la condicion
def p_while(t):
    'while : saveWhile APAR exp checkWhileCond DO ALLA estatutos CLLA'

    global PJumps
    global Cuadruplos
    global Ops

    if PJumps:
        end = PJumps.pop()
        ret = PJumps.pop()
        Cuadruplos.append(Cuad(Ops['goto'], -1, -1, ret+1))
        cuadToChange = Cuadruplos[end - 1]
        cuadToChange.recep = len(Cuadruplos) + 1

#Dejar migaja de pan para el while
def p_saveWhile(t):
    '''saveWhile : WHILE
    '''
    global PJumps
    global Cuadruplos
    PJumps.append(len(Cuadruplos))

# revisar la condición y hacer el cuadruplo de goto en falso
def p_checkWhileCond(t):
    '''checkWhileCond : CPAR
    '''
    global Ptipos
    global PilaO
    global Cuadruplos
    global PJumps
    global Ops

    if Ptipos and PilaO:
        expType = Ptipos.pop()
        validateTypes(expType, 'bool')
        res = PilaO.pop()
        Cuadruplos.append(Cuad(Ops['gotoF'], res, -1, -99))
        PJumps.append(len(Cuadruplos))


#------------------------------------
#FOR

# estructura básica de un for --> for i ([0]) = 0 to 10 do { estatutos } 

def p_for(t):
    'for : FOR varFor ididx IGUAL exp initFor exp beforeDo ALLA estatutos CLLA'

    global VControl
    global PJumps
    global Cuadruplos
    global Ops
    global PilaO
    global Ptipos


    ty = getVDirTemp('int')
    vdirUno = fetchVDir(1) #tener dvir de la constante del num 1
    Cuadruplos.append(Cuad(Ops['+'], VControl, vdirUno, ty)) # sumarle uno a la variable de control
    Cuadruplos.append(Cuad(Ops['='], ty, -1, VControl)) #igual ese valor a una variable temporal
    Cuadruplos.append(Cuad(Ops['='], ty, -1, PilaO[-1])) #y también a la varaible original
    fin = PJumps.pop() #saber a donde termina
    ret = PJumps.pop() #saber a donde volver para el ciclo
    Cuadruplos.append(Cuad(Ops['goto'], -1, -1, ret)) #goto automatico a donde se tiene que retornar para validar la condicion
    Cuadruplos[fin - 1].recep = len(Cuadruplos) + 1 # llenar los saltos
    elimina = PilaO.pop()
    tipoelimina = Ptipos.pop()

#inicio y manejo de la variable de control
def p_varFor(t):
    '''varFor : ID
    '''
    global PilaO
    global Ptipos

    dVir = fetchVDir(t[1])
    type = getType(t[1])
    PilaO.append(dVir)
    Ptipos.append(type)

    validateTypes(type, 'int')

#actualizar variable de control validando que si sea un int tambien
def p_initFor(t):
    '''initFor : TO
    '''
    global Ptipos
    global VControl
    global PilaO
    global Cuadruplos
    global Ops

    exp_type = Ptipos.pop()
    validateTypes(exp_type, 'int')
    if PilaO:
        exp = PilaO.pop()
        VControl = PilaO[-1]
        Cuadruplos.append(Cuad(Ops['='], exp, -1, VControl))


# validar que la condición sea valida, actualizar la varaible que dicta el final y hacer el go to en falso
def p_beforeDo(t):
    '''beforeDo : DO
    '''
    global Ptipos
    global PilaO
    global VFinal
    global VControl
    global PJumps
    global Cuadruplos
    global Ops

    if Ptipos and PilaO:
        tiex = Ptipos.pop()
        validateTypes(tiex, 'int')
        exp = PilaO.pop()
        VFinal = getVDirTemp('int')
        Cuadruplos.append(Cuad(Ops['='], exp, -1, VFinal))
        tx = getVDirTemp('bool')
        Cuadruplos.append(Cuad(Ops['<'], VControl, VFinal, tx))
        PJumps.append(len(Cuadruplos))
        Cuadruplos.append(Cuad(Ops['gotoF'], tx, -1, -99))
        PJumps.append(len(Cuadruplos))


#------------------------------------
#EXPRESIONES

#expresion
def p_exp(t):
    'exp : texp expp'
    t[0] = t[1]

#menor pioridad al or
def p_expp(t):
    '''expp : OR exp
            | empty
    '''

#tera expresion para prioridad del and
def p_texp(t):
    'texp : gexp texpp'
    t[0] = t[1]

def p_texpp(t):
    '''texpp : andCheck texp
             | empty
    '''
def p_andCheck(t):
    ''' andCheck : AND
    '''
    global POoper
    POoper.append(t[1])


#Gerneral expresion para operadores lógicos y ejecucion de ands
def p_gexp(t):
    'gexp : mexp gexpp'

    global POoper
    global PilaO
    global Ptipos
    global Cuadruplos

    if POoper:
        if POoper[-1] == 'and':
            rOp = PilaO.pop()
            rType = Ptipos.pop()
            lOp = PilaO.pop()
            lType = Ptipos.pop()
            op = POoper.pop()
            resType = isValidOp(rType, lType, op)
            resVdir = getVDirTemp(resType)
            Cuadruplos.append(Cuad(Ops[op], lOp, rOp, resVdir))
            PilaO.append(resVdir)
            Ptipos.append(resType)
    
    t[0] = t[1]

def p_gexpp(t):
    '''gexpp : addPO mexp
             | empty
    '''
def p_addPO(t):
    '''addPO : MAYQ
             | MENQ
             | MAYI
             | MENI
             | IGUALIGUAL
             | DIF
             | NOT
    '''
    global POoper
    POoper.append(t[1])

#Mega expresion, precedencia de los operadores + | - y ejecución de logicos

def p_mexp(t):
    'mexp : termino mexpp'

    global POoper
    global PilaO
    global Ptipos
    global Cuadruplos

    opers = ['>', '<', '>=', '<=', '==', '!=']

    if POoper:
        if POoper[-1] in opers:
            rOp = PilaO.pop()
            rType = Ptipos.pop()
            lOp = PilaO.pop()
            lType = Ptipos.pop()
            op = POoper.pop()
            resType = isValidOp(rType, lType, op)
            resVdir = getVDirTemp(resType)
            Cuadruplos.append(Cuad(Ops[op], lOp, rOp, resVdir))
            PilaO.append(resVdir)
            Ptipos.append(resType)

    t[0] = t[1]
# terminos de menor jerarquía

def p_mexpp(t):
    '''mexpp : operSR mexp
            | empty
    '''
# solo sumas o restas de terminos

def p_operSR(t):
    '''operSR : MENOS
              | MAS
    '''
    global POoper
    POoper.append(t[1])


#------------------------------------
#Termino
#precedencia de operadores * | / y ejecución de suma y resta

def p_termino(t):
    'termino : factor terminop'

    global POoper
    global PilaO
    global Ptipos
    global Cuadruplos
    global Ops

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
            Ptipos.append(resType)
    t[0] = t[1]
# segundo nivel de jerarquía

def p_terminop(t):
    '''terminop : oper termino
                | empty
    '''
# solo multiplicaciones y divisiones de factores

def p_oper(t):
    '''oper : DIV
            | POR
    '''
    global POoper
    POoper.append(t[1])

#--------------------------
#manejo de operaciones con parentesis
#uso de fondos falsos e implementacion de multiplicaciones y divisiones

def p_meteFondo(t):
    '''meteFondo : APAR'''
    global POoper

    POoper.append('~')

def p_sacaFondo(t):
    '''sacaFondo : CPAR'''
    global POoper

    POoper.pop()

def p_factor(t): 
    '''factor : meteFondo exp sacaFondo
              | ctes
    '''
    global PilaO
    global Ptipos
    global POoper
    global Cuadruplos
    global Ops
    global tablaConstantes

    
    if len(t) == 2:

        vDir = fetchVDir(t[1])
        if not vDir >= 46000 and vDir <50000:
            PilaO.append(vDir)
            Ptipos.append(getValType(t[1]))
        if isarray(t[1]):
           PilaO.pop()



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
            Ptipos.append(resType)

# para expresiones anidadas entre paréntesis
# para id's , elemento de vector y llamadas de función
# constantes directas

#--------------------
# manejo de expresiones con llamadas a funcion, indexamiento o sencillas
def p_factorp(t):
    '''factorp : APAR createEra factorParams cparParams
               | ididx
    '''

#cargar parametros para llamada a funcion
def p_factorParams(t):
    '''factorParams : exp valParams factorpp
                    | empty
    '''


#validar que la firma esté completa, obtener datos de donde inicia la funcion, 
# su direccion virtual, su tipo, hacer el parche guadalupano y cuadruplo de gosub

def p_cparParams(t):
    '''cparParams : CPAR'''
    global ParameterTableList
    global contParams
    global Cuadruplos
    global Ops
    global mainFuncTable
    global globalVariables
    global funcName
    global POoper
    global Ptipos
    global PilaO

    POoper.pop()
    id = t[-4]

    cparam = contParams.pop()

    if len(ParameterTableList) != cparam:
        ERROR("Missing or too much parameters")
    
    initDir = mainFuncTable[id]['initFunc']
    funcDVir = globalVariables[id]['vDir']
    funcType = globalVariables[id]['tipo']
    temp = getVDirTemp(funcType)
    Cuadruplos.append(Cuad(Ops['gosub'], id, -1, initDir))
    Cuadruplos.append(Cuad(Ops['='], funcDVir, -1, temp))
    PilaO.append(temp)
    Ptipos.append(funcType)

#crear era para la creacion de memoria en la llamada

def p_createEra(t):
    '''createEra : '''
    global Cuadruplos
    global Ops
    global mainFuncTable
    global contParams
    global POoper
    global ParameterTable
    global ParameterTableList
    global PilaO
    global Ptipos
   

    POoper.append("~")
    id = (t[-3])
    Cuadruplos.append(Cuad(Ops['era'], -1, -1, id))
    contParams.append(0)

#valdiar el parametro que coincida con el tipo de la firma y llevar la cuenta de cuantos van de cuantos

def p_valParams(t):
    '''valParams : '''

    global contParamsInt
    global contParamsFloat
    global contParamsChar
    global ParameterTableList
    global PilaO
    global Ptipos
    global Cuadruplos
    global Ops
    global contParams
    global filaParams


    if PilaO and Ptipos and ParameterTableList:
        argument = PilaO.pop()
        argType = Ptipos.pop()

        cParam = contParams.pop()

        if argType != ParameterTableList[cParam]:
            ERROR("tipos distintos", t[-1])
        if argType == 'int':
            contParamsInt += 1
            Cuadruplos.append(Cuad(Ops['parameter'], argument, -1, filaParams[cParam]))    
        elif argType == 'float':
            contParamsFloat += 1
            Cuadruplos.append(Cuad(Ops['parameter'], argument, -1, filaParams[cParam]))
        elif argType == 'char':
            contParamsChar += 1
            Cuadruplos.append(Cuad(Ops['parameter'], argument, -1, filaParams[cParam]))
        contParams.append(cParam+1)

    else:
        if len(ParameterTableList) != contParams:
            ERROR("function had no parameters", t[-1])

#llamadas con multiples parametros

def p_factorpp(t):
    '''factorpp : COMA exp valParams factorpp
                | empty
    '''


#----------------------------------
#CONSTANTES 

#agregar a tabla de constantes, validar exitencia si fue un id 
def p_ctes(t):
    '''ctes : CTEC
            | CTEI
            | CTEF
            | ID validateExistance factorp
    '''
    global tablaConstantes
    global PilaO

    if len(t) == 2:
        if not t[1] in tablaConstantes:
            tablaConstantes[t[1]] = getVdirCTE(t[1])
    t[0] = t[1]

def p_validateExistance(t):
    '''validateExistance : '''
    validateExistance(t[-1])
    t[0] = t[-1]


#--------------------------
def p_empty(t):
    'empty :'
    pass
# Epsilon

#---------------------------
def p_error(t):
    print("Error sintáctico en '%s'" % t.value)
    print(t)
    sys.exit()
# decir en dónde hubo error de sintaxis

#****************************
# procesar archivo de input
import ply.yacc as yacc
parser = yacc.yacc()
f = open("./"+arch , "r")
input = f.read()
#print(input)
parser.parse(input, debug=0)
# print(localVariables)
# print(globalVariables)
# print(mainFuncTable)
# print(tablaConstantes)
# print(PilaO)
output = open("cuads.o", "w")
for c in Cuadruplos:
    #print(str(c.count) + " " + "Cuad --> " + str(c.op) + " " + str(c.dir1) + " " + str(c.dir2) + " " + str(c.recep))
    output.write(str(c.count) + "~" + str(c.op) + "~" + str(c.dir1) + "~" + str(c.dir2) + "~" + str(c.recep) + "\n")
output.close()