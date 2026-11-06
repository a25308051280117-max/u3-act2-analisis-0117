import pandas as pd
import numpy as np
print("Analisis de datos vehiculos Matias Lopez NC 0117")

vehiculos = {  "Modelo": ["Sedan X", "SUV Compact", "Hatchback Z", "Pickup Heavy", "Electric Eco", "Coupe Sport"],
"Tipo_Motor": ["Diesel", "Hibrido", "Gasolina", "Diesel", "Gasolina", "Gasolina"],
"Autonomia_Km": [600, 800, 550, 700, 450, 500],
"Precio_USD": [22000, 35000, 18000, 45000, 32000, 41000]}

df = pd.DataFrame(vehiculos)
print(df)
print("-+-+-+-+Agrupar por una sola columna-+-+-+-+-")
agrupado = df.groupby('Tipo_Motor')
print(agrupado)
print("-+-+-+-por agregacion-+-+-+-+-")
# Autonomia_km promedio
print(agrupado['Autonomia_Km'].mean())
print("-+-+-+-precio maximo-+-+-+-+-")
# precio maximo de cada carro
print(agrupado['Precio_USD'].max())
