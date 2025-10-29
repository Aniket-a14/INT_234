import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

data = pd.read_csv('./dataset/ecommerce_customers_unit1.csv')
df = pd.DataFrame(data)

categorical_cols = df.select_dtypes(include=['object', 'category']).columns

le= LabelEncoder()
df['country_encoded'] = le.fit_transform(df['country'])
print("Label encoded:\n",df[['country','country_encoded']].head())

df_encoded = df.copy()
df_encoded = pd.get_dummies(df_encoded, columns=categorical_cols, dtype=int)
print("One-Hot Encoded Data:\n",df_encoded.head())
