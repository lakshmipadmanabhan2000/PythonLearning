#prime numbers b/w 1 and 100
def isPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
#start from 2 since 1 is niether prime nor composite
for j in range(2,101):
    if(isPrime(j)):
        print(j)