#Case-1 zip() method

arr1=[3,2,4,6]
arr2=[4,6,3,4]
ans=[]
for i,j in zip(arr1,arr2):
    ans.append(i+j)

print(ans)        #Prints the sum of both the arrays

#zip() methpod is used without the ufunc method

# #What is Vectorization?
# Converting iterative statements into a vector based operation is called vectorization.

# It is faster as modern CPUs are optimized for such operations.

#Case-2 - add(), which performs the same function as above

import numpy as np
arr1=[3,5,2,4,1]
arr2=[6,9,4,6,2]
x=np.add(arr1,arr2)
print(x)  #prints the addition of both the arrays


