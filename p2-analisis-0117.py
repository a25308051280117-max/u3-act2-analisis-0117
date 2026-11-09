
import pandas as pd
import numpy as np
print("Analisis de datos vehiculos Matias Lopez NC 0117")

vehiculos = {"Modelo": ["Sedan X", "SUV Compact", "Hatchback Z", "Pickup Heavy", "Electric Eco", "Sedan X"],
"Tipo_Motor": ["Diesel", "Hibrido", "Gasolina", "Diesel", "Gasolina", "Diesel"],
"Autonomia_km": [600, 800, 550, 700, 450, 600],
"Precio_USD": [22000, 35000, 18000, 45000, 32000, 22000]}

df = pd.DataFrame(vehiculos)
print(df)
print("+---+---Agrupar por una sola columna+---+---")
agrupado = df.groupby('Tipo_Motor')
print(agrupado)
print("+---+---por agregacion+---+---")
# Autonomia_km promedio
print(agrupado['Autonomia_km'].mean())
print("+---+---precio maximo+---+---")
# precio maximo de cada carro
print(agrupado['Precio_USD'].max())

print("+---+---segunda parte Matias Lopez 0117+---+---")
print("Agrupaciones multiples")
print("mean-->promedio,sum-->suma")
print("max-->maximo,min-->minimo")

resultado_agregado = agrupado['Precio_USD'].agg(['mean', 'sum', 'max', 'min'])
print(resultado_agregado)

print("agrupacion por varias columnas ")
print("agrega columnas al dataframe")
df['Team'] = ['A', 'B', 'A', 'B', 'A', 'A']

agrupado_multiple = df.groupby(['Tipo_Motor', 'Team'])['Autonomia_km'].mean()
print(agrupado_multiple)
