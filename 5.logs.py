# Logs
# NumPy provides functions to perform log at the base 2, e and 10.

# We will also explore how we can take log for any base by creating a custom ufunc.

# All of the log functions will place -inf or inf in the elements if the log can not be computed.

#Case-1-Basic logs

import numpy as np

arr=np.arange(1,10)  #The arange(1, 10) function returns an array with integers starting from 1 (included) to 10 (not included).
print(np.log2(arr))   #np.log10 can be used in place of log2, if we want to calculate log to the base 10.

# np.log can be used to perform logarithm to the base e.

#Case-2 log at any base

from math import log10
import numpy as np

nplog=np.frompyfunc(log,2,1)
print(nplog(100,15))

#It has 2 input parameters and 1 output.

#numpy.frompyfunc(func, nin, nout) function allows to create an arbitrary Python function as Numpy ufunc (universal function).