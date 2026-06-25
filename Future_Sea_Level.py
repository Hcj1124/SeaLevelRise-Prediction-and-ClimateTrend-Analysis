# -*- coding: utf-8 -*-
"""
Created on Wed May  8 22:50:07 2024

@author: rayhs
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\rayhs\OneDrive\Desk\sealevel.csv")

years = data['Year'].values.reshape(-1, 1)
sea_levels = data['GMSL_GIA'].values

model = LinearRegression()

model.fit(years, sea_levels)

future_years = np.array([[2022], [2023], [2024], [2025], [2026], [2027], [2028], [2029], [2030], [2031]])

future_sea_levels = model.predict(future_years)

for year, sea_level in zip(future_years.flatten(), future_sea_levels):
    print(f"Year: {year}, Predicted Sea Level Rise: {sea_level:.2f}")
    
plt.figure(figsize=(10, 6))
plt.scatter(years, sea_levels, color='blue', label='Actual Sea Levels')
plt.plot(np.concatenate([years, future_years]), np.concatenate([sea_levels, future_sea_levels]), color='red', linestyle='--', label='Predicted Sea Levels')

plt.title('Sea Level Rise Prediction')
plt.xlabel('Year')
plt.ylabel('Sea Level Rise')
plt.legend()
plt.grid(True)

plt.show()


