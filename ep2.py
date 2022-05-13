#EP2 por André Levorin e Luigi Zema

#imports
import random
import math





# Normalizando Base de Países
def normaliza(dados_paises):
    base_paises={}
    for continente in dados_paises:
        pais_continente=dados_paises[continente]
        for pais in pais_continente:
            v=pais_continente[pais]
            v['Continente']=continente
            base_paises[pais]=v
    return base_paises



# Sorteando Países
def sorteia_pais(dicionario_paises):
    lista_chaves_paises = list(dicionario_paises.keys())
    random_chave_paises = random.choice(lista_chaves_paises)
    return (random_chave_paises)    



# Distância de Haversine
def haversine(raio, latitude_A, longitude_A, latitude_B, longitude_B):
    lat_a_rad = math.radians(latitude_A)
    lat_b_rad = math.radians(latitude_B)
    lon_a_rad = math.radians(longitude_A)
    lon_b_rad = math.radians(longitude_B)
    dif_lat = (lat_b_rad - lat_a_rad ) / 2
    dif_lon = (lon_b_rad - lon_a_rad ) / 2
    a = math.sin(dif_lat)**2
    b = math.sin(dif_lon)**2
    c = math.cos(lat_a_rad) * math.cos(lat_b_rad)
    angulo = math.sqrt(a + c * b)
    haversine_formula = 2 * raio * math.asin(angulo)
    return haversine_formula    



