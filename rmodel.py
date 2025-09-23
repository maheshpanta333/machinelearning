import math, copy
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

#first we take data itself
x_train=np.array([1.0,2.0])
y_train=np.array([300,500])

#now first we compute cost function which is very essential for w and b later
def compute_cost(x,y,w,b):
    #first we see total number of sets of data we have
    m=x.shape[0]
    #since we know in cost function we iterate over m times we create variable cost and init it to 0 to iterate over all elements to sum them up
    cost=0
    #running sum iteration
    for i in range(m):
        f_wb=w*x[i]+b
        cost=cost+(f_wb-y[i])**2
    total_cost=(1/(2*m))*cost
    return total_cost


#now we create function to find gradient that would later be used to approximate valoues of w and b for the linear regression 
def compute_gradient(x,y,w,b):
    #as always first step is to find number of training examples
    m=x.shape[0]
    dj_dw=0
    dj_db=0 #these are what we require generally
    for i in range(m):
        f_wb=w*x[i]+b
        dj_dw_i=(f_wb-y[i])*x[i]
        dj_db_i=(f_wb-y[i])
        dj_dw+=dj_dw_i
        dj_db+=dj_db_i
    dj_dw=dj_dw/m
    dj_db=dj_db/m
    return dj_dw, dj_db

#to calculate w and b with least of the errors this is what we do
def gradient_descent(x,y,w_in,b_in,alpha,num_iters):
    b=b_in
    w=w_in
    for i in range(num_iters):
        #we calulate first gradient by calling the functoin itsef
        dj_dw, dj_db=compute_gradient(x,y,w,b)
        w=w-alpha*dj_dw
        b=b-alpha*dj_db
    return w,b


#now we call all the functions and values:
w_init=0
b_init=0
iterations=1000
tmp_alpha=1.0e-2
w_final,b_final=gradient_descent(x_train,y_train,w_init,b_init,tmp_alpha,iterations)
print(f"Final function is f_wb={w_final}x+{b_final}")
x_input=float(input("Emter the size of house and i shall predict its cost: "))
y_output=w_final*x_input+b_final
print(f"Well for house of size {x_input}ft will be ${y_output}!")
