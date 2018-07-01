# Recaman Object:
#   Provides the Recaman sequence solutoins up to n
#   input: integer n, represents the nth term of the sequence
#   returns: Recaman Object
#
#   Tested with python version 3.6.6
class Recaman(object):
    ''' ATTRIBUTES '''
    sequence = []

    ''' METHODS '''
    # constructor inits
    def __init__(self, n):
        super(Recaman, self).__init__()
        self.n = n
        self.sequence = [0]*n
        self.solve()

    # Solve first n terms of Recaman sequence
    def solve(self):
        self.sequence[0] = 0
        step = 0

        # Fill remaining terms using
        # recursive formula.
        for i in range(1, self.n):
            step += 1
            curr = self.sequence[i-1] - i
            for j in range(0, i):
                # If sequence[i-1] - i is
                # negative or already
                # exists.
                if ((self.sequence[j] == curr) or curr < 0):
                    curr = self.sequence[i-1] + i
                    break
            self.sequence[i] = curr
