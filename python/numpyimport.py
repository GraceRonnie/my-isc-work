import numpy as np
x = range(1, 11)
a1 = np.array(x, np.int32)
a2 = np.array(x, np.float32)
print a1.dtype #returns int32 as the data type
print a2.dtype #returns float32 as the data type

print a1 #returns [ 1  2  3  4  5  6  7  8  9 10] NB: does not include 11

print a2 #returns [  1.   2.   3.   4.   5.   6.   7.   8.   9.  10.]