import numpy as np


#输入层
x = np.array([2, 3, 1])
y_true = 1


#第1层参数
W1 = np.array([
    [0.5, 0.2, -1],
    [0.1, 0.8, 0.3],
    [-0.4, 0.2, 0.6],
    [0.7,-0.3,0.5]
])

b1 = np.array([0.5, 0.1, -0.2, 0.3])


#第2层参数
W2 = np.array([0.3,-0.5,0.8,0.2])
b2 = 0.2


#循环
for epoch in range(1000):

    z1 = np.dot(W1,x) + b1
    a1 = np.maximum(z1,0)

    z2 = np.dot(W2,a1) + b2
    y_pred = 1 / (1 + np.exp(-z2))

    #Loss
    loss = -(y_true * np.log(y_pred) + (1 - y_true)* np.log(1 - y_pred))

    #梯度1
    dL_dz2 = y_pred - y_true

    dL_dW2 = dL_dz2 * a1
    dL_db2 = dL_dz2

    #梯度2
    dL_da1 = dL_dz2 * W2
    dL_dz1 = dL_da1 * (z1 > 0)

    #梯度3
    dL_dW1 = np.outer(dL_dz1,x)
    dL_db1 = dL_dz1

    #update parameter1
    learning_rate = 0.1
    W1 = W1 - learning_rate * dL_dW1
    b1 = b1 - learning_rate * dL_db1

    W2 = W2 - learning_rate * dL_dW2
    b2 = b2 - learning_rate * dL_db2

    #判断结束
    if epoch % 100 == 0:
        print("epoch:",epoch,"loss:",loss,"y_pred:",y_pred)

print("final y_pred:",y_pred)
print("final loss:",loss)


 