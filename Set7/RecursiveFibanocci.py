#Find nth number in fibanocci series
def fibanocci(n):
    if(n<0):
        raise ValueError("Input a non-negative number")
    if(n==0 or n==1):
        return n
    return fibanocci(n-1)+fibanocci(n-2)
term=int(input("Enter number: "))
f=fibanocci(term)
print(f"{term}th number in fibanocci series is: {f} ")