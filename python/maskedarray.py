import numpy as np
import numpy.ma as MA
marr = MA.array(range(10), fill_value = -999)
print marr, marr.fill_value
marr[2] = MA.masked
print marr
print marr.mask
narr = MA.masked_where(marr > 6, marr)
print narr
x =  MA.filled
print x
print type(x)