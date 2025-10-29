import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {'Colour': ['Red', 'Blue', 'Green', 'Blue', 'Red', 'Green'],
}

df = pd.DataFrame(data)
print("Original Data:\n",df)
enc = LabelEncoder()
df['Colour_Encoded'] = enc.fit_transform(df['Colour'])
print("Encoded Data:\n",df)

df_encoded = df.copy()
df_encoded = pd.get_dummies(df_encoded, columns=['Colour'], dtype=int)
print("One-Hot Encoded Data:\n",df_encoded)

