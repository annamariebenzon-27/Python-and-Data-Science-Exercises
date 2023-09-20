import numpy as np
x=np.array([1, 2, 3, 4, 5, 6])
print('beginning x:\n',x)
x_reshape=x.reshape((2,3))
print('reshape x:\n', x_reshape)

#indexing the elements of the matrix. index starts at 0
print(x_reshape[0,0])
print(x_reshape[1,2])

#modifying x_reshape
print('x before we modify x_reshape:\n', x)
print('x_reshape before we modify x_reshape:\n', x_reshape)
x_reshape[0,0]=5
print('x_reshape after we modify its top left element:\n',x_reshape)
print('x after we modify top left element of x_reshape:\n', x)
y=x_reshape.T
print('The transpose of x_reshape is:\n ',y)


#sqrt and square of x
print('The sqrt of x is:\n', np.sqrt(x))
print('The square of x is:\n', x**2)

#random normal vairables with mean (loc)0 an standard deviation (scale) 1
z=np.random.normal(size=50)
print('The random normal with (loc) mean=0 and (scale)standard deviation=1 is: \n', z)

#adding an independent N(50,1) random variable to each element of z
z1=z+np.random.normal(loc=50, scale=1, size=50)
print('Adding and independent N(50,1) to each element of z:\n', z1)


#correlation between matrix z and z1. the off-diagonal elements give the correlation between z and z1
z2=np.corrcoef(z,z1)
print('The correlation between matrix z and z1 is:\n', z2)

#to ensure the code provides exactly the same results each it is run, we can set a random seed(rng.normal)
rng=np.random.default_rng(1303)
print(rng.normal(scale=5,size=2))
rng2=np.random.default_rng(1303)
print("To ensure the same random #:\n", rng2.normal(scale=5,size=2))

#to compute for the mean, variance and standard deviation use np.mean(), np.var(), and np.std()
rng=np.random.default_rng(3)
y=rng.standard_normal(10)
print('The mean:\n', np.mean(y),y.mean())
print('The variance is: \n', np.var(y), ',',y.var(),',', np.mean((y-y.mean())**2))
print('The standard deviation is: \n', np.sqrt(np.var(y)),',', np.std(y))  

#computing for the mean, variance and standard deviation of rows and columns of a matrix
X=rng.standard_normal((10,3))
print('The random matrix for 10x3 matrix: \n', X)

#getting the mean of the forst row or axis=0
X1=X.mean(axis=0)
X2=X.mean(0)
print('The mean of the first row:\n', X1,',s', X2)

#plotting
print('Plotting using matplotlib')
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplots
fig, ax=subplots(figsize=(8,8))
x=rng.standard_normal(100)
y=rng.standard_normal(100)
ax.plot(x,y)
plt.show()



#second approach
output=subplots(figsize=(8,8))
fig=output[0]
ax=output[1]

#testing---TESTING---
fig, ax=subplots(figsize=(8,8))
ax.plot(x,y,'o')
plt.show()

#to label plot
fig, ax=subplots(figsize=(8,8))
ax.scatter(x,y,marker='o')
ax.set_xlabel=("X-axis")
ax.set_ylabel=("Y-axis")
ax.set_title("Plot of X vs Y")

#changing the size
fig.set_size_inches(12,3)
fig

#creating 2x3 grid of plots in a figure
fig, axes=subplots(nrows=2,
                   ncols=3,
                   figsize=(15,5))
axes[0,1].plot(x,y,'o')
axes[1,2].scatter(x,y, marker="+")
fig

#to create x and y, we'll use the command np.linspace(a,b,n) which returns a vector of n numbers starting at a and ending at b
fig, ax=subplots(figsize=(8,8))
x=np.linspace(-np.pi,np.pi,50)
y=x
f=np.multiply.outer(np.cos(y),1/(1+x**2))
ax.contour(x,y,f)
#adding resolution
fig,ax=subplots(figsize=(8,8))
ax.contour(x,y,f, levels=45);
#fine-tune the output using ax.contour

fig, ax=subplots(figsize=(8,8))
ax.plot(x,y)
ax.imshow(f)
plt.show()





