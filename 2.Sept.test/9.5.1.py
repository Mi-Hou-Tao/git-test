import numpy as np

#输入层
x = np.array([2, 3, 1])
W1 = np.array([
    [0.5, 0.2, -1],
    [0.1, 0.8, 0.3],
    [-0.4, 0.2, 0.6],
    [0.7,-0.3,0.5]
])
b1 = np.array([0.5, 0.1, -0.2, 0.3])

#隐藏层1（ReLU)
z1 = np.dot(W1,x) + b1
a1 = np.maximum(z1, 0)

#输出层
W2 = np.array([0.3,-0.5,0.8,0.2])
b2 = 0.2
z2 = np.dot(W2,a1) + b2

#Sigmoid
y_pred = 1 / (1 + np.exp(-z2))
print("y_pred:",y_pred)
y_true = 1

#Loss
loss = -(y_true * np.log(y_pred) + (1 - y_true)* np.log(1 - y_pred))
print("Loss:",loss)

#梯度
dL_dz2 = y_pred - y_true
dL_dW2 = dL_dz2 * a1
dL_db2 = dL_dz2
print("dL/dz2:",dL_dz2)
print("dL/dW2:",dL_dW2)
print("dL/db2:",dL_db2)

#update parameter
learning_rate = 0.1
W2 = W2 - learning_rate * dL_dW2
b2 = b2 - learning_rate * dL_db2
print("updated W2:",W2)
print("updated b2:",b2)

#前向传播
z2 = np.dot(W2,a1) + b2
y_pred = 1 / (1 + np.exp(-z2))

loss = -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
print("updated y_pred:",y_pred)
print("updated loss:",loss)

