import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


import matplotlib.pyplot as plt

from preprocess import preprocess_image


paths = [
    "test_my_digits/3/3_01.png",
    "test_my_digits_dark/3/3_04.png",
]

titles = [
    "Normal 3",
    "Dark 3",
]


plt.figure(figsize=(6, 3))

for i, path in enumerate(paths):

    image = preprocess_image(path)

    print(titles[i])
    print("最小值：", image.min().item())
    print("最大值：", image.max().item())
    print("平均值：", image.mean().item())
  
    plt.subplot(1, 2, i + 1)

    plt.imshow(
        image.squeeze(),
        cmap="gray"
    )

    plt.title(titles[i])
    plt.axis("off")

plt.show()