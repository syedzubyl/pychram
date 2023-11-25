def bin_arr(arr, start, stop):
    if start >= stop:
        return 0
    elif start == stop-1:
        return arr[start]
    else:
        mid = (start + stop) // 2
        return bin_arr(arr, start, mid) + bin_arr(arr, mid, stop)


n = int(input("enter the number for size for list:"))
a = []
for i in range(0 , n):
    ele = int(input("enter the element for list each by each:"))
    a.append(ele)
print("the binary recursion are:")
print(a)
print("the sum of list is :", bin_arr(a, 0, n))
