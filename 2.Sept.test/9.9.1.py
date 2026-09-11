import pandas as pd
import torch
import torch.nn as nn

data = pd.read_csv("measures.csv")
data = data.sample(1000,random_state=42)
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

from sklearn.preprocessing import StandardScaler
scaler_x = StandardScaler()
X_train = scaler_x.fit_transform(X_train)
X_val = scaler_x.transform(X_val)

X_test = scaler_x.transform(X_test)
scaler_y = StandardScaler()
y_train = scaler_y.fit_transform(y_train.reshape(-1,1))
y_val = scaler_y.transform(y_val.reshap(-1,1))
y_test = scaler_y.transform(y_test.reshape(-1,1))

X_train = torch.tensor (X_train,dtype=torch.float32)
X_val = torch.tensor(X_val,dtype=torch.float32)
X_test = torch.tensor (X_test,dtype=torch.float32)
y_train = torch.tensor(y_train,dtype=torch.float32)
y_val = torch.tensor(y_val,dtype=torch.float32) 
y_test = torch.tensor(y_test,dtype=torch.float32)

model = nn.Sequential(
    nn.Linear(4,16),
    nn.ReLU(),
    nn.Linear(16,1)
)
