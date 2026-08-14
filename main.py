from sklearn.linear_model import LinearRegression

X = [
    [1],
    [2],
    [3],
    [4]
]

y = [
    5,
    10,
    15,
    20
]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[6]])

print(prediction)