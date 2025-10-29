import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    'Experience' : [1,2,3,4,5,6,7,8,9,10],
    'Salary': [25000,27000,29000,31000,33000,35000,37000,39000,41000,43000]
}

df = pd.DataFrame(data)

x = df[['Experience']]
y = df['Salary']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print(y_pred)
print(y_test)
print(model.score(x_test, y_test))

