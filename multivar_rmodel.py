import matplotlib.pyplot as plt
import numpy as np
import math,copy

#our original data sets 
x_train = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]])
y_train = np.array([460, 232, 178])

#intial w and b value for the regressio model would be as follows
w_init=np.array([ 0.39133535, 18.75376741, -53.36032453, -26.42131618])
b_init=785.1811367994083

#we now create function for creating the function which we can do by manulaly performing dot product but using dot product from np library is generally better and faster
def predict(x,w,b):
    p=np.dot(x,w)+b
    return p

#for x we know we have multi-dimensional matrix but we send row first so we get rows only by slicing
x_vec=x_train[0,:]
f_wb=predict(x_vec,w_init,b_init)

def compute_cost(x,y,w,b):
    m=x.shape[0];
    cost=0.0
    for i in range(m):
        f_wb_i=np.dot(x[i],w)+b
        cost+=(f_wb_i-y[i])**2
    cost=cost/(2*m)
    return cost


cost=compute_cost(x_train,y_train,w_init,b_init)


#we also need to evaluate gradient
def compute_gradien(x,y,w,b):
    m,n=x.shape
    dj_dw=np.zeros((n,))
    dj_db=0

    for i in range(m):
        #directly find error rather than creating function first 
        #we calculate errors for each rows
        err=((np.dot(x[i],w)+b)-y[i])
        for j in range(n):
            #then what we do is multiply that each error to all values of x[i][j] and summmate it to each column separately 
            dj_dw[j]=dj_dw[j]+err*x[i][j]
            #then we sum all the change in one column so we calculate different dj_dw for one column separately in one rows by multiplying errors to the x element of the column itself
        dj_db=dj_db+err
    dj_db/=m
    dj_dw/=m
    return dj_db,dj_dw

#now we figure out actual w and b
def gradient_descent(x,y,w_in,b_in,alpha,num_itrs):
    w=copy.deepcopy(w_in)#just creating duplicate w to prevent chainging global w
    b=b_in
    for i in range(num_itrs):
        dj_db,dj_dw=compute_gradien(x,y,w,b)
        w=w-alpha*dj_dw
        b=b-alpha*dj_db

    return w,b

#everything is here same as single variable
initial_w=np.zeros_like(w_init)
initial_b=0
iterations=1000
alpha=5.0e-7
w_final, b_final = gradient_descent(x_train, y_train, initial_w, initial_b,alpha, iterations)
print(f"b,w found by gradient descent: {b_final:0.2f},{w_final} ")
m,_ = x_train.shape
#this here just shows from our data what is predicted vs what is the target datat
for i in range(m):
    print(f"prediction: {np.dot(x_train[i], w_final) + b_final:0.2f}, target value: {y_train[i]}")
