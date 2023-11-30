def quickSort(arr, low, high):
    if low < high:
        pivot = partion(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)


def partion(arr, low, high):
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


print("QUICK SORT METHODS:")
print("-------------------")
print(" ")
input_string = input("ENTER the elements of a list separted by spaces: \n")
data = [int(x) for x in input_string.split()]

print("assepted data:", data)
print(" ")
print("Unsorted Array:")
print(data)
size = len(data)

quickSort(data, 0, size - 1)
print(" ")
print("Sorted Array using Quick sort in assecending order:")
print(data)
