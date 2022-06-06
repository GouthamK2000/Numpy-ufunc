#Case-1-Trigonometric functions
import numpy as np

x=np.sin(np.pi/2) #Can use cos, tan as well
print(x)

#Case-2- Sin values for all values in an array

import numpy as np
arr=np.array([np.pi/2,np.pi/4,np.pi/6,np.pi/8])
x=np.sin(arr)
print(x)  #Prints the sin values for all the eleements in the array

#Case-3 -COnverting degrees to radians

import numpy as np

arr=np.array([np.pi/2,np.pi/4,np.pi/6,np.pi/8])
x=np.deg2rad(arr)
print(x)

#Case-4 -Radians to Degrees                        radians values are pi/180 * degree_values.

import numpy as np
arr=np.array([np.pi/2,np.pi/4,np.pi/6,np.pi/8])
x=np.rad2deg(arr)
print(x)

#Case-5-Finding Angles
# Finding angles from values of sine, cos, tan. 
# E.g. sin, cos and tan inverse (arcsin, arccos, arctan).


# NumPy provides ufuncs arcsin(), arccos() and arctan() that 
# produce radian values for corresponding sin, cos and tan values given.

import numpy as np
x=np.arcsin(1)
print(x)       #Outputs :1.5707963267948966

#Case-6- Finding angles of each value in an array

import numpy as np
arr=np.array([1,-1,0.1])
x=np.arcsin(arr)
print(x)   #Outputs : [ 1.57079633 -1.57079633  0.10016742]

#Case-7-Finding the hypotenuse


import numpy as np
base=4
perp=3
x=np.hypot(base,perp)
print(x) #Outputs :5.0
