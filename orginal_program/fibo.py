def fibo(x):
    if x <= 1:
        return x
    else:
        return fibo(x-1) + fibo(x-2)


i = int(input("enter the number:"))
if i <= 0:
    print("enter poistive value ")
else:
    print("fibonnical series:")


for x in range(i):
    print(fibo(x))

