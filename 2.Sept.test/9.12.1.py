import pandas as pd
import torch
import torch.nn as nn


data = pd.read_csv("measures_v2.csv")
#读入数据
data = pd.read_csv(".csv")
#随机取样本
data = data.sample(1000000,random_state = 42)
data = data.sample(n,random_state = 42)
from sklearn.model_selection import train_test_split


from sklearn.model_selection import train_test_split
a,b,c,d = train_test_split(
    x,
    y,
    test_size= x,
    random_state= 42
)

#标准化
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import StandardScaler
scaler_x = StandardScaler()
a = scaler_x.fit_transform(a)
b = scaler_x.transform(b)

scaler_y = StandardScaler()
c = scaler_y.fit_transform(c.reshape(-1,1))
d = scaler_y.transform(d,reshape(-1,1))

#转换
a = torch.tensor(a,dtype=torch.float32)
#...
c = torch.tensor(c,dtype = torch.float32)
torch.manual_seed(42)

model = nn.Sequential(
    nn.Linear(4,32),
    nn.ReLU(),
    nn.Linear(32,16),
    nn.ReLU(),
    nn.Linear(16,1)
)

loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(
    model.parameters(),
    lr = 0.01
)
