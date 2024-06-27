def merge_sort(arr):
    if len (arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    
    merge_sort(left)
    merge_sort(right)
    print(left)
    print(right)
    merg_two_sorted_lists(left,right,arr)





def merg_two_sorted_lists(a,b,arr):
    
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] =a[i]
            i += 1
        else:
            arr[k] =b[j]
            j+= 1
        k+=1
        
    while i < len_a:
      arr[k] =a[i]
      i+=1
      k+=1
    while j < len_b:
      arr[k] =b[j]
      j+=1
      k+=1
   


if __name__ == '__main__':

    a = [5, 6, 50 , 10, 9,17 ,3]
   


    print(merge_sort(a))
    print (a)