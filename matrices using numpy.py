import numpy as np
s=5
v=np.array([5,-2,4])
m=np.array([[5,12,6],[-3,0,14]])
print(type(s))
print(type(v))
print(type(m))
s_array=np.array(s)
print(s_array)
print(v)
print(m)
print(m.shape)
print(v.shape)
print(s_array.shape)

#matrix operation
print('adding/subtracting matrices requires the same dimension. For example:')

m1=np.array([[5, -3, 2], [4, 8, 10], [24, -20, -5]])
m2=np.array([[-3, 2, 0.5], [-15, 10, -8], [-4, 12, 18]])
m3=m1+m2
print(m3)

# Dimensions: scalar has 1x1(Rank 0 Tensor); vector has mx1 (Rank 1 Tensor); matrix has mxn(Rank mxn Tensor); tensor has kxmxn dimension (Rank 3), collection of matrices

print('create a tensor:')
t=np.array([m1,m2])
print(t)
print(t.shape)

print('transposing a matrix')
A=np.array([[5,12,6],[-3,9,14]])
print(A)
print(A.T)

print('dot product')
b1=np.array([2,8,-4])
b2=np.array([1,-7,3])
b3=np.dot(b1,b2)
print(b3)

print('matrices with pi')
print(np.pi)
m_pi=([2/np.pi, np.pi/5, 1])
print(m_pi)

print('matrices with sine function')
x=45
m_sine=([np.sin(x), -2, np.pi/np.sin(x)])
print(m_sine)

#printing linspace
print(np.linspace(-2,2,num=5))


