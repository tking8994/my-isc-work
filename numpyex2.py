import numpy as np

arr=np.array([range(4),range(10,14)])
print(arr)
print(arr.shape)
print(arr.size)
print(arr.max())
print(arr.min())


#part 2

print(np.reshape(arr,(2,2,2)))
print(np.ravel(arr))

print(np.float64(arr))
