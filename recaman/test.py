from Recaman import Recaman
import matplotlib.pyplot as plt
import numpy as np
import time

t = time.time()
r = Recaman()
r.solve(0,4000)
t = time.time() - t
f = open("seq.txt",'w')
f.write(str(t))
f.write(str(r.sequence))
f.close()

#plt.plot(list(r.sequence.keys()),list(r.sequence.values()))
#plt.show()