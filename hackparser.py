## Hack Assembly Parser

allowed_non_alpha_char = ['_', '.', ':', '$', '0', '1', '-', '!']

def commandType(command):
    if command == '':
        return None
    if command[0] == '@':
        return 'A_COMMAND'
    elif command[0] == '(':
        return 'L_COMMAND'
    elif (command[0].isalpha() or command[0] in allowed_non_alpha_char):
        return 'C_COMMAND'
    else:
        return None

def symbol(command):
    if command[0] == '@':
        return command[1:]
    elif command[0] == '(':
        return command[1:-1]
    else:
        return None

def dest(command):
    if '=' in command:
        return command.split('=')[0]
    else:
        return 'null'

def comp(command):
    assign = (command.split(';')[0])
    return assign.split('=')[-1]

def jmp(command):
    if ';' in command:
        return (command.split(';')[-1])
    else:
        return 'null'
    



