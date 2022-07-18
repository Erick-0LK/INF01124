import time
import random

# LABORATÓRIO: 2 ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# FUNÇÕES -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Função que faz o mecanismo mediana de três.
def mediana_de_tres(vetor, inicio, fim, trocas):

    meio = (inicio + fim - 1) // 2
    A = vetor[inicio]
    B = vetor[meio]
    C = vetor[fim]

    if A >= C >= B or A >= B >= C:
        (vetor[inicio], vetor[fim]) = (C, A)
        trocas += 1
    elif B >= A >= C or B >= C >= A:
        (vetor[meio], vetor[fim]) = (C, B)
        trocas += 1

# Função que faz o mecanismo aleatório.
def aleatorio(vetor, inicio, fim, trocas):

    auxiliar = random.randint(inicio, fim)
    (vetor[auxiliar], vetor[fim]) = (vetor[fim], vetor[auxiliar])
    trocas += 1
    
# Função que faz o particionamento tipo Lomuto.
def particionamento_lomuto(vetor, inicio, fim, trocas):

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
def particionamento_hoare(vetor, inicio, fim, trocas):
 
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
        print(trocas)

# Função que faz o algoritmo Quick Sort de acordo com o particionamento e a escolha selecionados.
def quick_sort(vetor, inicio, fim, particionamento, escolha, trocas):
    if particionamento == 1:
            if inicio < fim:
                if escolha == 1:
                    mediana_de_tres(vetor, inicio, fim, trocas)
                    particionador = particionamento_lomuto(vetor, inicio, fim, trocas)
                    quick_sort(vetor, inicio, particionador - 1, 1, 1, trocas)
                    quick_sort(vetor, particionador + 1, fim, 1, 1, trocas)
                else:
                    aleatorio(vetor, inicio, fim, trocas)
                    particionador = particionamento_lomuto(vetor, inicio, fim, trocas)
                    quick_sort(vetor, inicio, particionador - 1, 1, 1, trocas)
                    quick_sort(vetor, particionador + 1, fim, 1, 1, trocas)
    else:
        if inicio < fim:
            if escolha == 1:
                mediana_de_tres(vetor, inicio, fim, trocas)
                particionador = particionamento_hoare(vetor, inicio, fim, trocas)
                quick_sort(vetor, inicio, particionador, 0, 1, trocas)
                quick_sort(vetor, particionador + 1, fim, 0, 1, trocas)
            else:
                aleatorio(vetor, inicio, fim, trocas)
                particionador = particionamento_hoare(vetor, inicio, fim, trocas)
                quick_sort(vetor, inicio, particionador, 0, 1, trocas)
                quick_sort(vetor, particionador + 1, fim, 0, 1, trocas)

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

# LABORATÓRIO: 2 ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTÃO: 1 --------------------------------------------------------------------------------------------------------------------------------------------------------------------

trocas = 0

with open(r'C:\Programas\UFRGS\Bacharelado em Ciência da Computação\Classificação & Pesquisa de Dados\entrada-quicksort.txt') as file:

    for line in file:

        line = line.split()
        line = [int(i) for i in line]
        line.pop(0)
        tamanho = len(line)

        clone = line.copy()
        tempo_inicio = time.time()
        quick_sort(clone, 0, tamanho - 1, 1, 1, trocas)
        tempo_fim = time.time()
        tempo = tempo_fim - tempo_inicio
        escreve_stats_mediana_lomuto("TAMANHO ENRTADA " + str(tamanho) + "\nSWAPS " + str(trocas) + "\nRECURSOES" + "\nTEMPO " + str('{:.6f}'.format(tempo)) + "\n")
        trocas = 0

        clone = line.copy()
        tempo_inicio = time.time()
        quick_sort(clone, 0, tamanho - 1, 1, 0, trocas)
        tempo_fim = time.time()
        tempo = tempo_fim - tempo_inicio
        escreve_stats_aleatorio_lomuto("TAMANHO ENRTADA " + str(tamanho) + "\nSWAPS " + str(trocas) + "\nRECURSOES" + "\nTEMPO " + str('{:.6f}'.format(tempo)) + "\n")
        trocas = 0

        clone = line.copy()
        tempo_inicio = time.time()
        quick_sort(clone, 0, tamanho - 1, 0, 1, trocas)
        tempo_fim = time.time()
        tempo = tempo_fim - tempo_inicio
        escreve_stats_mediana_hoare("TAMANHO ENRTADA " + str(tamanho) + "\nSWAPS " + str(trocas) + "\nRECURSOES" + "\nTEMPO " + str('{:.6f}'.format(tempo)) + "\n")
        trocas = 0

        clone = line.copy()
        tempo_inicio = time.time()
        quick_sort(clone, 0, tamanho - 1, 0, 0, trocas)
        tempo_fim = time.time()
        tempo = tempo_fim - tempo_inicio
        escreve_stats_aleatorio_hoare("TAMANHO ENRTADA " + str(tamanho) + "\nSWAPS " + str(trocas) + "\nRECURSOES" + "\nTEMPO " + str('{:.6f}'.format(tempo)) + "\n")
        trocas = 0