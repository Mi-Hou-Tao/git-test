import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
from model import CNN

transform = transforms.ToTensor()

train_data = datasets.MNIST(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

train_loader = DataLoader(
    train_data,
    batch_size=64,
    shuffle=True
)



model = CNN()

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr=0.001)

for epoch in range(5):
    for images,labels in train_loader:
        output = model(images)
        loss = loss_fn(output,labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch + 1},Loss:{loss.item():.4f}")

test_data = datasets.MNIST(
    root="./data",
    train=False,
    download=True,
    transform=transform
)

test_loader = DataLoader(test_data,batch_size=64)

correct = 0
total = 0

with torch.no_grad():
    for images,labels in test_loader:
        output = model(images)

        predictions = output.argmax(dim=1)

        correct +=(predictions == labels).sum().item()
        total += labels.size(0)

accuracy = correct / total
print("测试集准确率：",accuracy)

