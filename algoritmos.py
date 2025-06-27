# Funções dos algoritmos de Dividir e Conquistar

def merge_count(arr, nivel=0, mostrar_passos=True):
    if len(arr) <= 1:
        return arr, 0
    meio = len(arr) // 2
    if mostrar_passos:
        print("  " * nivel + f"Dividindo: {arr}")
    esq, inv_esq = merge_count(arr[:meio], nivel+1, mostrar_passos)
    dir, inv_dir = merge_count(arr[meio:], nivel+1, mostrar_passos)
    merged, inv_merge = merge(esq, dir, nivel, mostrar_passos)
    total_inv = inv_esq + inv_dir + inv_merge
    if mostrar_passos:
        print("  " * nivel + f"Juntando: {merged} | Inversões até aqui: {total_inv}")
    return merged, total_inv

def merge(esq, dir, nivel, mostrar_passos):
    i = j = inv = 0
    resultado = []
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            inv += len(esq) - i
            if mostrar_passos:
                print("  " * (nivel+1) + f"Inversão: {esq[i:]} > {dir[j]}")
            j += 1
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado, inv

def mediana_das_medianas(arr, mostrar_passos=True, nivel=0):
    if len(arr) <= 5:
        arr_ordenado = sorted(arr)
        idx = (len(arr_ordenado) - 1) // 2  # pega o elemento mais à esquerda no caso par
        mediana = arr_ordenado[idx]
        if mostrar_passos:
            print("  " * nivel + f"Grupo final: {arr_ordenado} -> Mediana: {mediana}")
        return mediana
    grupos = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medianas = []
    for grupo in grupos:
        grupo_ordenado = sorted(grupo)
        idx = (len(grupo_ordenado) - 1) // 2  # pega o elemento mais à esquerda no caso par
        mediana = grupo_ordenado[idx]
        medianas.append(mediana)
        if mostrar_passos:
            print("  " * nivel + f"Grupo: {grupo_ordenado} -> Mediana: {mediana}")
    if mostrar_passos:
        print("  " * nivel + f"Medians dos grupos: {medianas}")
    return mediana_das_medianas(medianas, mostrar_passos, nivel+1)

import math

def distancia(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def par_mais_proximo(pontos, mostrar_passos=True, nivel=0):
    n = len(pontos)
    if n <= 3:
        min_dist = float('inf')
        par = None
        for i in range(n):
            for j in range(i+1, n):
                d = distancia(pontos[i], pontos[j])
                if mostrar_passos:
                    print("  " * nivel + f"Comparando {pontos[i]} e {pontos[j]}: dist = {d:.2f}")
                if d < min_dist:
                    min_dist = d
                    par = (pontos[i], pontos[j])
        return par, min_dist
    pontos = sorted(pontos, key=lambda x: x[0])
    meio = n // 2
    Q = pontos[:meio]
    R = pontos[meio:]
    if mostrar_passos:
        print("  " * nivel + f"Dividindo: {pontos}")
    par_esq, dist_esq = par_mais_proximo(Q, mostrar_passos, nivel+1)
    par_dir, dist_dir = par_mais_proximo(R, mostrar_passos, nivel+1)
    if dist_esq < dist_dir:
        d = dist_esq
        par_min = par_esq
    else:
        d = dist_dir
        par_min = par_dir
    x_meio = Q[-1][0]
    faixa = [p for p in pontos if abs(p[0] - x_meio) < d]
    faixa = sorted(faixa, key=lambda x: x[1])
    for i in range(len(faixa)):
        for j in range(i+1, min(i+7, len(faixa))):
            d_faixa = distancia(faixa[i], faixa[j])
            if mostrar_passos:
                print("  " * (nivel+1) + f"Faixa: comparando {faixa[i]} e {faixa[j]}: dist = {d_faixa:.2f}")
            if d_faixa < d:
                d = d_faixa
                par_min = (faixa[i], faixa[j])
    if mostrar_passos:
        print("  " * nivel + f"Menor par nesta divisão: {par_min} com dist = {d:.2f}")
    return par_min, d
