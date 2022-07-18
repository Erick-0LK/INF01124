## UNIVERSIDADE FEDERAL DO RIO GRANDE DO SUL
## INSTITUTO DE INFORMÁTICA
#
## INF01124 - CLASSIFICAÇÃO E PESQUISA DE DADOS 
## LABORATÓRIO 2
#
## Erick Larratéa Knoblich 00324422
## Leonardo Azzi Martins, 00323721
## 2022/1

import time
import random

trocas = 0
recursoes = -1

LOMUTO = 0
HOARE = 1

ALEATORIO = 0
MEDIANA_TRES = 1

# LABORATÓRIO: 2 ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# FUNÇÕES -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Função que faz o mecanismo mediana de três.
def mediana_de_tres(vetor, inicio, fim):

    global trocas
    global recursoes
    meio = (inicio + fim - 1) // 2
    A = vetor[inicio]
    B = vetor[meio]
    C = vetor[fim]

    if B >= A >= C or C >= A >= B:
        (vetor[inicio], vetor[fim]) = (C, A)
        trocas += 1
    elif A >= B >= C or C >= B >= A:
        (vetor[meio], vetor[fim]) = (C, B)
        trocas += 1

# Função que faz o mecanismo aleatório.
def aleatorio(vetor, inicio, fim):

    global trocas
    global recursoes
    auxiliar = random.randint(inicio, fim)
    (vetor[auxiliar], vetor[fim]) = (vetor[fim], vetor[auxiliar])
    trocas += 1

# Função que faz o particionamento tipo Lomuto.
def particionamento_lomuto(vetor, inicio, fim):

    global trocas
    global recursoes
    particionador = vetor[fim]
    i = inicio - 1

    for j in range(inicio, fim):

        if vetor[j] <= particionador:
            i = i + 1
            (vetor[i], vetor[j]) = (vetor[j], vetor[i])
            trocas += 1

    (vetor[i + 1], vetor[fim]) = (vetor[fim], vetor[i + 1])
    trocas += 1

    return i + 1

# Função que faz o particionamento tipo Hoare.
def particionamento_hoare(vetor, inicio, fim):

    global trocas
    global recursoes
    particionador = vetor[inicio]
    i = inicio - 1
    j = fim + 1
 
    while (True):

        i += 1
        while (vetor[i] < particionador):
            i += 1
 
        j -= 1
        while (vetor[j] > particionador):
            j -= 1
 
        if (i >= j):
            return j
 
        (vetor[i], vetor[j]) = (vetor[j], vetor[i])
        trocas += 1

# Função que faz o algoritmo Quick Sort de acordo com o particionamento e a escolha selecionados.
def quick_sort(vetor, inicio, fim, particionamento, escolha):

    global recursoes
    recursoes += 1

    # LOMUTO
    if particionamento == LOMUTO:
        if inicio < fim:

            ## MEDIANA DE TRÊS
            if escolha == MEDIANA_TRES:
                mediana_de_tres(vetor, inicio, fim)
                particionador = particionamento_lomuto(vetor, inicio, fim)
                quick_sort(vetor, inicio, particionador - 1, LOMUTO, MEDIANA_TRES)
                quick_sort(vetor, particionador + 1, fim, LOMUTO, MEDIANA_TRES)

            ## ALEATÓRIO
            else:
                aleatorio(vetor, inicio, fim)
                particionador = particionamento_lomuto(vetor, inicio, fim)
                quick_sort(vetor, inicio, particionador - 1, LOMUTO, ALEATORIO)
                quick_sort(vetor, particionador + 1, fim, LOMUTO, ALEATORIO)

    # HOARE
    else:
        if inicio < fim:
            ## MEDIANA DE TRÊS
            if escolha == MEDIANA_TRES:
                mediana_de_tres(vetor, inicio, fim)
                particionador = particionamento_hoare(vetor, inicio, fim)
                quick_sort(vetor, inicio, particionador, HOARE, MEDIANA_TRES)
                quick_sort(vetor, particionador + 1, fim, HOARE, MEDIANA_TRES)

            ## ALEATÓRIO
            else:
                aleatorio(vetor, inicio, fim)
                particionador = particionamento_hoare(vetor, inicio, fim)
                quick_sort(vetor, inicio, particionador, HOARE, MEDIANA_TRES)
                quick_sort(vetor, particionador + 1, fim, HOARE, MEDIANA_TRES)

def escreve_stats_mediana_lomuto(string):

    exit = open("stats-mediana-lomuto.txt", "a")
    exit.write(string)
    exit.close()

def escreve_stats_aleatorio_lomuto(string):

    exit = open("stats-aleatorio-lomuto.txt", "a")
    exit.write(string)
    exit.close()

def escreve_stats_mediana_hoare(string):

    exit = open("stats-mediana-hoare.txt", "a")
    exit.write(string)
    exit.close()

def escreve_stats_aleatorio_hoare(string):

    exit = open("stats-aleatorio-hoare.txt", "a")
    exit.write(string)
    exit.close()

def main():

    # LABORATÓRIO: 2 ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    # QUESTÃO: 1 --------------------------------------------------------------------------------------------------------------------------------------------------------------------

    ## WINDOWS
    # with open(r"C:\Programas\UFRGS\Bacharelado em Ciência da Computação\INF01124 - Classificação & Pesquisa de Dados\Laboratório 2\entrada-quicksort.txt") as file:

    # LINUX
    with open('entrada-quicksort.txt') as file:

        for line in file:

            line = line.split()
            line = [int(i) for i in line]
            line.pop(0)
            tamanho = len(line)
            vec = line.copy()

            ini = 0
            fim = tamanho - 1

            trocas = 0
            recursoes = -1
            
            ## ==============================
            ## LOMUTO - Mediana
            ## ==============================
            tempo_inicio = time.time()

            quick_sort(vec, ini, fim, LOMUTO, MEDIANA_TRES)

            tempo_fim = time.time()
            tempo = tempo_fim - tempo_inicio
            escreve_stats_mediana_lomuto("TAMANHO ENTRADA " + str(tamanho) + "\nSWAPS " + str(trocas) + "\nRECURSOES " + str(recursoes) + "\nTEMPO " + str('{:.6f}'.format(tempo)) + "\n")
            
            trocas = 0
            recursoes = -1

            ## ==============================
            ## LOMUTO - Aleatório
            ## ==============================

            vec = line.copy()
            tempo_inicio = time.time()

            quick_sort(vec, ini, fim, LOMUTO, ALEATORIO)

            tempo_fim = time.time()
            tempo = tempo_fim - tempo_inicio

            escreve_stats_aleatorio_lomuto("TAMANHO ENTRADA " + str(tamanho) + "\nSWAPS " + str(trocas) + "\nRECURSOES " + str(recursoes) + "\nTEMPO " + str('{:.6f}'.format(tempo)) + "\n")
            
            trocas = 0
            recursoes = -1

            ## ==============================
            ## HOARE - Mediana
            ## ==============================

            vec = line.copy()
            tempo_inicio = time.time()

            quick_sort(vec, ini, fim, HOARE, MEDIANA_TRES)

            tempo_fim = time.time()
            tempo = tempo_fim - tempo_inicio

            escreve_stats_mediana_hoare("TAMANHO ENTRADA " + str(tamanho) + "\nSWAPS " + str(trocas) + "\nRECURSOES " + str(recursoes) + "\nTEMPO " + str('{:.6f}'.format(tempo)) + "\n")
            
            trocas = 0
            recursoes = -1

            ## ==============================
            ## HOARE - Aleatório
            ## ==============================

            vec = line.copy()
            tempo_inicio = time.time()

            quick_sort(vec, ini, fim, HOARE, ALEATORIO)
            
            tempo_fim = time.time()
            tempo = tempo_fim - tempo_inicio

            escreve_stats_aleatorio_hoare("TAMANHO ENTRADA " + str(tamanho) + "\nSWAPS " + str(trocas) + "\nRECURSOES " + str(recursoes) + "\nTEMPO " + str('{:.6f}'.format(tempo)) + "\n")
            
            trocas = 0
            recursoes = -1

if __name__ == "__main__":
    main()