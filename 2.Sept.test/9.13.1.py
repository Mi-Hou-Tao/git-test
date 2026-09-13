import pandas as pd
import torch
import torch.nn as nn
data = pd.read_csv("")
data = data.sample(100000,random_state=42)
feature = [
    "",
    ""
]
X = data[feature].values
y = data[""].values

from sklearn.model_selection import train_test_split
a,b,c,d = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)
from sklearn.preprocessing import StandardScaler

scaler_x = StandardScaler()
a = scaler_x.fit_transform(a)
b = scaler_x.transform(b)
scaler_y = StandardScaler()
c = scaler_y.fit_transform(c,reshape(-1,1))
d = scaler_y.transform(d,reshape(-1,1))

a = torch.tensor(a,dtype=torch.float32)
b = torch.tensor(b,dtype=torch.float32)
c
d
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

for epoch in range(1000):
    e = model(a)
    loss = loss_fn(e,c)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

model.eval()
with torch.no_grad():
    f = model(b)
    loss_fin = loss_fn(f,d)

from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import numpy as np

e_real = scaler_y.inverse_transform(
    e.numpy()
)
d_real  = scaler_y.inverse_transform(
    d.numpy()
)

mae = mean_absolute_error(d_real,e_real)
rmse = np.sqrt(
    mean_squared_error(d_real,e_real)
)
r2 = r2_score(d_real,e_real)

torch.save(model.state_dict(),"")

import joblib
joblib.dump(scaler_x,"")
joblib.dump(scaler_y,"")
