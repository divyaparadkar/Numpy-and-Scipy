
#2D array
import numpy as np
b= np.array([[1,2],[2,4]])
print(b)


#3D array 
c=[[[1,2,3,4],[2,5,6,7],[4,6,7,8],[5,7,9,0],[4,6,7,8],[5,6,7,0],[2,45,7,8]]]
d=np.array(c)
print(d)

b=d[0][0][1]
print(b)

e=d[1][0][3]
print(e)