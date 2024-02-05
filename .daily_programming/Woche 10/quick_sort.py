# Beispiel
unsorted_array = [3, 6, 8, 10, 1, 2, 1] 

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
sorted_array = quick_sort(unsorted_array)
print(sorted_array) 