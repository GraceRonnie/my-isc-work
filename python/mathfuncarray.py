import numpy as np
def calcMagnitude(u, v, minmag = 0.1):
    mag = ((u**2) + (v**2))**0.5
    output = np.where(mag > minmag, mag, minmag)
    return output

#u = np.array([[4, 5, 6], [2, 3, 4]])
#v = np.array([[2, 2, 2], [1, 1, 1]])
#print calcMagnitude(u, v)

u = np.array([[4, 5, 0.01], [2, 3, 4]])
v = np.array([[2, 2, 0.03], [1, 1, 1]])
print calcMagnitude(u, v)
