#Case-1 -LCM

import numpy as np
num1= 23
num2=12
x=np.lcm(num1,num2)
print(x)  #Outputs: 276

#Case-2 -LCM in arrays

import numpy as np

arr=np.array([7,5,6,4])
x=np.lcm.reduce(arr)    #Reduce function reduces the array to 1D
print(x)  #Outputs :420

#Case-3-LCM in a range of numbers

import numpy as np

arr=np.arange(1,5)
x=np.lcm.reduce(arr)
print(x) #Outputs : 12