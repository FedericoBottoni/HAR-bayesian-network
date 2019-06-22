import sys
import numpy
sys.path.append('configs')
sys.path.append('configs\\bns')
sys.path.append('src')
sys.path.append('src\\discretize')
sys.path.append('src\\models')
sys.path.append('src\\shared')

from dsShuffle import dsShuffle

numpy.set_printoptions(precision=None, threshold=sys.maxsize, suppress="true", floatmode="maxprec_equal")
dsShuffle('pomSkeleton', None)
