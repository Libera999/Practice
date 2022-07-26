def fib(n,cache):

    if n==0: return 0
    elif n==1: return 1

    if cache[n]==0:
        cache[n]=fib(n-1,cache)+fib(n-2,cache)

    print(cache)
    return cache[n]

n=int(input("Fib number:"))
array=[0]*(n+1)            ##cache array of zeroes

f=fib(n,array)
print(f)

