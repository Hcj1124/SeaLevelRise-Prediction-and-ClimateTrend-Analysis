# -*- coding: utf-8 -*-
"""
Created on Wed May  8 22:50:07 2024

@author: rayhs
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\rayhs\OneDrive\Desk\merged_data.csv")

years = data['Year'].values.reshape(-1, 1)
CO2_mean = data['Mean'].values

model = LinearRegression()

model.fit(years, CO2_mean)

future_years = np.array([[2022], [2023], [2024], [2025], [2026], [2027], [2028], [2029], [2030], [2031]])

future_CO2 = model.predict(future_years)

for year, CO2_P in zip(future_years.flatten(), future_CO2):
    print(f"Year: {year}, Predicted CO2 Mean: {CO2_P:.2f}")
    
plt.figure(figsize=(10, 6))
plt.scatter(years, CO2_mean, color='blue', label='Actual CO2 Mean')
plt.plot(np.concatenate([years, future_years]), np.concatenate([CO2_mean, future_CO2]), color='red', linestyle='--', label='Predicted CO2 Mean')

plt.title('CO2 Mean Prediction')
plt.xlabel('Year')
plt.ylabel('CO2 Mean')
plt.legend()
plt.grid(True)

plt.show()


