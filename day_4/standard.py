import pandas as pd
from sklearn.preprocessing import StandardScaler


data = pd.read_csv('./dataset/ecommerce_customers_unit1.csv')
df = pd.DataFrame(data)

num_cols = df.select_dtypes(include=['int64', 'float64']).columns

std = StandardScaler()
df_std = df.copy()
df_std[num_cols] = pd.DataFrame(std.fit_transform(df[num_cols]))
print("Original:\n",df)
print("Standardized:\n",df_std)