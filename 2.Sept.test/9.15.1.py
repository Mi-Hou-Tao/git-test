import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import torch
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

transform = transforms.ToTensor()

train_data = datasets.MNIST(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

image,label = train_data[0]

print("训练集数量：", len(train_data))
print("图片形状：", image.shape)
print("标签：", label)

print("最大像素值：", image.max())
print("最小像素值：", image.min())

plt.imshow(image.squeeze(), cmap="gray", vmin=0, vmax=1)
plt.show()