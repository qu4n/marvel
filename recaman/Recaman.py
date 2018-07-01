# Recaman Object:
#   Returns a Recaman object with solved sequence up to n,
#   where n is the single constructor input argument.
#
#   Tested with python version 3.6.6
class Recaman(object):
    ''' ATTRIBUTES '''
    sequence = {}

    ''' METHODS '''
    # constructor
    def __init__(self,n):
        super(Recaman, self).__init__()
        self.n = n
        self.sequence = {}
        self.solve(0,0)

    # recursive solution
    def solve(self,i,step):
        if(len(self.sequence)==self.n):
            return
        
        backStep = i - step
        forStep = i + step

        if((backStep < 0) or (backStep in self.sequence)):
            self.sequence[forStep] = step
            self.solve(forStep,step+1)
        else:
            self.sequence[backStep] = step
            self.solve(backStep,step+1)
    
    # get final sequence
    def getSequence(self):
        return list(self.sequence.keys())