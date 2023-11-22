import pandas as pd

# Cargar el conjunto de datos desde el archivo CSV
data = pd.read_csv('properties.csv')

# Modificar la columna de precio de rupias a dólares
data['Price'] = data['Price'] / 83  # Suponiendo que 1 dólar equivale a 83 rupias

# Encuentrar los apartamentos disponibles y calcular la media de precios
apartamentos_disponibles = data[data['Possession Status'].isin(['Ready to move', 'Immediately'])]
media_precios_disponibles = apartamentos_disponibles['Price'].mean()

# Encontrar el número de inmuebles en el primer piso
num_inmuebles_primer_piso = data[data['Floor No'] == 1].shape[0]

# Encontrar el constructor que ha realizado más edificios
constructor_mas_edificios = data['Developer'].value_counts().idxmax()

# Encontrar la cantidad de casas disponibles en general
casas_disponibles = data['Units Available'].sum()

# Mostrar todos los locales comerciales
locales_comerciales = data[data['Commercial'] == 1]

# Encontrar el inmueble más costoso y el más barato
inmueble_mas_costoso = data.loc[data['Price'].idxmax()]
inmueble_mas_barato = data.loc[data['Price'].idxmin()]

# Encontrar los inmuebles siendo construidos por "Kalpataru Ltd"
inmuebles_kalpataru = data[data['Developer'] == 'Kalpataru Ltd']

# Imprimir los resultados
print(f"Media de precios de apartamentos disponibles: {media_precios_disponibles} dólares")
print(f"Número de inmuebles en el primer piso: {num_inmuebles_primer_piso}")
print(f"Constructor con más edificios realizados: {constructor_mas_edificios}")
print(f"Cantidad de casas disponibles en general: {casas_disponibles}")
print("\nLocales comerciales:")
print(locales_comerciales)
print("\nInmueble más costoso:")
print(inmueble_mas_costoso)
print("\nInmueble más barato:")
print(inmueble_mas_barato)
print("\nInmuebles construidos por Kalpataru Ltd:")
print(inmuebles_kalpataru)
