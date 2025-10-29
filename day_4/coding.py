import pandas as pd
from pandas.core.arrays import categorical
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

data = pd.read_csv('./dataset/ecommerce_customers_unit1.csv')
df = pd.DataFrame(data)
print("Original Data:\n",df)

categorical_cols = df.select_dtypes(include=['object', 'category']).columns
print(categorical_cols.to_list())

le= LabelEncoder()
df['country_encoded'] = le.fit_transform(df['country'])
print("Label encoded:\n",df[['country','country_encoded']].head())


