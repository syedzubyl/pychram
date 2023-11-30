def arr_lin(arr, s):
    if s == 1:
        return 0
    else:
        return arr[s-1]+arr_lin(arr, s-1)


n = int(input("enter the size of lists you needed"))
a = []
for x in range(0,n):
    ele = int(input("enter element once:"))
    a.append(ele)

print(" ")
print(" ")
print("Linear Recursion")
print("------------------")
print(" ")
print("Your given number is ")
print(a)
print("The summing of array is ",arr_lin(a,n))
