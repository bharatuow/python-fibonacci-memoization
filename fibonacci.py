cache={}
def fib(n):
    #check cache value
    if n in cache:
        return cache[n]
    
    #compute nth value
    if(n==0 or n==1):
        value=n
    else:
        value=fib(n-1)+fib(n-2)
    
    cache[n]=value
    return value