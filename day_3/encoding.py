import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

data = {
    'Age': [18,22,45,60,32],
    'Income': [2000, 5000,10000,6000,5500]
}

df = pd.DataFrame(data)
print("Original Data:\n",df)

scaler = MinMaxScaler()
df[['Age']] = scaler.fit_transform(df[['Age']])
df[['Income']] = scaler.fit_transform(df[['Income']])
print("Normalized Data:\n",df)

std = StandardScaler()
df[['Age']] = std.fit_transform(df[['Age']])
df[['Income']] = std.fit_transform(df[['Income']])
print("Standardized Data:\n",df)

