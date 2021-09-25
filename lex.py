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