import time

# LABORATÓRIO: 1 ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# FUNÇÕES --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Função que ordena um vetor de acordo com o método Shell Short.
def shell_sort(array, question):

    starting_time = time.time()
    size = len(array)
    interval = size // 2

    if question == 1:
        write_file1(str(array)[1:-1] + " SEQ=SHELL\n")
    else:
        write_file2("SHELL," + str(len(array)) + ",")

    while interval > 0:
        for i in range(interval, size):
            temp = array[i]
            j = i

            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
                array[j] = temp

        if question == 1:
            write_file1(str(array)[1:-1] + " INCR=" + str(interval) + "\n")

        interval //= 2

    ending_time = time.time()

    if question == 2:
        write_file2(str('{:.6f}'.format(ending_time - starting_time)) + "\n")

# Função que ordena um vetor de acordo com o método Shell Short (Knuth).
def shell_sort_knuth(array, question):

    starting_time = time.time()
    size = len(array)
    k = 1

    if question == 1:
        write_file1(str(array)[1:-1] + " SEQ=KNUTH\n")
    else:
        write_file2("KNUTH," + str(len(array)) + ",")

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

        if question == 1:
            write_file1(str(array)[1:-1] + " INCR=" + str(interval) + "\n")

        interval //= 3

    ending_time = time.time()
   
    if question == 2:
        write_file2(str('{:.6f}'.format(ending_time - starting_time)) + "\n")

# Função que ordena um vetor de acordo com o método Shell Short (Ciura).
def shell_sort_ciura(array, question):

    starting_time = time.time()
    size = len(array)
    ciura_sequence = [1, 4, 10, 23, 57, 132, 301, 701]

    if question == 1:
        write_file1(str(array)[1:-1] + " SEQ=CIURA\n")
    else:
        write_file2("CIURA," + str(len(array)) + ",")

    while ciura_sequence[-1] < size:
        ciura_sequence.append(int(ciura_sequence[-1]*2.25))

    while (ciura_sequence[-1]) > size:
        ciura_sequence.pop(-1)

    for h in reversed(ciura_sequence):
        for i in range(h, size):
            t = array[i]
            j = i
            while j >= h and array[j - h] > t:
                array[j] = array[j - h]
                j -= h

            array[j] = t

        if question == 1:
            write_file1(str(array)[1:-1] + " INCR=" + str(h) + "\n")
        
    ending_time = time.time()
   
    if question == 2:
        write_file2(str('{:.6f}'.format(ending_time - starting_time)) + "\n")

# Função que escreve o primeiro arquivo.
def write_file1(string):

    exit = open("saida1.txt", "a")
    exit.write(string)
    exit.close()

# Função que escreve o segundo arquivo.
def write_file2(string):

    exit = open("saida2.txt", "a")
    exit.write(string)
    exit.close()              

# LABORATÓRIO: 1 ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTÃO: 1 ------------------------------------------------------------------------------------------------------------------------------------------------------------------

with open('entrada1.txt') as file1:

    saida = open("saida1.txt", "w")
    saida.close()

    for line in file1:
        line = line.split()
        line = [int(i) for i in line]
        line.pop(0)
        clone = line.copy()
        shell_sort(clone, 1)
        clone = line.copy()
        shell_sort_knuth(clone, 1)
        clone = line.copy()
        shell_sort_ciura(clone, 1)
        
# LABORATÓRIO: 1 ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# QUESTÃO: 2 ------------------------------------------------------------------------------------------------------------------------------------------------------------------

with open('entrada2.txt') as file2:

    saida = open("saida2.txt", "w")
    saida.close()
    
    for line in file2:
        line = line.split()
        line = [int(i) for i in line]
        line.pop(0)
        clone = line.copy()
        shell_sort(clone, 2)
        clone = line.copy()
        shell_sort_knuth(clone, 2)
        clone = line.copy()
        shell_sort_ciura(clone, 2)