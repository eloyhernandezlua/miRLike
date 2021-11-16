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

def ERROR(tipo, at=""):
    print("ERROR: ", tipo, " @ -->", at)
    sys.exit()


def getCTE(val):
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

def checkForNone(val):
    global isGlobal
    
    if val is None:
        ERROR("Trying to use none values")

def loadMemoria(pName):
    for elemento in mainFuncTable[pName]['vars']:
        dVir = mainFuncTable[pName]['vars'][elemento]['vDir']
        currentMemory.mem[dVir] = None

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
    #print(PC+1, "<---- Cuad a ejecutar" )

    if int(op) == 14:
        PC = int(res) - 2
    elif int(op) == 11:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)])
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)]
    elif int(op) == 1:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)])
            checkForNone(memoriaGlobal.mem[int(dir2)])
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] + memoriaGlobal.mem[int(dir2)]
    elif int(op) == 3:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)])
            checkForNone(memoriaGlobal.mem[int(dir2)])
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] * memoriaGlobal.mem[int(dir2)]
    elif int(op) == 12:
        if res[0] == '"':
            print(res[1:-1])
        elif isGlobal:
            print(memoriaGlobal.mem[int(res)])
    elif int(op) == 2:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)])
            checkForNone(memoriaGlobal.mem[int(dir2)])
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] - memoriaGlobal.mem[int(dir2)]
    elif int(op) == 4:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)])
            checkForNone(memoriaGlobal.mem[int(dir2)])
            if type(memoriaGlobal.mem[int(dir1)]) and type(memoriaGlobal.mem[int(dir2)]) == int:
                memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] // memoriaGlobal.mem[int(dir2)]
            else:
                 memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] / memoriaGlobal.mem[int(dir2)]
    elif int(op) == 7:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)])
            checkForNone(memoriaGlobal.mem[int(dir2)])
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] > memoriaGlobal.mem[int(dir2)]   
    elif int(op) == 15:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)])
            if not memoriaGlobal.mem[int(dir1)]:
                PC = int(res) - 2
    elif int(op) == 5:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)])
            checkForNone(memoriaGlobal.mem[int(dir2)])
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] == memoriaGlobal.mem[int(dir2)]  
    elif int(op) == 6:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)])
            checkForNone(memoriaGlobal.mem[int(dir2)])
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] < memoriaGlobal.mem[int(dir2)]  
    elif int(op) == 8:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)])
            checkForNone(memoriaGlobal.mem[int(dir2)])
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] <= memoriaGlobal.mem[int(dir2)]  
    elif int(op) == 9:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)])
            checkForNone(memoriaGlobal.mem[int(dir2)])
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] >= memoriaGlobal.mem[int(dir2)]  
    elif int(op) == 10:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)])
            checkForNone(memoriaGlobal.mem[int(dir2)])
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] != memoriaGlobal.mem[int(dir2)]  
    elif int(op) == 25:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)])
            checkForNone(memoriaGlobal.mem[int(dir2)])
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] != memoriaGlobal.mem[int(dir2)]  
    elif int(op) == 16:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)])
            if memoriaGlobal.mem[int(dir1)]:
                PC = int(res) - 2
    elif int(op) == 13:
        if isGlobal:
            val = input()
            isReadable(int(res), val)
            memoriaGlobal.mem[int(res)] = val
    elif int(op) == 18:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)])
            checkForNone(memoriaGlobal.mem[int(dir2)])
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] and memoriaGlobal.mem[int(dir2)] 
    elif int(op) == 19:
        if isGlobal:
            checkForNone(memoriaGlobal.mem[int(dir1)])
            checkForNone(memoriaGlobal.mem[int(dir2)])
            memoriaGlobal.mem[int(res)] = memoriaGlobal.mem[int(dir1)] or memoriaGlobal.mem[int(dir2)] 
    elif int(op) == 20:
        if execStack:
            currentMemory = execStack.pop()
        else:
            isGlobal = True
        
    elif int(op) == 21:
        isGlobal = False
        if currentMemory is not None:
            execStack.append(currentMemory)
            currentMemory = Memoria()
            loadMemoria(res)
            print(currentMemory.mem)
        else:
            currentMemory = Memoria()
            loadMemoria(res)
            print(currentMemory.mem)

    


    

    PC += 1

    if PC == len(cuads):
        sys.exit()

print(memoriaGlobal.mem)
    
    







