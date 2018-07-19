from Recaman import Recaman
import matplotlib.pyplot as plt
import numpy as np
import time

t = time.time()
%time r = Recaman(100)
t = time.time() - t
print(t)
print(r.sequence)

plt.plot(list(r.sequence.keys()),list(r.sequence.values()))
plt.show()