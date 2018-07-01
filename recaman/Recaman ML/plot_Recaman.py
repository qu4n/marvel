import matplotlib.pyplot as plt
import numpy as np

#List of Recaman outputs
yValues = list()
#List of step sizes
xValues = list()


#Open a CSV file contain a (step size, recaman output) pair per line
with open('.\\Datasets\\RecamanTrainingData_100000.csv') as f:
    #Read in all lines in the file
    lines = f.readlines()

    '''
    '   Iterate through each line in the file and create list of x values and a 
    '   list of y values for plotting purposes.
    '''
    for line in lines:
        if len(line) > 1:
            line = line.strip()
            step,label = line.split(",")
            #step and label need coverted from strings to floats to properly plot
            xValues.append(float(step))
            yValues.append(float(label))


plt.plot(xValues,yValues)
plt.ylabel('Recaman Output (Labels)')
plt.xlabel('Step Size (Features)')
plt.show()





