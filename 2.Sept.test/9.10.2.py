import pandas as pd
import torch
import torch.nn as nn

data = pd.read_csv("measures_v2.csv")
data = data.sample(100000,random_state=42)
print(data.shape)

features = [
    "stator_tooth",
    "stator_yoke",
    "pm",
    "i_d"

]
X = data[features].values
y = data["stator_winding"].values
print("X_shape:",X.shape)
print("y_shape:",y.shape)

#划分数据集，即训练、验证、测试集
from sklearn.model_selection import train_test_split
X_train,X_temp,y_train,y_temp = train_test_split(
    X,
    y,
    test_size = 0.3,
    random_state = 42
)
X_val,X_test,y_val,y_test = train_test_split(
    X_temp,y_temp,
    test_size=0.5,
    random_state=42
)
print("X_train:",X_train.shape)
print("X_val:",X_val.shape)
print("X_test:",X_test.shape)
print("y_test:",y_test.shape)
print("y_val:",y_val.shape)
print("y_train:",y_train.shape)

#标准化与Tensor转换
from sklearn.preprocessing import StandardScaler
scaler_x = StandardScaler()

X_train = scaler_x.fit_transform(X_train)
X_val = scaler_x.transform(X_val)
X_test = scaler_x.transform(X_test)

scaler_y = StandardScaler()

y_train = scaler_y.fit_transform(y_train.reshape(-1,1))
y_val = scaler_y.transform(y_val.reshape(-1,1))
y_test = scaler_y.transform(y_test.reshape(-1,1))

X_train = torch.tensor (X_train,dtype=torch.float32)
X_val = torch.tensor(X_val,dtype=torch.float32)
X_test = torch.tensor (X_test,dtype=torch.float32)

y_train = torch.tensor(y_train,dtype=torch.float32)
y_val = torch.tensor(y_val,dtype=torch.float32)
y_test = torch.tensor(y_test,dtype=torch.float32)

#定义神经网络结构(封装为nn.Linear)

torch.manual_seed(42)#固定神经网络随机初始化

#模型改进
model = nn.Sequential(
    nn.Linear(4,32),
    nn.ReLU(),
    nn.Linear(32,16),
    nn.ReLU(),
    nn.Linear(16,1)
)

#定义损失函数（预测与真实之差）与优化器（接受可训练参数）
loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(
    model.parameters(),#取出可训练参数
    lr = 0.01
)

#循环训练
for epoch in range(1000):
    y_pred = model(X_train)
    loss = loss_fn(y_pred,y_train)
    optimizer.zero_grad()#清空上一次的梯度
    loss.backward()#反向传播，计算梯度
    optimizer.step()#根据梯度重新更新参数
    if epoch % 100 == 0:
        print("epoch:",epoch,"loss:",loss.item())

#进入验证集评估
model.eval()
with torch.no_grad():#不计算梯度，不更新参数
    y_val_pre = model(X_val)
    val_loss = loss_fn(y_val_pre,y_val)
print("validation loss:",val_loss.item())

#进入测试集考试
model.eval()
with torch.no_grad():
    y_test_pred = model(X_test)
    test_loss = loss_fn(y_test_pred,y_test)
print("test loss:",test_loss.item())

#将预测结果还原为真实温度
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import numpy as np

y_test_pred_real = scaler_y.inverse_transform(
    y_test_pred.numpy()
)#预测值已还原

y_test_real = scaler_y.inverse_transform(
    y_test.numpy()
)#真实值已还原

#计算指标
mae = mean_absolute_error(y_test_real,y_test_pred_real)
rmse = np.sqrt(
    mean_squared_error(y_test_real,y_test_pred_real)
)
r2 = r2_score(y_test_real,y_test_pred_real)

print("MAE:",mae)
print("RMSE:",rmse)
print("R^2:",r2)

#保存模型参数(改进版)
torch.save(model.state_dict(),"motor_temperature_improved_model.pth")

#保存标准化器
import joblib
joblib.dump(scaler_x,"scaler_x.pkl")
joblib.dump(scaler_y,"scaler_y.pkl")

print("模型与标准化器已保存")


#---------正式调用模型实现预测温度--------


#模型改进
loaded_model = nn.Sequential(
    nn.Linear(4,32),
    nn.ReLU(),
    nn.Linear(32,16),
    nn.ReLU(),
    nn.Linear(16,1)
)

#加载已训练参数
loaded_model.load_state_dict(
    torch.load("motor_temperature_improved_model.pth")
)

#切换到预测模式
loaded_model.eval()

#设定数据
new_data = [[
    20.0,
    22.0,
    25.0,
    -0.5
]]

#标准化
new_data = scaler_x.transform(new_data)
new_data = torch.tensor(
    new_data,
    dtype=torch.float32
)

#预测
with torch.no_grad():
    prediction = loaded_model(new_data)

#还原温度
prediction_real = scaler_y.inverse_transform(
    prediction.numpy()
)
print("预测发动机温度为:",
      prediction_real[0,0],
      "°C")


#做散点图
import matplotlib.pyplot as plt

plt.scatter(y_test_real,y_test_pred_real)

min_value = min(y_test_real.min(),y_test_pred_real.min())
max_value = max(y_test_real.max(),y_test_pred_real.max())

plt.plot(
    [min_value,max_value],
    [min_value,max_value]
)

plt.xlabel("True Temperature(°C)")
plt.ylabel("Predicted Temperature(°C)")
plt.title("True vs Predicted Temperature")
plt.show()

# 误差分析
errors = y_test_pred_real - y_test_real

print("平均误差:", np.mean(errors))
print("平均绝对误差:", np.mean(np.abs(errors)))
print("最大绝对误差:", np.max(np.abs(errors)))
print("误差标准差:", np.std(errors))


# 误差分布图
errors = y_test_pred_real.flatten() - y_test_real.flatten()

plt.figure(figsize=(8, 5))
plt.hist(errors, bins=50)

plt.xlabel("Prediction Error (°C)")
plt.ylabel("Number of Samples")
plt.title("Distribution of Prediction Errors")

plt.show()


# 找出误差最大的5个样本
abs_errors = np.abs(errors)

largest_indices = np.argsort(abs_errors)[-5:][::-1]

print("\n误差最大的5个样本：")

for i in largest_indices:
    print(
        "真实温度:",
        y_test_real[i, 0],
        "°C",
        "预测温度:",
        y_test_pred_real[i, 0],
        "°C",
        "绝对误差:",
        abs_errors[i],
        "°C"
    )


    # 按温度区间进行误差分析
true_temp = y_test_real.flatten()
abs_errors = np.abs(errors.flatten())

ranges = [
    ("<40°C", true_temp < 40),
    ("40-60°C", (true_temp >= 40) & (true_temp < 60)),
    ("60-80°C", (true_temp >= 60) & (true_temp < 80)),
    (">80°C", true_temp >= 80)
]

print("\n不同温度区间的预测误差:")

for name, mask in ranges:
    if np.sum(mask) > 0:
        mae_range = np.mean(abs_errors[mask])
        print(
            name,
            "样本数:", np.sum(mask),
            "MAE:", mae_range
        )

print("\n测试集真实温度统计:")
print("最低温度:", true_temp.min())
print("最高温度:", true_temp.max())
print("平均温度:", true_temp.mean())

