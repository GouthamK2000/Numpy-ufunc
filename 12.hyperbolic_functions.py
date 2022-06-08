#Case-1-ufuncs for hyperbolic functions

import numpy as np

arr=np.sinh(np.pi/2)
print(arr)   

#Case-2-cos values for all the values in an array

import numpy as np

arr=np.array([np.pi/2,np.pi/4,np.pi/6,np.pi/8])
x=np.cosh(arr)
print(x)

#Case-3-Finding Angles

# Finding angles from values of hyperbolic sine, 
# cos, tan. E.g. sinh, cosh and tanh inverse (arcsinh, arccosh, arctanh).

# Numpy provides ufuncs arcsinh(), arccosh() and 
# arctanh() that produce radian values for corresponding sinh, cosh and tanh values given.

import numpy as np

x=np.arcsinh(1)
print(x)

#Case-4-FInding cos values for in an array

import numpy as np

arr=np.array([np.pi/2,np.pi/4,np.pi/6])
x=np.arctanh(arr)
print(x)