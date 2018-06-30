import matplotlib.pyplot as plt
import numpy as np



recamanList = list()
xValues = list()

with open('C:\\Users\\DRock\\Documents\\GitHub\\marvel\\recaman\\Recaman ML\\Datasets\\RecamanTrainingData_30000') as f:
    lines = f.readlines()

    for line in lines:
        if len(line) > 1:
            line = line.strip()
            step,label = line.split(",")
            recamanList.append(float(label))
            xValues.append(float(step))


plt.plot(xValues,recamanList)
plt.ylabel('Recaman Output (labels)')
plt.xlabel('Step')
plt.show()





