def fib(n):
    if n==0: return 0

    a=0
    b=1
    for i in range(2,n-1):
       current=a+b
       a=b
       b=current

    return a+b

num=input("Fib_number:")
print(fib(int(num)))