from typing import List
from lex import mainFuncTable
from lex import tablaConstantes

f = open("cuads.o", "r")

cuads = f.read()
cuads = cuads.split("\n")
cuads = cuads[:-1]

for cuad in cuads:
    print(cuad)
print(mainFuncTable['MyRlike'])