## Hack Assembler

import hackparser
import hackcodegen

def assembler(filename):
    asmfilename = filename.split('\\')[-1]
    programname = asmfilename.split('.')[0]
    folderlist = filename.split('\\')[0:-1]
    folderlist = [s + '\\' for s in folderlist]
    folder = ''.join(folderlist)
    hackfilename = folder + programname + '.hack'
    
    asmfile = open(filename, 'r')
    hackfile = open(hackfilename, 'w')

    for line in asmfile:
        print line
        line = line.split('//', 1)[0]
        line = line.strip()
        if line == '':
            continue
        print line
        if hackparser.commandType(line) == 'A_COMMAND':
            value = dec2val(hackparser.symbol(line))
            hackfile.write('0' + value + '\n')
            print '0' + value
        elif hackparser.commandType(line) == 'C_COMMAND':
            bincmd = ('111' + hackcodegen.comp[hackparser.comp(line)] +
                      hackcodegen.dest[hackparser.dest(line)] +
                      hackcodegen.jmp[hackparser.jmp(line)])
            hackfile.write(bincmd + '\n')
            print bincmd

    asmfile.close()
    hackfile.close()
            
def dec2val(numstr):
    num = int(numstr)
    binnum = bin(num)
    binnum = binnum.split('b')[-1]
    binnum = binnum.zfill(15)
    binnum = binnum[-15:]
    return binnum
            
        
    
