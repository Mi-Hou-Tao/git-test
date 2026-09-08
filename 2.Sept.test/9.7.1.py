import numpy as np

x = np.array([2,3,1])
y_true = 1

W1 = np.array([
        [0.5,0.2,-1],
        [0.1,0.8,0.3],
        [-0.4,0.2,0.6],
        [0.7,-0.3,0.5]
])
            
b1 = np.array([0.5,0.1,-0.2,0.3])
W2 = np.array([0.3,-0.5,0.8,0.2])
b2 = 0.2

for epoch in range(1000):
    z1 = np.dot(W1,x) + b1
    a1 = np.maximum(z1,0)
    z2 = np.dot(W2,a1) + b2
    y_pred = 1 / (1 + np.exp(-z2))
    loss = -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

    dl_dz2 = y_pred - y_true
    dl_dW2 = dl_dz2 * a1
    dl_db2 = dl_dz2

    dl_da1 = dl_dz2 * W2
    dl_dz1 = dl_da1 * (z1 > 0)

    dl_dW1 = np.outer(dl_dz1,x)
    dl_db1 = dl_dz1

    learning_rate = 0.1
    W1 = W1 - learning_rate * dl_dW1
    b1 = b1 - learning_rate * dl_db1
    W2 = W2 - learning_rate * dl_dW2
    b2 = b2 - learning_rate * dl_db2

    if epoch % 100 == 0:
        print("epoch:",epoch,"loss:",loss,"y_pred:",y_pred)

print("final loss:",loss)
print("final y_pred:",y_pred)