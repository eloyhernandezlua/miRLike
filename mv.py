import sys
from typing import List
from lex import mainFuncTable
from lex import especiales
from lex import tablaConstantes
import sys
import statistics
import matplotlib.pyplot as plt

#leer archivo donde viene codigo intermedio
f = open("cuads.o", "r")

cuads = f.read()
cuads = cuads.split("\n")
cuads = cuads[:-1]


#donde se van a manejar las memorias
execStack = []

#variables globales 
isGlobal = True
PC = 0
savedPC = []

#imprimir errores y parar programa

def ERROR(tipo, at=""):
    print("ERROR: ", tipo, " @ -->", at)
    sys.exit()

#obtener el valor de la constante a partir de una direccion virtual

def getCTE(val):
    global tablaConstantes
    for key, value in tablaConstantes.items():
         if val == value:
             return key
 
    ERROR("No existe", val)

#validar si se puede leer hacia un tipo de variable en particular

def isReadable(var, val):
    global isGlobal

    if isGlobal:
        
        if var < 5000 and var >= 2000:
            try:
                val = int(val)
            except:
                ERROR("TYPE MISMATCH", val)
        elif var < 9000 and var >= 5000:
            try:
                val = float(val)
            except: 
                ERROR("TYPE MISMATCH", val)
        elif var < 12000 and var >= 9000:
            if len(val) > 1:
                ERROR("NOT A SINGLE CHAR", val)
            val = str(val)
        else:
            ERROR("TYPE MISMATCH", val)

#validar que la dirección que quiere accesar si tenga ya un valor asignado

def checkForNone(val, cuad):
    global isGlobal
    
    if val is None:
        ERROR("Trying to use none values", cuad)

#cargar la memoria a maquina virtual, ahora la direccion es la llave y el valor es el correcto
def loadMemoria(pName):
    for elemento in mainFuncTable[pName]['vars']:
        dVir = mainFuncTable[pName]['vars'][elemento]['vDir']
        currentMemory.mem[dVir] = None

#chechar si la direccion corresponde a un arreglo
def checkforArray(val):
    return val >= 50000

#doble indexamiento para un arreglo
def fromArray(idx):
    
    global isGlobal
    if isGlobal:
        try:
            return int(memoriaGlobal.mem[idx])
        except:
            print("el idx --> ", idx)
            print(memoriaGlobal.mem)
            return idx
    else:
        try:
            return currentMemory.mem[idx]
        except:
            print("el idx --> ", idx)
            print(currentMemory.mem)
            return idx
        
#verificar si esta en memoria local

def isInLocal(val):

    try:
        currentMemory.mem[val]
        return True
    except:
        return False

#ver si está en memoria globlal

def isInGlobal(val):
    try:
        memoriaGlobal.mem[val]
        return True
    except:
        # print(memoriaGlobal.mem)
        ERROR("Unexisting value", str(val))

#ver si estuvo en la ultima memoria local antes de hacer un cambio de contexto
def isInPastLocal(val):
    global execStack
    try:
        execStack[-1].mem[val]
        return True
    except:
        return False

#template de memoria
class Memoria:
    def __init__(self):
        self.mem = {}

#cargar nombre del programa

for i in mainFuncTable.keys():
    if mainFuncTable[i]['scope'] == 'g':
        programName = i

#inicializar memorias
memoriaGlobal = Memoria()
currentMemory = None

#Cargar memoria global
for elemento in mainFuncTable[programName]['vars']:
    dVir = mainFuncTable[programName]['vars'][elemento]['vDir']
    memoriaGlobal.mem[dVir] = None

#cargar constatnes a memoria glboal
for elememnto in tablaConstantes:
    dVir = tablaConstantes[elememnto]
    if dVir < 40000:
        memoriaGlobal.mem[dVir] = int(elememnto)
    elif dVir < 43000:
        memoriaGlobal.mem[dVir] = float(elememnto)
    elif dVir < 46000:
        memoriaGlobal.mem[dVir] = str(elememnto) 


#prints para debugging:  cer los cuadruplos, lo que recibe de funciones y constantes

# print("\n", mainFuncTable)
# print("\n", tablaConstantes)

# for cuad in cuads:
#     print(cuad.split('~'))

# print(memoriaGlobal.mem)


#mientras el PC siga en rango, hará cuadruplos

while PC <= len(cuads):
    #fragmentar el cuadruplo a algo entendible

    (idx, op, dir1, dir2, res) = cuads[PC].split("~")

    #MAS prints solo para debugging
    # print(PC+1, "<---- Cuad a ejecutar" )
    # if isGlobal:
    #     print("Global")
    #     print(memoriaGlobal.mem)
    #     if currentMemory is not None:
    #         print("Local")
    #         print(currentMemory.mem)
    # else:
    #     print("Local")
    #     print(currentMemory.mem)

    # print(PC+1, " IS GLOBAL --> ", isGlobal)


    #go to
    if int(op) == 14:
        PC = int(res) - 2
    elif int(op) == 11:
        if checkforArray(int(res)):
                res = fromArray(int(res))
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)], int(dir1))
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)]
        else:
            try:
                checkForNone(currentMemory.mem[int(dir1)], int(dir1))
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)]
            except:
                checkForNone(memoriaGlobal.mem[int(dir1)], int(dir1))
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)]
    #suma
    elif int(op) == 1:
        if checkforArray(int(dir1)):
            dir1 = fromArray(int(dir1))
        if checkforArray(int(dir2)):
            dir2 = fromArray(int(dir2))
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)], 1)
            checkForNone(memoriaGlobal.mem[int(dir2)], 1)
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] + memoriaGlobal.mem[int(dir2)]
        else:
            if isInLocal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] + currentMemory.mem[int(dir2)]
            elif isInLocal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] + memoriaGlobal.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] + currentMemory.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] + memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values")
    #multiplicacion
    elif int(op) == 3:
        if checkforArray(int(dir1)):
            dir1 = fromArray(int(dir1))
        if checkforArray(int(dir2)):
            dir2 = fromArray(int(dir2))
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)], 3)
            checkForNone(memoriaGlobal.mem[int(dir2)], 3)
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] * memoriaGlobal.mem[int(dir2)]
        else:
            if isInLocal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] * currentMemory.mem[int(dir2)]
            elif isInLocal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] * memoriaGlobal.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] * currentMemory.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInGlobal(int(dir2)):
                
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] * memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values")
    # escritura
    elif int(op) == 12:
        if res[0] == '"':
            print(res[1:-1])
        elif isGlobal:
            if checkforArray(int(res)):
                res = fromArray(int(res))
            print(memoriaGlobal.mem[int(res)])
        else: 
            if checkforArray(int(res)):
                res = fromArray(int(res))
            try:
                print(currentMemory.mem[int(res)])
            except:
                print(memoriaGlobal.mem[int(res)])
    #resta
    elif int(op) == 2:
        # if checkforArray(int(res)):
        #     res = fromArray(int(res))
        if checkforArray(int(dir1)):
            dir1 = fromArray(int(dir1))
        if checkforArray(int(dir2)):
            dir2 = fromArray(int(dir2))
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)], 2)
            checkForNone(memoriaGlobal.mem[int(dir2)], 2)
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] - memoriaGlobal.mem[int(dir2)]
        else:
            if len(execStack) > 0:
                if isInPastLocal(int(dir1)) and isInPastLocal(int(dir2)):
                    execStack[-1].mem[int(res)] = execStack[-1].mem[int(dir1)] - execStack[-1].mem[int(dir2)]
                elif isInPastLocal(int(dir1)) and isInGlobal(int(dir2)):
                    execStack[-1].mem[int(res)] = execStack[-1].mem[int(dir1)] - memoriaGlobal.mem[int(dir2)]
                elif isInGlobal(int(dir1)) and isInPastLocal(int(dir2)):
                    execStack[-1].mem[int(res)] = memoriaGlobal.mem[int(dir1)] - execStack[-1].mem[int(dir2)]
                elif isInGlobal(int(dir1)) and isInGlobal(int(dir2)):
                    execStack[-1].mem[int(res)] = memoriaGlobal.mem[int(dir1)] - memoriaGlobal.mem[int(dir2)]
                else:
                    ERROR("Trying to use none values")
            else:     
                if isInLocal(int(dir1)) and isInLocal(int(dir2)):
                    currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] - currentMemory.mem[int(dir2)]
                elif isInLocal(int(dir1)) and isInGlobal(int(dir2)):
                    currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] - memoriaGlobal.mem[int(dir2)]
                elif isInGlobal(int(dir1)) and isInLocal(int(dir2)):
                    currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] - currentMemory.mem[int(dir2)]
                elif isInGlobal(int(dir1)) and isInGlobal(int(dir2)):
                    currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] - memoriaGlobal.mem[int(dir2)]
                else:
                    ERROR("Trying to use none values")
    #division
    elif int(op) == 4:
        if checkforArray(int(dir1)):
            dir1 = fromArray(int(dir1))
        if checkforArray(int(dir2)):
            dir2 = fromArray(int(dir2))
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)], 4)
            checkForNone(memoriaGlobal.mem[int(dir2)], 4)
            if type(memoriaGlobal.mem[int(dir1)]) == int and type(memoriaGlobal.mem[int(dir2)]) == int:
                memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] // memoriaGlobal.mem[int(dir2)]
            else:
                memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] / memoriaGlobal.mem[int(dir2)]
        else:
            if isInLocal(int(dir1)) and isInLocal(int(dir2)):
                if type(currentMemory.mem[int(dir1)]) == int and type(currentMemory.mem[int(dir2)]) == int:
                    currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] // currentMemory.mem[int(dir2)]
                else:
                    currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] / currentMemory.mem[int(dir2)]
            elif isInLocal(int(dir1)) and isInGlobal(int(dir2)):
                if type(currentMemory.mem[int(dir1)]) == int and type(memoriaGlobal.mem[int(dir2)]) == int:
                    currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] // memoriaGlobal.mem[int(dir2)]
                else:
                    currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] / memoriaGlobal.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInLocal(int(dir2)):
                if type(memoriaGlobal.mem[int(dir1)]) == int and type(currentMemory.mem[int(dir2)]) == int:
                    currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] // currentMemory.mem[int(dir2)]
                else:
                    currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] / currentMemory.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInGlobal(int(dir2)):
                if type(memoriaGlobal.mem[int(dir1)]) == int and type(memoriaGlobal.mem[int(dir2)]) == int:
                    currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] // memoriaGlobal.mem[int(dir2)]
                else:
                    currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] / memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values")
    #mayor que
    elif int(op) == 7:
        if checkforArray(int(dir1)):
            dir1 = fromArray(int(dir1))
        if checkforArray(int(dir2)):
            dir2 = fromArray(int(dir2))
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)], 7)
            checkForNone(memoriaGlobal.mem[int(dir2)], 7)
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] > memoriaGlobal.mem[int(dir2)]   
        else:
            if isInLocal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] > currentMemory.mem[int(dir2)]
            elif isInLocal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] > memoriaGlobal.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] > currentMemory.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] > memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values")   
    #go to en falso
    elif int(op) == 15:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)], 15)
            if not memoriaGlobal.mem[int(dir1)]:
                PC = int(res) - 2
        else:
            if isInLocal(int(dir1)):
                checkForNone(currentMemory.mem[int(dir1)], 15)
                if not currentMemory.mem[int(dir1)]:
                    PC = int(res) - 2
            elif isInGlobal(int(dir1)):
                checkForNone(memoriaGlobal.mem[int(dir1)], 15)
                if not memoriaGlobal.mem[int(dir1)]:
                    PC = int(res) - 2
    #igual igual
    elif int(op) == 5:
        if checkforArray(int(dir1)):
            dir1 = fromArray(int(dir1))
        if checkforArray(int(dir2)):
            dir2 = fromArray(int(dir2))
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)], 5)
            checkForNone(memoriaGlobal.mem[int(dir2)], 5)
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] == memoriaGlobal.mem[int(dir2)]  
        else:
            if checkforArray(int(dir1)):
                dir1 = fromArray(int(dir1))
            if checkforArray(int(dir2)):
                dir2 = fromArray(int(dir2))
            if isInLocal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] == currentMemory.mem[int(dir2)]
            elif isInLocal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] == memoriaGlobal.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInLocal(int(dir2)):
                
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] == currentMemory.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] == memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values")
    #menor que
    elif int(op) == 6:
        if checkforArray(int(dir1)):
            dir1 = fromArray(int(dir1))
        if checkforArray(int(dir2)):
            dir2 = fromArray(int(dir2))
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)], 6)
            checkForNone(memoriaGlobal.mem[int(dir2)], 6)
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] < memoriaGlobal.mem[int(dir2)]  
        else:
            if isInLocal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] < currentMemory.mem[int(dir2)]
            elif isInLocal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] < memoriaGlobal.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] < currentMemory.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] < memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values")  
    #menor o igual
    elif int(op) == 8:
        if checkforArray(int(dir1)):
            dir1 = fromArray(int(dir1))
        if checkforArray(int(dir2)):
            dir2 = fromArray(int(dir2))
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)], 8)
            checkForNone(memoriaGlobal.mem[int(dir2)], 8)
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] <= memoriaGlobal.mem[int(dir2)]  
        else:
            if isInLocal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] <= currentMemory.mem[int(dir2)]
            elif isInLocal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] <= memoriaGlobal.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] <= currentMemory.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] <= memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values")
    #mayor o igual
    elif int(op) == 9:
        if checkforArray(int(dir1)):
            dir1 = fromArray(int(dir1))
        if checkforArray(int(dir2)):
            dir2 = fromArray(int(dir2))
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)], 9)
            checkForNone(memoriaGlobal.mem[int(dir2)], 9)
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] >= memoriaGlobal.mem[int(dir2)]  
        else:
            if isInLocal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] >= currentMemory.mem[int(dir2)]
            elif isInLocal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] >= memoriaGlobal.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] >= currentMemory.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] >= memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values")
    #diferente
    elif int(op) == 10:
        if checkforArray(int(dir1)):
            dir1 = fromArray(int(dir1))
        if checkforArray(int(dir2)):
            dir2 = fromArray(int(dir2))
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)], 10)
            checkForNone(memoriaGlobal.mem[int(dir2)], 10)
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] != memoriaGlobal.mem[int(dir2)]  
        else:
            if isInLocal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] != currentMemory.mem[int(dir2)]
            elif isInLocal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] != memoriaGlobal.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] != currentMemory.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] != memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values")
    #go to en true
    elif int(op) == 16:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)], 15)
            if memoriaGlobal.mem[int(dir1)]:
                PC = int(res) - 2
        else:
            if isInLocal(int(dir1)):
                checkForNone(currentMemory.mem[int(dir1)], 15)
                if currentMemory.mem[int(dir1)]:
                    PC = int(res) - 2
            elif isInGlobal(int(dir1)):
                checkForNone(memoriaGlobal.mem[int(dir1)], 15)
                if memoriaGlobal.mem[int(dir1)]:
                    PC = int(res) - 2
    #lectura
    elif int(op) == 13:
        if checkforArray(int(res)):
            res = fromArray(int(res))
        if isGlobal:
            val = input()
            isReadable(int(res), val)
            memoriaGlobal.mem[int(res)] = val
        else:
            val = input()
            isReadable(int(res), val)
            if isInLocal(int(res)):
                currentMemory.mem[int(res)] = val
            elif isInGlobal(int(res)):
                memoriaGlobal.mem[int(res)] = val
    #and
    elif int(op) == 18:
        if checkforArray(int(dir1)):
            dir1 = fromArray(int(dir1))
        if checkforArray(int(dir2)):
            dir2 = fromArray(int(dir2))
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)], 18)
            checkForNone(memoriaGlobal.mem[int(dir2)], 18)
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] and memoriaGlobal.mem[int(dir2)] 
        else:
            if isInLocal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] and currentMemory.mem[int(dir2)]
            elif isInLocal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] and memoriaGlobal.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] and currentMemory.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] and memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values")
    #or
    elif int(op) == 19:
        if checkforArray(int(dir1)):
            dir1 = fromArray(int(dir1))
        if checkforArray(int(dir2)):
            dir2 = fromArray(int(dir2))
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)], 19)
            checkForNone(memoriaGlobal.mem[int(dir2)], 19)
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] or memoriaGlobal.mem[int(dir2)] 
        else:
            if isInLocal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] or currentMemory.mem[int(dir2)]
            elif isInLocal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] or memoriaGlobal.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] or currentMemory.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] or memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values")
    #end function
    elif int(op) == 20:
        if execStack:
            currentMemory = execStack.pop()
        else:
            isGlobal = True
        PC = savedPC.pop()
    #era
    elif int(op) == 21:
        if currentMemory is not None:
            execStack.append(currentMemory)
            currentMemory = Memoria()
            loadMemoria(res)
        else:
            currentMemory = Memoria()
            loadMemoria(res)
    #go sub
    elif int(op) == 23:
        isGlobal = False
        savedPC.append(PC + 1)
        PC = int(res) - 2
    #return 
    elif int(op) == 17:
        if checkforArray(int(dir1)):
            dir1 = fromArray(int(dir1))
        if isInLocal(int(dir1)):
            
            memoriaGlobal.mem[int(res)] = currentMemory.mem[int(dir1)]
        elif isInGlobal(int(dir1)):
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)]
        if not execStack:
            isGlobal = True  
        if execStack:
            currentMemory = execStack.pop()
        PC = savedPC.pop() - 1
    #parametro
    elif int(op) == 22:
        if checkforArray(int(dir1)):
            dir1 = fromArray(int(dir1))
        if checkforArray(int(dir2)):
            dir2 = fromArray(int(dir2))
        if isGlobal:
            currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)]
        else:
            if isInPastLocal(int(dir1)):
                currentMemory.mem[int(res)] = execStack[-1].mem[int(dir1)]
            elif isInGlobal(int(dir1)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)]
    # verificar indice arreglo        
    elif int(op) == 24:
        if isGlobal:
            if memoriaGlobal.mem[int(dir1)] >= memoriaGlobal.mem[int(res)] or memoriaGlobal.mem[int(dir1)] < 0:
                ERROR("INDEX OUT OF BOUNDS", dir1)
        else:
            if isInLocal(int(dir1)):

                if currentMemory.mem[int(dir1)] >= memoriaGlobal.mem[int(res)] or memoriaGlobal.mem[int(dir2)] < 0:
                    ERROR("INDEX OUT OF BOUNDS", dir1)
            elif isInGlobal(int(dir1)):
                if memoriaGlobal.mem[int(dir1)] >= memoriaGlobal.mem[int(res)] or memoriaGlobal.mem[int(dir2)] < 0:
                    ERROR("INDEX OUT OF BOUNDS", dir1)
    #media
    elif int(op) == 25:
        print(statistics.mean(especiales[int(res)]))
    #media harmonica
    elif int(op) == 26:
        print(statistics.harmonic_mean(especiales[int(res)]))
    #mediana
    elif int(op) == 27:
        print(statistics.median(especiales[int(res)]))
    #mediana de grupo
    elif int(op) == 28:
        print(statistics.median_grouped(especiales[int(res)]))
    #moda
    elif int(op) == 29:
        print(statistics.mode(especiales[int(res)]))
    #deviación poblacional
    elif int(op) == 30:
        print(statistics.pstdev(especiales[int(res)]))
    #desviacion estandar
    elif int(op) == 31:
        print(statistics.stdev(especiales[int(res)]))
    #varianza poblacional
    elif int(op) == 32:
        print(statistics.pvariance(especiales[int(res)]))
    #varianza
    elif int(op) == 33:
        print(statistics.variance(especiales[int(res)]))
    #plot
    elif int(op) == 34:
        # pip uninstall matplotlib
        # python3 -m pip install matplotlib
        # si no jala por alguna razón matplot lib correr esto en terminal
        plt.plot(especiales[int(res)])    
        plt.show()

    #ir al siguiente cuádruplo
    PC += 1

    #a menos de que haya sido el último
    if PC == len(cuads):
        sys.exit()

    
    







