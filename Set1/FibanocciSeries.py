#print fibanocci series upto n
n=int(input("Enter a number: "))
a=0
b=1
print(a)
print(b)
c=a+b
while(c<=n):
    print(c)
    a=b
    b=c
    c=a+b