import numpy as np
x=list(range(1,11))
print(x)
a1=np.array(x,dtype=np.int)
print(a1)
a2=np.array(x,dtype=np.float64)
print(a2)




#ex2

y=np.zeros((2,3,4))
print(y)
z=np.ones((2,3,4))
print(z)

b=np.arange(1,1000,1)
print(b)

#ex3

l=[2,3.2,5.5,-6.4,-2.2,2.4]
c=np.array(l,dtype=np.float64)
print(c)
print(c[1:4])
print(c[1])

d=[[2,3.2,5.5,-6.4,-2.2,2.4],[1,22,4,0.1,5.3,-9],[3,1,2.1,21,1.1,-2]]
e1=np.array(d,dtype=np.float64)
print(e1)
