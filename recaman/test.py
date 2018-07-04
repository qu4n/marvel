from Recaman import Recaman
import matplotlib.pyplot as plt
import numpy as np
import time

t = time.time()
r = Recaman(15000)
t = time.time() - t
print(t)
#print(r.sequence)

#plt.plot(list(r.sequence.values()),list(r.sequence.keys()))
plt.plot(list(r.sequence.keys()),list(r.sequence.values()))
plt.show()