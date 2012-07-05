## Hack Assembler

import hackparser
import hackcodegen
import hacksymtab

def assembler(filename):
    asmfilename = filename.split('\\')[-1]
    programname = asmfilename.split('.')[0]
    folderlist = filename.split('\\')[0:-1]
    folderlist = [s + '\\' for s in folderlist]
    folder = ''.join(folderlist)
    hackfilename = folder + programname + '.hack'
    
    asmfile = open(filename, 'r')
    hackfile = open(hackfilename, 'w')

    symtab = hacksymtab.HackSymbolTable()

    ## First pass
    ROMaddr = 0
    for line in asmfile:
        line = (line.split('//', 1)[0])
        line = line.strip()
        if line == '':
            continue
        commandType = hackparser.commandType(line)
        if (commandType == 'A_COMMAND' or commandType == 'C_COMMAND'):
            ROMaddr += 1
        elif commandType == 'L_COMMAND':
            assert not symtab.contains(hackparser.symbol(line))
            symtab.addEntry(hackparser.symbol(line), ROMaddr + 1)

    asmfile.close()
    asmfile = open(filename, 'r')
        
    ## Second pass
    nextfreeRAM = 16
    for line in asmfile:
        print line
        line = (line.split('//', 1)[0])
        line = line.strip()
        if line == '':
            continue
        print line
        if hackparser.commandType(line) == 'A_COMMAND':
            if line[1].isdigit():
                value = str(line[1:])
            else:
                symbol = hackparser.symbol(line)
                if symtab.contains(symbol):
                    value = str(symtab.getAddress(symbol))
                else:
                    symtab.addEntry(symbol, nextfreeRAM)
                    value = str(nextfreeRAM)
                    nextfreeRAM += 1
            hackfile.write('0' + dec2val(value) + '\n')
            print '0' + dec2val(value)
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
            
        
    
