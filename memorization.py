# fibonacci
# memorization
def fib(n,term):
 
    if n <= 1:
        return n
 
    if term[n] != 0:
        return term[n]
 
    else:
     
    # store the value of fib(n)
    
        term[n] = fib(n - 1, term) + fib(n - 2, term)
        return term[n]

term = [0 for i in range(1000)]

print(fib(6,term))

