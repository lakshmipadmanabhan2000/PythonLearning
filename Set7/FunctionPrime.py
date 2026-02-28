#Check a number is prime or not using function
def isBoolean(num):
    for i in range(2,num):
        if(num%i==0):
            return False
    return True
n=int(input("Enter number: "))
if(n==1):
    print(f"{n} is niether prime nor composite")
else:
    out=isBoolean(n)
    if(out):
        print(f"{n} is prime")
    else:
        print(f"{n} is composite")