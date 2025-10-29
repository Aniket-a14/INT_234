import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data = {'Marks':[55, 89, 76, 65, 48, 90, 82, 72, 60, 78, 67, 85, 73, 80, 68],
        'Hours_Studied':[4, 8, 6, 5, 3, 9, 7, 6, 4, 7, 5, 8, 6, 7, 5]}

df = pd.DataFrame(data)
X = df[['Hours_Studied']]
Y = df['Marks']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=10)
model = LinearRegression()

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Predicted Marks:", y_pred)
print("Actual Marks:", y_test.values)
print("Model Score:", model.score(X_test, y_test))

plt.scatter(X, Y, color='green')
plt.plot(X, model.predict(X), color='orange')
plt.show()