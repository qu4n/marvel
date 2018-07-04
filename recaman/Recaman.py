# Recaman Object:
#   Returns a Recaman object with solved sequence up to n,
#   where n is the single constructor input argument.
#
#   Tested with python version 3.6.6
from operator import itemgetter
from collections import OrderedDict
import sys

sys.setrecursionlimit(16000)
class Recaman(object):
    ''' ATTRIBUTES '''
    sequence = {}

    ''' METHODS '''
    # constructor
    def __init__(self,n):
        super(Recaman, self).__init__()
        self.n = n
        self.solve(0,0)

    # recursive solution
    def solve(self,i,step):
        if(step<self.n):
            backStep = i - step
            if((backStep < 0) or (backStep in self.sequence)):
                forStep = i + step
                self.sequence[forStep] = step
                self.solve(forStep,step+1)
            else:
                self.sequence[backStep] = step
                self.solve(backStep,step+1)