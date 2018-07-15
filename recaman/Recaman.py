# Recaman Object:
#   Returns a Recaman object with solved sequence up to n,
#   where n is the single constructor input argument.
#
#   Tested with python version 3.6.6
from operator import itemgetter
from collections import OrderedDict
import sys

sys.setrecursionlimit(16000)
class Recaman:
    ''' ATTRIBUTES '''
    sequence = {}
    current_position = 0

    def solve(self,step,total_steps):
        if (step == total_steps):
            self.current_position = 0
            return
        
        backStep = self.current_position - step
        if((backStep < 0) or (backStep in self.sequence.values())):
            forStep = self.current_position + step
            self.sequence[step] = forStep
            self.current_position = forStep
            self.solve(step+1,total_steps)
        else:
            self.sequence[step] = backStep
            self.current_position = backStep
            self.solve(step+1,total_steps)