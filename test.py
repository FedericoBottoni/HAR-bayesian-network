import sys
sys.path.append('configs')
sys.path.append('configs\\bns')
sys.path.append('src')
sys.path.append('src\\discretize')
sys.path.append('src\\models')
sys.path.append('src\\shared')

from dsShuffle import dsShuffle

if len(sys.argv) > 1:
    dsShuffle('test', int(sys.argv[1]))
else:
    raise Exception('No argument passed')