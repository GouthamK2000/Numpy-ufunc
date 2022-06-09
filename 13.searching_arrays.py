#Case-1- where() method

import numpy as np
arr=np.array([7,4,5,3,4,5,2,6,7])
x=np.where(arr==4)
print(x)  #Outputs :(array([1, 4], dtype=int64),)

#Case-2-Finding odds

import numpy as np

arr=np.array([2,3,6,2,4,9,19])
x=np.where(arr%2==1)
print(x)          #Outputs. Similarly it can be doen for even numbers

#Case-3-searchsorted(), which performs binary search

import numpy as np

arr=np.array([5,7,9,1,6,7,2])
x=np.searchsorted(arr,5) # the name of the array and the element that needs to be searched is entered here.
print(x) #Outputs :4 (positon after sorting)

#Same programmme, to find the position of an element from the right

import numpy as np

arr=np.array([5,7,9,1,6,7,2])
x=np.searchsorted(arr,5,side='right')
print(x) #Outputs :4 (Position of thr mentioned eleemnt after sorting, from the right)

#Case-4-Finding indexes where specified numbers should be inserted

import numpy as np

arr=np.array([3,4,8,2,9,1,6,3,6])
x=np.searchsorted(arr,[5,7])
print(x)             #Outputs:  [2 9]  , these are the positions that the specified eleemnts will be put into.

