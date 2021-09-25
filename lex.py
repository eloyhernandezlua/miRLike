import re

#reserved words

reserved = {

}

#tokens

tokens = [

] + list(reserved.values())


#types

#Build lexer
import ply.lex as lex

#Gramatic rules

import ply.yacc as yacc
parser = yacc.yacc()

f = open("./pass.txt", "r")
input = f.read()
print(input)
parser.parse(input)