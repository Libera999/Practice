#tabulation Bottom Up, time and space complexity O(n) vs time O(2^n) with ordinary recursion

def fib(n):
    res[0]=0
    res[1]=1

    for i in range(2,n):
        res[i]=res[i-1]+res[i-2]

    return res[n]

    


