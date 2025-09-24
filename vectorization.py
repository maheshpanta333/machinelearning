#   numpy tutorial for vectorization of multiple variable regression

import numpy as np
import matplotlib.pyplot as plt

# we create matrix with zero as elements with zeros with 4 as our number of elements
a=np.zeros(4)
print(a.shape)
print(a.dtype)


#variation_1
b=np.zeros((4,4))
print(b.shape)
print(b.dtype)

#another variation this generates random numbers from 0 to 1 and stores in the one dimensional matrix
c=np.random.random_sample(4)
print(c)
print(c.shape)
print(c.dtype)

#np.arrange just assigns value for example here we assigned from 0 to 6 by jumping 2 values 
a=np.arange(0,20,2)
print(a)

#we can also slice the values and access them
c=a[2:7:1] # here we go from 2 to 7 where 2 is inclusive and 7 is exclusive going one step each
print(c)

d=a[1:5:3]
print(d)


e=np.mean(a)
print(e)

f=a**3
print(f)


#rand and random_sample do the same thing as below but random sample takes size keyword as well
x=np.random.random_sample(size=(2,3))
print(x)

y=np.random.rand(2,3)
print(y)


#changes rows after one bracket closes acting as one list is for one row
z = np.array([[1],[2],[3],[4]])
print(z)
#in thits case to find the size just as we do in the pandas we use x[i].shape
print(x[1].shape)

#first creates 1-D array then reshapes it into newer size lets see what does minus sign does:
aa=np.arange(6).reshape(-1,2) #here -1 tells numpy to figure out dimension on its own so the total number of element still remains the same like 6/2 so it would be taking 3 as thet rows in the place of -1
print(aa)


a = np.arange(20).reshape(-1, 10)
print("a[:, 2:7:1] = \n", a[:, 2:7:1], ",  a[:, 2:7:1].shape =", a[:, 2:7:1].shape, "a 2-D array")
