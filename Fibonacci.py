def fib_recursion(n,cache):

    if n==0: return 0
    elif n==1: return 1

    if cache[n]==0:
        cache[n]=fib_recursion(n-1,cache)+fib_recursion(n-2,cache)

    print(cache)
    return cache[n]

n=int(input("Fib number:"))
array=[0]*(n+1)            ##cache array of zeroes

f=fib_recursion(n,array)
print(f)

