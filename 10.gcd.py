#Case-1 -Finding gcd/hcf

import numpy as np

num1=12
num2=4
x=np.gcd(num1,num2)
print(x)  #Outputs :4

#Case-2 -GCD of a list of numbers

import numpy as np

arr=np.arange(1,20)
x=np.gcd.reduce(arr)
print(x) #Outputs : 1

#Case-3 -GCD of a list/array

import numpy as np

arr=np.array([4,2,8])
x=np.gcd.reduce(arr)
print(x) #Outputs :2