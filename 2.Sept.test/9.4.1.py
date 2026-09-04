import numpy as np

x = np.array([2, 3, 1])
W1 = np.array([
    [0.5, 0.2, -1],
    [0.1, 0.8, 0.3],
    [-0.4, 0.2, 0.6],
    [0.7,-0.3,0.5]
])
b1 = np.array([0.5, 0.1, -0.2, 0.3])

z1 = np.dot(W1,x) + b1

a1 = np.maximum(z1, 0)

print(z1)
print(a1)