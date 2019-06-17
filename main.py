import sys
sys.path.append('configs')
sys.path.append('src')
sys.path.append('src\models')
sys.path.append('src\shared')

modes = ['pgm', 'pomegranate']
def parseModName(mod):
    if mod in modes:
        return mod
    else:
        return modes[0]

from dsShuffle import dsShuffle
dsShuffle(parseModName(sys.argv[1]) if len(sys.argv) > 1 else modes[0])
