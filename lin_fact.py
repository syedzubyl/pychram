def fact_lin(x):
    if x ==1:
        return x
    else:
        return x*fact_lin(x-1)


n=int(input("enter the number to find factorial of series"))
if n<0:
    print("please enter the negative number are not valid")
elif n==0:
    print("The factorial for zero is one")
else:
    print("the factorial is",n,"is a :",fact_lin(n))