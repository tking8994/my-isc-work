import numpy as np
a=np.array([range(4),range(10,14)])
print(np.reshape(a,(2,4)))
b=np.array([2,-1,1,0])
print(b)
print(np.multiply(a,b))
b1=(np.multiply(b,100))
print(b1)
b2=(np.multiply(b,100.0))
print(b2)
print(b1==b2)
#print(dir(b1))
#print(dir(b2))

#part 2

arr=np.array([range(10)])
print(arr)
print(np.greater(arr,3))
#print(np.less(arr,3))
#print(arr>=3)
#print(3>arr, arr>8) # and (arr<8)
condition= np.logical_or(arr< 3, arr> 8)
print(np.where(condition, arr*5, arr*-5))
