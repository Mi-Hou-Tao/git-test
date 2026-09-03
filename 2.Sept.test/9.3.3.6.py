import numpy as np

X = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])

y_true = np.array([0, 0, 0, 1, 0, 1, 1, 1])

def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

W1 = np.random.rand(3, 4) * 0.1
b1 = np.zeros(4)

W2 = np.random.rand(4, 1) * 0.1
b2 = np.zeros(1)

def calculate_loss(X, y_true, W1, b1, W2, b2):
    z1 = X @ W1 + b1
    a1 = relu(z1)

    z2 = a1 @ W2 + b2
    y_pred = sigmoid(z2)


    epsilon = 1e-8

    loss = -np.mean(
        y_true.reshape(-1, 1) * np.log(y_pred + epsilon) + (1 - y_true.reshape(-1, 1)) * np.log(1 - y_pred + epsilon)
    )
    return loss

loss = calculate_loss(X, y_true, W1, b1, W2, b2)
print("Loss:", loss)

learning_rate = 0.1
epsilon = 0.0001

for epoch in range(1000):
    gradient_W1 = np.zeros_like(W1)

    for i in range(W1.shape[0]):
        for j in range(W1.shape[1]):
            W1_plus = W1.copy()
            W1_minus = W1.copy()

            W1_plus[i, j] += epsilon
            W1_minus[i, j] -= epsilon

            loss_plus = calculate_loss(X, y_true, W1_plus, b1, W2, b2)
            loss_minus = calculate_loss(X, y_true, W1_minus, b1, W2, b2)

            gradient_W1[i, j] = (loss_plus - loss_minus) / (2 * epsilon)

    W1 = W1 - learning_rate * gradient_W1

    b1_plus = b1.copy()
    b1_minus = b1.copy()

    for i in range(b1.shape[0]):
        b1_plus[i] += epsilon
        b1_minus[i] -= epsilon

        loss_plus = calculate_loss(X, y_true, W1, b1_plus, W2, b2)
        loss_minus = calculate_loss(X, y_true, W1, b1_minus, W2, b2)

        gradient_b1 = (loss_plus - loss_minus) / (2 * epsilon)

        b1[i] = b1[i] - learning_rate * gradient_b1
gradient_W2 = np.zeros_like(W2)

for i in range(W2.shape[0]):
    W2_plus = W2.copy()
    W2_minus = W2.copy()

    W2_plus[i, 0] += epsilon
    W2_minus[i, 0] -= epsilon

    loss_plus = calculate_loss(X, y_true, W1, b1, W2_plus, b2)
    loss_minus = calculate_loss(X, y_true, W1, b1, W2_minus, b2)

    gradient_W2[i, 0] = (loss_plus - loss_minus) / (2 * epsilon)


W2 = W2 - learning_rate * gradient_W2


b2_plus = b2.copy()
b2_minus = b2.copy()

b2_plus[0] += epsilon
b2_minus[0] -= epsilon

loss_plus = calculate_loss(X, y_true, W1, b1, W2, b2_plus)
loss_minus = calculate_loss(X, y_true, W1, b1, W2, b2_minus)

gradient_b2 = (loss_plus - loss_minus) / (2 * epsilon)

b2 = b2 - learning_rate * gradient_b2

print("New loss:", calculate_loss(X, y_true, W1, b1, W2, b2))