#Importaciones
import numpy as np
import pandas as pd 
import string

#Declaración de constantes
l_sol = 3.828e26  # Luminosidad del Sol [Watts]
m_sol = 1.9884e30  # Masa del Sol [KG]
g = 6.67430e-11  # Constante de gravitación universal [m^3/kg/s^2]

#Lectura de datos
data = pd.read_csv("exoplanets.csv")

#Limpieza de datos:
data_limpio = data.fillna(0) #Eliminación de datos Nan y rellenar con 0 para evitar errores
data_limpio['star_name'] = data_limpio['star_name'].replace(0, '0') #Reemplazo de 0 por '0' para evitar errores, ya que los nombres son str
data_limpio['star_alternate_names'] = data_limpio['star_alternate_names'].replace(0, '0') #Lo mismo para alternate_names

#Creamos las instancias de cada estrella.

estrella_HR8799 = crear_estrella(data_limpio, "HR 8799")
estrella_HD202206 = crear_estrella(data_limpio, "HD 202206 ")
estrella_TRAPPIST1 = crear_estrella(data_limpio, "TRAPPIST-1")
estrella_TOI1338 = crear_estrella(data_limpio, "TOI-1338")
estrella_HD188753 = crear_estrella(data_limpio, "HD 188753")
estrella_Kepler451 = crear_estrella(data_limpio, "Kepler-451")
estrella_Kepler16 = crear_estrella(data_limpio, "Kepler-16 ")

#Creación de sistemas planetarios a partir de la base de datos utilizando función *crear_sistema* en base a la estrellla principal
sistema_HR8799 = crear_sistema(data_limpio, estrella_HR8799)
sistema_HD202206 = crear_sistema(data_limpio, estrella_HD202206)
sistema_TRAPPIST1 = crear_sistema(data_limpio, estrella_TRAPPIST1)
sistema_TOI1338 = crear_sistema(data_limpio, estrella_TOI1338)
sistema_Kepler451 = crear_sistema(data_limpio, estrella_Kepler451)
sistema_Kepler16 = crear_sistema(data_limpio, estrella_Kepler16)

#Creación de sistema jerárquico
#Utilizando 2 sistemas planetarios, los uniremos para crear a mano un sistema jerárquico.
#Creamos la instancia de la clase SistemaJerarquico
sistema_jerarquico = SistemaJerarquico()
#Añadimos al sistema las 2 estrellas que conforman el sistema jerárquico.
sistema_jerarquico.agregar_estrella(estrella_Kepler16)
sistema_jerarquico.agregar_estrella(estrella_Kepler451)
sistema_jerarquico.agregar_estrella(estrella_Kepler16)