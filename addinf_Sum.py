def arr_sum(arr, size):
    if size == 0:
        return 0
    else:
        return arr[size - 1] + arr_sum(arr, size - 1)


n = int(input("Enter the number for array size: "))
a = []

for i in range(0, n):
    ele = int(input("Enter the element one by one: "))
    a.append(ele)

print("The given array is:")
print(a)

print("The total sum of the array elements is:", arr_sum(a, n))

