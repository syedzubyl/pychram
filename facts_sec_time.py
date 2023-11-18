def fact(x):
    if x == 1:
        return x
    else:
        return x*fact(x-1)


n = int(input("Enter the for How number need length:"))
print(fact(n))