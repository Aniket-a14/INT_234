import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./dataset/ecommerce_customers_unit1.csv')
print("Head of the data:\n",data.head(),"\n")
print("Info of the data:\n",data.info(),"\n")
print("Describe of the data:\n",data.describe(),"\n")
print("Null values in the data:\n",data.isnull().sum(),"\n")
print("Total null values in the data:\n",data.isnull().sum().sum(),"\n")
print("Shape of the data:\n",data.shape,"\n")

#bar chart for missing values
plt.figure(figsize=(10, 5))
missing_values = data.isnull().sum().sort_values(ascending=False)
missing_values.plot(kind='bar')
plt.xlabel('Columns')
plt.ylabel('Missing Values')
plt.tight_layout()
plt.show()

df = pd.DataFrame(data)
df['age'] = df['age'].fillna(value=df['age'].mean())
print(df["age"])
df['total_spent'] = df["total_spent"].fillna(value=df['total_spent'].mean())
print(df["total_spent"])

q1 = df['total_spent'].quantile(0.25)
q3 = df['total_spent'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
outliers = df[(df['total_spent'] < lower_bound) | (df['total_spent'] > upper_bound)]
print("Outliers in total_spent:\n",outliers)

#boxplot for total_spent
plt.figure(figsize=(10, 5))
plt.boxplot(df['total_spent'], vert=False)
plt.title('Boxplot of Total Spent')
plt.xlabel('Total Spent')
plt.grid(True)
plt.show()