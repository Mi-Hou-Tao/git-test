import torch
from torchvision import datasets,transforms

transforms = transforms.ToTensor()
train_data = datasets.MNIST(
    root="./data",
    train=True,
    download=True,
    transform=transform
)
