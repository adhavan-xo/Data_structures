def partition(arr,l,h):
    pivot = arr[h]
    i = l-1
    for j in range(l,h):
        if arr[j] <= pivot:
            i = i+1
            (arr[i],arr[j]) = (arr[j],arr[i])
    return i+1
def quick_sort(arr,l,h):
    if l<h:
        pi = partition(arr,l,h)
        quick_sort(arr, l, pi-1)
        quick_sort(arr, pi+1, h)

data = [50,-20,5,25,45,19]
size = len(data)
quick_sort(data,0,size-1)
print(data)