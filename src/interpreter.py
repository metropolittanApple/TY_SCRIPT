# Interpreter file

from basic import Lexer

class Interpreter:
    def __init__(self, source):
        self.lexer = Lexer(source)
        self.tokens = self.lexer.make_tkns()

    def interpret(self):
        self.tokens_list = self.tokens

        print(self.tokens_list)
