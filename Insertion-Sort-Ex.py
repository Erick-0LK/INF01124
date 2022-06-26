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
       print()

    for i in range(1, len(array)):
        chave = array[i]
        j = i - 1
               
        while j >= 0 and chave < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            changes = changes + 1
        
        array[j + 1] = chave
        print(array)  

    if print_ok > 0:
       print() 
       print("Array after: ", end = "")
       print(array)  
       print() 
       
    print("Insertion Sort used " + str(changes) + " changes.")

arr6 = [32, 7, 3, 15, 13, 4, 21, 6, 2, 9, 1, 31, 45, 11, 5, 8]
insertion_sort(arr6, 1)