#Case-1 -Simple arithmetic

import numpy as np
arr1=[6,4,6,3]
arr2=[9,6,4,6]
newarr=np.add(arr1,arr2)  #use np.subtract,np.multiply,np.divide to perform the respective operations
print(newarr)

#Case-1 -Power
import numpy as np

arr1=[65,24,1234,13]
arr2=[1,2,3,4]
newarr=np.power(arr1,arr2)      #this function prints the power .
print(newarr)          

#Case-3 -modulus or remainder

import numpy as np

arr1=[8,6,5]
arr2=[7,4,3]
newarr=np.mod(arr1,arr2) #This prints the remeinder. np.remainder(), can also be used for performing the same operation.
print(newarr)

#Case-4 -To return both the quotient and the modulus

imort numpy as np

arr1=[5,4,3]
arr2=[7,6,5]
newarr=np.divmod(arr1,arr2)  #Here divmod function is used to perfor this operation.
print(newarr) # divmod function basically returns 2 arrays. the first array contains the quotient and second array contains the mod.

#Case-4-  Absolute value

import numpy as np
 arr1=[-4,-7,-8]
 newarr=np.absolute(arr1)
print(arr1)   #Absolute value means positive values. If any or all values are positive, then it returns the same element.