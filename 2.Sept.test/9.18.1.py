import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import torch
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

from model import CNN
from preprocess import preprocess_image


# 1. 加载微调后的模型
model = CNN()

model.load_state_dict(
    torch.load(
        "mnist_cnn_my_digits.pth",
        weights_only=True
    )
)

model.eval()


# 2. 找到测试图片
root = Path("test_my_digits_dark")

correct = 0
total = 0

wrong = []

# 创建 10×10 的混淆矩阵
confusion_matrix = np.zeros((10, 10), dtype=int)


# 3. 一张一张进行预测
for digit in range(10):

    folder = root / str(digit)

    for image_path in folder.glob("*.png"):

        # 文件夹名称就是正确答案
        true_label = digit

        # 预处理
        image = preprocess_image(image_path)

        # 预测
        with torch.no_grad():

            output = model(image.unsqueeze(0))

            prediction = output.argmax(dim=1).item()

        # 统计
        total += 1

        if prediction == true_label:
            correct += 1

        else:
            wrong.append(
                (image_path, true_label, prediction)
            )

        # 混淆矩阵
        confusion_matrix[true_label][prediction] += 1


# 4. 计算准确率
accuracy = correct / total

print("总图片数量：", total)
print("预测正确：", correct)
print("预测错误：", total - correct)
print("准确率：", accuracy)
print("准确率：", f"{accuracy * 100:.2f}%")


# 5. 输出错误样本
print("\n错误样本：")

for image_path, true_label, prediction in wrong:

    print(
        f"{image_path}："
        f"真实={true_label}，"
        f"预测={prediction}"
    )


# 6. 输出混淆矩阵
print("\n混淆矩阵：")
print(confusion_matrix)


# 7. 显示混淆矩阵
plt.figure(figsize=(8, 8))

plt.imshow(confusion_matrix)

plt.colorbar()

plt.xticks(range(10))
plt.yticks(range(10))

plt.xlabel("预测数字")
plt.ylabel("真实数字")

plt.title("手写数字识别混淆矩阵")

# 在每个格子里显示数字
for i in range(10):
    for j in range(10):

        plt.text(
            j,
            i,
            confusion_matrix[i, j],
            ha="center",
            va="center"
        )

plt.show()
# 8. 显示错误样本

if len(wrong) > 0:

    plt.figure(figsize=(10, 3))

    for i, (image_path, true_label, prediction) in enumerate(wrong):

        image = plt.imread(image_path)

        plt.subplot(1, len(wrong), i + 1)

        plt.imshow(image, cmap="gray")

        plt.title(
            f"真实:{true_label}\n预测:{prediction}"
        )

        plt.axis("off")

    plt.show()



# 查看暗光图片经过预处理后的效果

paths = [
    "test_my_digits/3/3_04.png",
    "test_my_digits/4/4_03.png",
    "test_my_digits/5/5_03.png",
    "test_my_digits/9/9_03.png",
    "test_my_digits/7/7_10.png"
]

plt.figure(figsize=(10, 2))

for i, path in enumerate(paths):

    image = preprocess_image(path)

    plt.subplot(1, 5, i + 1)

    plt.imshow(image.squeeze(), cmap="gray")

    plt.title(path.split("/")[-1])

    plt.axis("off")

plt.show()


import matplotlib.pyplot as plt

image = preprocess_image("test_my_digits_dark/3/3_04.png")

plt.imshow(image.squeeze(), cmap="gray")
plt.axis("off")
plt.show()  