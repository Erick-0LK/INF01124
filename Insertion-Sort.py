import random

def print_array(array):

 aux = 0

 print("[", end = "")
 for i in array:
    aux = aux + 1
    if aux == len(array):
       print(i, end = "]")
    else:
        print(i, end = ", ")      

def insertion_sort(array, print_ok):

    changes = 0

    if print_ok > 0:
       print("Array before: ", end = "")
       print_array(array)
       print()

    for i in range(1, len(array)):
        chave = array[i]
        j = i - 1
               
        while j >= 0 and chave < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            changes = changes + 1
        
        array[j + 1] = chave

    if print_ok > 0:
       print("Array after: ", end = "")
       print(array)  

    print("Insertion Sort used " + str(changes) + " changes.")
    print()   

arr1 = [12, 2, 5, 4, 8, 7, 6, 9, 1, 15]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

arr4 = []
arr5 = []

insertion_sort(arr1, 1)
insertion_sort(arr2, 1)
insertion_sort(arr3, 1)

j = 0

for i in range(999, -1, -1):
    arr4.append(i)

insertion_sort(arr4, 0)

for i in range(0, 1000 + 1):
    arr5.append(random.randint(0, 999))

insertion_sort(arr5, 0)    

arr5.clear()

for i in range(0, 1000 + 1):
    arr5.append(random.randint(0, 999))

insertion_sort(arr5, 0)
