#Case-1-Create your own ufunc

# To create you own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.

# The frompyfunc() method takes the following arguments:

# function - the name of the function.
# inputs - the number of input arguments (arrays).
# outputs - the number of output arrays.

import numpy as np

def myadd(x,y):
    return x+y

myadd=np.frompyfunc(myadd,2,1)
print(myadd([3,4,2],[8,6,4]))       #This prints the sum of both the arrays.

#Case-2- Check if it is a ufunc

import numpy as np

print(type(np.add)))           # this return  A ufunc should return <class 'numpy.ufunc'>.


#case-3 - What happens when  the function is not a ufunc?
import numpy as np

print(type(concatenate))       #Output: <class 'builtin_function_or_method'>

#Case-4, checking if something is a ufunc, using if else statemnt.

import numpy as np

if type(np.add)==ufunc:
    print("True")

else:
    print("False")