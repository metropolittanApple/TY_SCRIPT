from basic import *

print('IOSCRIPT - 0.0.1')

while True:
    awns = input('IO >> ')

    if awns == '' or awns == 'quit':
        quit()

    lexer = Lexer(awns)
    lexer.make_tkns()