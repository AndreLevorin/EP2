#EP2 por André Levorin e Luigi Zema

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
  
  
