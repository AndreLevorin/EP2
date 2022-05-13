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



# Adicionando em uma Lista Ordenada
def adiciona_em_ordem(nome_pais, distancia, lista_pais_distancia):
    lista_nova_pais_distancia = []
    lista_nova_pais_distancia.append(nome_pais)
    lista_nova_pais_distancia.append(distancia)
    lista_pais_distancia.append(lista_nova_pais_distancia)
    segundo_elemento = lista_nova_pais_distancia[1]
    lista_pais_distancia.sort(key= lambda x : x[1])
    return (lista_pais_distancia)



# Está na Lista?
def esta_na_lista(pais, lista_paises):
  for X in lista_paises:
    if X[0]==pais:
      return True 
  return False



# Sorteia Letra com Restricoes
def sorteia_letra(palavra,lista_restrita):
    pontos=['.',',','-',';',' ']
    palavra=palavra.lower()
    check_for=False
    lista=[]
    saida=''
    for letra in palavra:
        if letra not in lista_restrita and letra not in pontos and letra not in lista:
            lista.append(letra)
            check_for=True
    while check_for:
        saida=random.choice(lista)
        check_for=False
    return saida



