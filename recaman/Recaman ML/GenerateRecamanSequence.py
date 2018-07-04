# Python 3 program to print n-th
# number in Recaman's sequence
 
# Prints first n terms of Recaman
# sequence
def recaman(n,f):
 
    # Create an array to store terms
    arr = [0] * n
 
    # First term of the sequence
    # is always 0
    arr[0] = 0
    step = 0
    f.write(str(step) + "," + str(arr[0]) + "\n")
 
    # Fill remaining terms using
    # recursive formula.
    for i in range(1, n):
     
        step += 1
        curr = arr[i-1] - i
        for j in range(0, i):
         
            # If arr[i-1] - i is
            # negative or already
            # exists.
            if ((arr[j] == curr) or curr < 0):
                curr = arr[i-1] + i
                break
             
        arr[i] = curr
        f.write(str(step) + "," + str(arr[i]) + "\n")
 
# Driver code
n = 200
f = open('RecamanTrainingData_' + str(n) + '.csv','w')
 
recaman(n, f)
f.close()
 
# This code is contributed by Smitha.