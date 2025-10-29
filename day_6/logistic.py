import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data = {
    'Age': [25, 32, 45, 28, 52, 23, 38, 41, 30, 35],
    'Salary': [45000, 65000, 85000, 38000, 95000, 35000, 75000, 78000, 42000, 58000],
    'Purchase': [1, 1, 1, 0, 1, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(data)
print("Summary stats:/n",df.describe())
X = df[['Age','Salary']]
Y = df['Purchase']

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=0)
model = LogisticRegression()
model.fit(X_train,Y_train)
y_pred = model.predict(X_test)
print("Predicted Purchase:", y_pred)
print("Actual Purchase:", Y_test.values)
print("Model Score:", model.score(X_test, Y_test))

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

new_purchase = pd.DataFrame({'Age':[39],'Salary':[69000]})
prediction = model.predict(new_purchase)
print("Purchase prob.:",prediction[0])

x_range = np.linspace(df['Age'].min(), df['Age'].max(), 20)
y_range = np.linspace(df['Salary'].min(), df['Salary'].max(), 20)
x_surf, y_surf = np.meshgrid(x_range,y_range)

z_surf = model.predict(pd.DataFrame({'Age': x_surf.ravel(), 'Salary': y_surf.ravel()}))
z_surf = z_surf.reshape(x_surf.shape)
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Age'],df['Salary'],df['Purchase'],color='red')
ax.plot_surface(x_surf,y_surf,z_surf, cmap='coolwarm', alpha=0.5)
ax.set_xlabel('Age')
ax.set_ylabel('Salary')
ax.set_zlabel('Purchase')
plt.show()
