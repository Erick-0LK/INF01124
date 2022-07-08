# INF01124 (Clasificação & Pesquisa de Dados) -----------------------------------------------------------------------------------------------------------------------------------
# ALGORITMOS --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Função que ordena um vetor de acordo com o método Insertion Sort.
def insertion_sort(array):

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
               
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            changes = changes + 1
        
        array[j + 1] = key

# Função que ordena um vetor de acordo com o método Shell Sort.
def shell_sort(array):

    size = len(array)
    interval = size // 2

    while interval > 0:
        for i in range(interval, size):
            temp = array[i]
            j = i

            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
                array[j] = temp
        
        interval //= 2

# Função que ordena um vetor de acordo com o método Shell Sort (Knuth).
def shell_sort_knuth(array):

    size = len(array)
    k = 1

    while size > int((pow(3, k) - 1) / 2):
        k += 1
        interval = int((pow(3, k) - 1) / 2)

    while interval > 0:
        for i in range(interval, size):
            temp = array[i]
            j = i

            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
                array[j] = temp
        
        interval //= 3

# Função que ordena um vetor de acordo com o método Shell Sort (Ciura).
def shell_sort_ciura(array):

    size = len(array)
    ciura_sequence = [1, 4, 10, 23, 57, 132, 301, 701]

    while ciura_sequence[-1] < size:
        ciura_sequence.append(int(ciura_sequence[-1]*2.25))

    while (ciura_sequence[-1]) > size:
        ciura_sequence.pop(-1)

    for h in reversed(ciura_sequence):
        for i in range(h, size):
            temp = array[i]
            j = i

            while j >= h and array[j - h] > temp:
                array[j] = array[j - h]
                j -= h

            array[j] = temp     

# Função que ordena um vetor de acordo com o método Selection Sort.
def selection_sort(array):
   
    # Extrai o tamanho do vetor.
    size = len(array)
 
    # Percorre todo o vetor, exceto o último elemento.
    for i in range(size):

        # Atribui o índice i ao valor mínimo.
        minimum = i

        # Percorre todo o vetor após o elemento de índice i, exceto o último elemento.
        for j in range(i + 1, size):

            # Se o elemento de índice j é menor do que o elemento de índice mínimo, o elemento de índice i sendo comparado, então o índice j é o novo mínimo.
            if array[j] < array[minimum]:

                # Atribui o índice j ao valor mínimo.
                minimum = j

        # Coloca o elemento de índice mínimo na posição correta. 
        (array[i], array[minimum]) = (array[minimum], array[i])