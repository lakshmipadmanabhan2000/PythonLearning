def reverse(n):
    rev=0
    while(n!=0):
        d=n%10
        n=n//10 
        rev=rev*10+d
    return rev
n=int(input("Enter a number: "))
n_rev=reverse(n)
if(n==n_rev):
    print("Palindrome")
else:
    print("Not a palindrome")

