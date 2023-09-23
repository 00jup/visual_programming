import tensorflow as tf
import pandas as pd
import numpy as np

data = pd.read_csv('gpascore.csv')
# 전처리해야 함
print(data.isnull().sum())
data = data.dropna()
# data = data.fillna(100)

# print(data['gpa'].min())
# print(data['gpa'].count())
# print(data.isnull().sum())

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

y = data['admit']
xdata = []
# 맘대로 하기 대부분 근데 2의 제곱수로 표현함. 마지막은 하나의 노드만 가지고 있으면 된다.

model.compile(optimizer='adam', loss='binary_crossentropy',
              metrics=['accuracy'])

for i, rows in data.iterrows():
    xdata.append([rows['gre'], rows['gpa'], rows['rank']])


# model.fit(x=data[['gre', 'gpa', 'rank']], y=data['admit'], epochs=10)

model.fit(np.array(xdata), np.array(y), epochs=1000)

# 예측
predict = model.predict([[750, 3.70, 3], [400, 2.2, 1]])
print(predict)
