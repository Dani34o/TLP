import pandas as pd

file_path = 'NBA_2024_per_game.csv'
data = pd.read_csv(file_path)

# 1. Encontrar el jugador que mas tiempo haya jugado en la temporada.
jugador_mas_tiempo = data.loc[data['MP'].idxmax()]['Player']
print(f"1. Jugador que más tiempo jugó: {jugador_mas_tiempo}")

# 2. Encontrar todos los jugadores que hayan jugado para los Cleveland Cavaliers (CLE) en la posición de Point Guard (PG).
jugadores_cle_pg = data[(data['Tm'] == 'CLE') & (data['Pos'] == 'PG')]['Player'].tolist()
print(f"2. Jugadores de los Cleveland Cavaliers en la posición de Point Guard: {jugadores_cle_pg}")

# 3. Encontrar los jugadores que tengan mas de 1 robo por partido y mas de 1 bloqueo por partido usando list comprehension.
jugadores_robos_bloqueos = [jugador for index, jugador in data.iterrows() if jugador['STL'] > 1 and jugador['BLK'] > 1]
print(f"3. Jugadores con más de 1 robo y 1 bloqueo por partido: {jugadores_robos_bloqueos}")

# 4. Encontrar cual es el porcentaje de canastas de 3 puntos que se hacen en la liga.
porcentaje_tiros_3_puntos = (data['3P'].sum() / data['3PA'].sum()) * 100
print(f"4. Porcentaje de canastas de 3 puntos en la liga: {porcentaje_tiros_3_puntos:.2f}%")

# 5. Encontrar que jugadores estuvieron en 2 equipos o mas en una sola temporada.
jugadores_varios_equipos = data[data.duplicated(subset=['Player', 'Tm'], keep=False)]['Player'].unique()
print(f"5. Jugadores que estuvieron en 2 equipos o más en una sola temporada: {jugadores_varios_equipos}")
