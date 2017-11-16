import numpy as np
arr =  np.arange(10)
print arr < 3
print np.less(arr, 3)
condition = np.logical_or(arr < 3, arr > 8)
new_arr = np.where(condition, arr * 5, arr * -5)
print new_arr