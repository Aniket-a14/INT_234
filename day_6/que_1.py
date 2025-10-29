import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data = {
    'Marks': [25, 32, 45, 28, 52, 23, 38, 41, 30, 35],
    'Hours_studied': [1,4,3,6,2,4,6,3,6,7],
    'Status': [1, 1, 1, 0, 1, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(data)
print("Summary stats:/n",df.describe())
X = df[['Marks','Hours_studied']]
Y = df['Status']

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=0)
model = LogisticRegression()
model.fit(X_train,Y_train)
y_pred = model.predict(X_test)
print("Predicted Status:", y_pred)
print("Actual Status:", Y_test.values)
print("Model Score:", model.score(X_test, Y_test))

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

new_Status = pd.DataFrame({'Marks':[39],'Hours_studied':[5]})
prediction = model.predict(new_Status)
print("Status prob.:",prediction[0])

x_range = np.linspace(df['Marks'].min(), df['Marks'].max(), 20)
y_range = np.linspace(df['Hours_studied'].min(), df['Hours_studied'].max(), 20)
x_surf, y_surf = np.meshgrid(x_range,y_range)

z_surf = model.predict(pd.DataFrame({'Marks': x_surf.ravel(), 'Hours_studied': y_surf.ravel()}))
z_surf = z_surf.reshape(x_surf.shape)
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Marks'],df['Hours_studied'],df['Status'],color='red')
ax.plot_surface(x_surf,y_surf,z_surf, cmap='coolwarm', alpha=0.5)
ax.set_xlabel('Marks')
ax.set_ylabel('Hours_studied')
ax.set_zlabel('Status')
plt.show()
