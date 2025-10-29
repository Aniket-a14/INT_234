import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


data = {'Area':[1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000],
        'Bedrooms':[3, 4, 3, 5, 4, 5, 4, 6, 5, 6],
        'Price':[300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000]}

df = pd.DataFrame(data)
print("Summary Statistics:\n", df.describe())
X = df[['Area', 'Bedrooms']]
Y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Predicted Prices:", y_pred)
print("Actual Prices:", y_test.values)
print("Model Score:", model.score(X_test, y_test))

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

new_house = pd.DataFrame({'Area':[3200], 'Bedrooms':[4]})
predicted_price = model.predict(new_house)
print("Predicted price for new house:", predicted_price[0])


x_range = np.linspace(df['Area'].min(), df['Area'].max(), 20)
y_range = np.linspace(df['Bedrooms'].min(), df['Bedrooms'].max(), 20)
x_surf, y_surf = np.meshgrid(x_range, y_range)

z_surf = model.predict(pd.DataFrame({'Area': x_surf.ravel(), 'Bedrooms': y_surf.ravel()}))
z_surf = z_surf.reshape(x_surf.shape)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Area'], df['Bedrooms'], df['Price'], color='red')
ax.plot_surface(x_surf, y_surf, z_surf, color='blue', alpha=0.5)
ax.set_xlabel('Area')
ax.set_ylabel('Bedrooms')
ax.set_zlabel('Price')
plt.show()


