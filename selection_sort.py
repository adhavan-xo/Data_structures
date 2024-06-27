def selectionSort(array,size):
    for step in range(size):
        min = step
        for i in range(step + 1,size):
            if array[i] < array[min]:
                min = i
        (array[step],array[min]) = (array[min],array[step])

data = [50,-20,5,25,45,19]
size = len(data)
selectionSort(data,size)
print(data)