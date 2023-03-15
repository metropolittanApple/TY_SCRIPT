# Convert input in to tokens

import os

TK_OPENPAREN = 'OPENPAREN'
TK_CLOSEPAREN = 'CLOSEPAREN'
TK_NUMBER = 'NUMBER'
TK_PLUS = 'PLUS'
TK_MINUS = 'MINUS'
TK_MUL = 'MUL'
TK_DIV = 'DIV'
TK_VAR = 'VAR'
DIGITS = '0123456789'

try:
    from colorama import Fore

except:
    os.system('pip3 install colorama')

class Error:
    def __init__(self, type):
        self.type = type

    def UnrecognizedChar(current_char):
        print(Fore.RED + f'>> ERROR: Unrecognized character found in source: {current_char}')
        quit(1)

class Token:
    def __init__(self, type):
        self.type = type

class Lexer:
    def __init__(self, source):
        self.source = list(source)

    def make_tkns(self):
        tokens = []

        while not tokens:

            for token in self.source:

                if token == '(':
                    tokens.append(Token(TK_OPENPAREN))
                    self.source.pop(0)
                
                elif token == ')':
                    tokens.append(Token(TK_CLOSEPAREN))
                    self.source.pop(0)

                elif token in DIGITS:
                    tokens.append(Token(TK_NUMBER))
                    self.source.pop(0)

                elif token == '+':
                    tokens.append(Token(TK_PLUS))
                    self.source.pop(0)
                
                elif token == '-':
                    tokens.append(Token(TK_MINUS))
                    self.source.pop(0)

                elif token == '*':
                    tokens.append(Token(TK_MUL))
                    self.source.pop(0)
                
                elif token == '/':
                    tokens.append(Token(TK_DIV))
                    self.source.pop(0)

                elif token == 'var':
                    tokens.append(Token(TK_VAR))
                    self.source.pop(0)

                # Skip chars
                
                elif token == ' ':
                    self.source.pop(0)
                elif token == '\t':
                    self.source.pop(0)
                elif token == '\n':
                    self.source.pop(0)

                else:
                    # The character was illegal.
                    return Error.UnrecognizedChar(token)

        return tokens