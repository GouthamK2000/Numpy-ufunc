#Case-1 - Simple addition of 2 arrays

import numpy as np
arr1=[3,6,2]
arr2=[8,6,4]
newarr=np.add(arr1,arr2)
print(newarr)   #Adds both thae arrays to give a new array
#output :   [11 12  6]

#Case-2 -  sum of all the elements present in all the arrays

import numpy as np
arr1=[3,6,1]
arr2=[6,5,7]
newarr=np.sum([arr1,arr2])
print(newarr) # Outputs :28

#Case-3 -Sum of elements in each array

import numpy as np
arr1=[6,5,3]
arr2=[9,5,0]
newarr=np.sum([arr1,arr2],axis=1)
print(newarr)  #[14 14]

#Case-4 -Cumsum(Partial additon)

import numpy as np
arr=[8,6,5,4]
newarr=np.cunmsum(arr)
print(newarr)   #Outputs : [ 8 14 19 23]

#Cummulative Sum
# Cummulative sum means partially adding the elements in array.

# E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].

# Perfom partial sum with the cumsum() function.