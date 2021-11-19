import sys
from typing import List
from lex import mainFuncTable
from lex import tablaConstantes
import sys

f = open("cuads.o", "r")

execStack = []

cuads = f.read()
cuads = cuads.split("\n")
cuads = cuads[:-1]

isGlobal = True
PC = 0
savedPC = []

def ERROR(tipo, at=""):
    print("ERROR: ", tipo, " @ -->", at)
    sys.exit()


def getCTE(val):
    global tablaConstantes
    for key, value in tablaConstantes.items():
         if val == value:
             return key
 
    ERROR("No existe", val)

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
            val = str(val)
        else:
            ERROR("TYPE MISMATCH", val)

def checkForNone(val, cuad):
    global isGlobal
    
    if val is None:
        ERROR("Trying to use none values", cuad)

def loadMemoria(pName):
    for elemento in mainFuncTable[pName]['vars']:
        dVir = mainFuncTable[pName]['vars'][elemento]['vDir']
        currentMemory.mem[dVir] = None


def isInLocal(val):
    try:
        currentMemory.mem[val]
        return True
    except:
        return False

def isInGlobal(val):
    try:
        memoriaGlobal.mem[val]
        return True
    except:
        ERROR("Unexisting value")


class Memoria:
    def __init__(self):
        self.mem = {}

for i in mainFuncTable.keys():
    if mainFuncTable[i]['scope'] == 'g':
        programName = i

memoriaGlobal = Memoria()
currentMemory = None

for elemento in mainFuncTable[programName]['vars']:
    dVir = mainFuncTable[programName]['vars'][elemento]['vDir']
    memoriaGlobal.mem[dVir] = None

for elememnto in tablaConstantes:
    dVir = tablaConstantes[elememnto]
    if dVir < 40000:
        memoriaGlobal.mem[dVir] = int(elememnto)
    elif dVir < 43000:
        memoriaGlobal.mem[dVir] = float(elememnto)
    elif dVir < 46000:
        memoriaGlobal.mem[dVir] = str(elememnto) 

# print("\n", mainFuncTable)
# print("\n", tablaConstantes)

# for cuad in cuads:
#     print(cuad.split('~'))

# print(memoriaGlobal.mem)

while PC <= len(cuads):
    (idx, op, dir1, dir2, res) = cuads[PC].split("~")
    # print(PC+1, "<---- Cuad a ejecutar" )
    # if isGlobal:
    #     print(memoriaGlobal.mem)
    #     if currentMemory is not None:
    #         print(currentMemory.mem)

    if int(op) == 14:
        PC = int(res) - 2
    elif int(op) == 11:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)], 11)
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)]
        else:
            try:
                checkForNone(currentMemory.mem[int(dir1)], 11)
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)]
            except:
                checkForNone(memoriaGlobal.mem[int(dir1)], 11)
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)]
    elif int(op) == 1:
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
            elif isGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] + memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values", cuad)

    elif int(op) == 3:
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
            elif isGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] * memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values", cuad)
    elif int(op) == 12:
        if res[0] == '"':
            print(res[1:-1])
        elif isGlobal:
            print(memoriaGlobal.mem[int(res)])
        else: 
            try:
                print(currentMemory.mem[int(res)])
            except:
                print(memoriaGlobal.mem[int(res)])
    elif int(op) == 2:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)], 2)
            checkForNone(memoriaGlobal.mem[int(dir2)], 2)
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] - memoriaGlobal.mem[int(dir2)]
        else:
            if isInLocal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] - currentMemory.mem[int(dir2)]
            elif isInLocal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] - memoriaGlobal.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] - currentMemory.mem[int(dir2)]
            elif isGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] - memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values", cuad)
    elif int(op) == 4:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)], 4)
            checkForNone(memoriaGlobal.mem[int(dir2)], 4)
            #memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] / memoriaGlobal.mem[int(dir2)]
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
            elif isGlobal(int(dir1)) and isInGlobal(int(dir2)):
                if type(memoriaGlobal.mem[int(dir1)]) == int and type(memoriaGlobal.mem[int(dir2)]) == int:
                    currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] // memoriaGlobal.mem[int(dir2)]
                else:
                    currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] / memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values", cuad)
    elif int(op) == 7:
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
            elif isGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] > memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values", cuad)   
    elif int(op) == 15:
        checkForNone(memoriaGlobal.mem[int(dir1)], 15)
        if not memoriaGlobal.mem[int(dir1)]:
            PC = int(res) - 2
    elif int(op) == 5:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)], 5)
            checkForNone(memoriaGlobal.mem[int(dir2)], 5)
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] == memoriaGlobal.mem[int(dir2)]  
        else:
            if isInLocal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] == currentMemory.mem[int(dir2)]
            elif isInLocal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = currentMemory.mem[int(dir1)] == memoriaGlobal.mem[int(dir2)]
            elif isInGlobal(int(dir1)) and isInLocal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] == currentMemory.mem[int(dir2)]
            elif isGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] == memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values", cuad)
    elif int(op) == 6:
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
            elif isGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] < memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values", cuad)  
    elif int(op) == 8:
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
            elif isGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] <= memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values", cuad)
    elif int(op) == 9:
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
            elif isGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] >= memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values", cuad)
    elif int(op) == 10:
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
            elif isGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] != memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values", cuad)
    elif int(op) == 16:
        checkForNone(memoriaGlobal.mem[int(dir1)], 16)
        if memoriaGlobal.mem[int(dir1)]:
            PC = int(res) - 2
    elif int(op) == 13:
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
    elif int(op) == 18:
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
            elif isGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] and memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values", cuad)
    elif int(op) == 19:
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
            elif isGlobal(int(dir1)) and isInGlobal(int(dir2)):
                currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)] or memoriaGlobal.mem[int(dir2)]
            else:
                ERROR("Trying to use none values", cuad)
    elif int(op) == 20:
        if execStack:
            currentMemory = execStack.pop()
        else:
            isGlobal = True
        PC = savedPC.pop()
    elif int(op) == 21:
        if currentMemory is not None:
            execStack.append(currentMemory)
            currentMemory = Memoria()
            loadMemoria(res)
        else:
            currentMemory = Memoria()
            loadMemoria(res)
            # print(memoriaGlobal.mem)
            # print(currentMemory.mem)
    elif int(op) == 23:
        isGlobal = False
        savedPC.append(PC)
        PC = int(res) - 2
    elif int(op) == 17:
        if isInLocal(int(dir1)):
            memoriaGlobal.mem[int(res)] = currentMemory.mem[int(dir1)]
        elif isInGlobal(int(dir1)):
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)]
        PC = savedPC.pop()
    elif int(op) == 22:
        currentMemory.mem[int(res)] = memoriaGlobal.mem[int(dir1)]
    elif int(op) == 24:
        if isGlobal:
            if memoriaGlobal.mem[int(dir1)] >= memoriaGlobal.mem[int(res)] or memoriaGlobal.mem[int(dir1)] < 0:
                ERROR("INDEX OUT OF BOUNDS", dir1)
        else:
            if isInLocal(currentMemory.mem[int(dir1)]):
                if currentMemory.mem[int(dir1)] >= memoriaGlobal.mem[int(res)] or memoriaGlobal.mem[int(dir1)] < 0:
                    ERROR("INDEX OUT OF BOUNDS", dir1)
            elif isInGlobal(memoriaGlobal.mem[int(dir1)]):
                if memoriaGlobal.mem[int(dir1)] >= memoriaGlobal.mem[int(res)] or memoriaGlobal.mem[int(dir1)] < 0:
                    ERROR("INDEX OUT OF BOUNDS", dir1)

    

    PC += 1

    if PC == len(cuads):
        # print(memoriaGlobal.mem)
        sys.exit()

    
    







