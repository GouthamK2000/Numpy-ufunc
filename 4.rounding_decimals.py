# Rounding Decimals
# There are primarily five ways of rounding off decimals in NumPy:

# truncation
# fix
# rounding
# floor
# ceil

#Case-1- truncation

import numpy as np

arr=np.trunc([-2.45,6.87])        #Here trunc() or fix() can be used...both provide the same result.
print(arr) #Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.

#Outputs : [-2.  6.]

#Case-2- rounding

import numpy as np

 arr=np.around([-2.45,6.87]) 
 print(arr)

# The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.

# E.g. round off to 1 decimal point, 3.16666 is 3.2
# Outputs : [-2.  7.]

#Case-3- floor

import numpy as np

ar=np.floor([-4.5,3.13])
print(ar)

# The floor() function rounds off decimal to nearest lower integer.

E.g. floor of 3.166 is 3.

#Outputs : [-5.  3.]

#Case-4- Ceil
import numpy as np

arr=np.ceil([-6.77,7.1])
print(arr)   
# Prints:[-6.  8.]
# The ceil() function rounds off decimal to nearest upper integer.

# E.g. ceil of 3.166 is 4.