import sys
sys.path.append('configs')
sys.path.append('configs\\bns')
sys.path.append('src')
sys.path.append('src\\discretize')
sys.path.append('src\\models')
sys.path.append('src\\shared')


from dsShuffle import makeInference
if len(sys.argv) > 1:
    makeInference(sys.argv[1])
else:
    makeInference(None)
