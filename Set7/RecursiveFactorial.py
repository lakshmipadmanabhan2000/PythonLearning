#Compute factorial using recursion
def factorial(num):
    if(num==1):
        return num
    return num *factorial(num-1)
n=int(input("Enter number: "))
p=factorial(n)
print("Factorial of {} is {}".format(n,p))