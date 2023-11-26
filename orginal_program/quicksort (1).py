def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)

def partition(arr, low, high):
    p = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j

print("QUICK SORT METHOD")
print('-----------------')
print("")
input_string = input("enter the elements of a list separated by space\n")
data = [int(x) for x in input_string.split()]
print("accepted data:", data)
print("")
print("UNSORTED ARRAY")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print('')
print("sorted array using quicksort in ascending order")
print(data)
