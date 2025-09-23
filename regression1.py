import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")


#taking input
x_train=np.array([[1.0,2.0]])
y_train=np.array([300,500.0])
print(f"x_train={x_train}")
print(f"y_train{y_train}")
print(f"x_train.shape:{x_train.shape}")
m=x_train.shape[0] #for multidimesional array we only take the zeroth index for the dimensino here ig
print(f"Number of training examples is: {m}")

plt.scatter(x_train,y_train, marker="x",c="b")

plt.title("Housing price")
plt.ylabel("Price (in 1000s of dollars)")
plt.xlabel("Size(1000 sq ft)")
plt.show()
#to train them we store them in coordinates
