def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


print('MERGE SORT METHOD')
print('--------------------------------')
print('')
input_string = input('Enter elements of a list separated by space \n')
data = [int(x) for x in input_string.split()]

print('Accepted Data: ', data)
print('')
print("Unsorted Array")
print(data)

size = len(data)
data = merge_sort(data)

print('')
print('Sorted Array using Merge Sort in Ascending Order:')
print(data)
