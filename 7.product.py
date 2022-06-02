#Case-1- Basic multiplication

import numpy as np
arr=np.array([6,1,7,4])
pro=np.prod(arr)
print(pro)          #Output: 168

#With 2 arrays

import numpy as np

arr=np.array([2,3,4,5])
arr1=np.array([1,2,3,4])
pro=np.prod([arr1,arr])
print(pro)    #Outputs :  2880


#Case-2 - TO return product of each array, in an array

import numpy as np

arr1=np.array([1,2,3])
arr2=np.array([5,6,7])
arr=np.prod([arr1,arr2],axis=1)
print(arr)
#Outputs : [  6 210]

#Case-3-Cumproduct

# Cummulative Product
# Cummulative product means taking the product partially.

# E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]

# Perfom partial sum with the cumprod() function.

import numpy as np

arr1=np.array([7,5,6])
arr=np.cumpord(arr1)
print(arr)    #Outputs :[  7  35 210]

