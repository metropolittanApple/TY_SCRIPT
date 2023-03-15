from interpreter import Interpreter

print('')
print('                             TY SCRIPT - 0.0.1\n')
print('                           ██████████████████████')
print('')
while True:
    awns = input('TY >> ')

    interpreter = Interpreter(awns)

    interpreter.interpret()

    if awns == '' or awns == 'quit':
        quit()