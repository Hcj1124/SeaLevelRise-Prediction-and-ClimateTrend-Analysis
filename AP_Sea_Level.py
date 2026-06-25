# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:16:30 2024

@author: rayhs
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

df = pd.read_csv(r"C:\Users\rayhs\OneDrive\Desk\sealevel.csv")
df.dropna(inplace=True)
x = df.drop(columns=['GMSL_GIA']) 
y = df['GMSL_GIA']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = RandomForestRegressor()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.2)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')  # 绘制对角线参考线
plt.title('Actual vs Predicted Sea Level (Random Forest)')
plt.xlabel('Actual Sea Level (GMSL_GIA)')
plt.ylabel('Predicted Sea Level (GMSL_GIA)')
plt.show()
