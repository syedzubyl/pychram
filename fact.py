def fact(x):
    if x == 1:
        return x
    else:
        return x * fact(x - 1)


x = int(input("enter the number"))
if x <= 0:
    print("Sorry,Negative doesn't exit")
else:
    print("the factorial series are: ", x, "is", fact(x))
