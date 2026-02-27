inp1= input("Enter first integer list separated by spaces: ")
inp2= input("Enter second integer list separated by spaces: ")
l1=list(map(int,inp1.split()))
l2=list(map(int,inp2.split()))
l3=[]
for a in l1:
    if(a in l2):
        l3.append(a)
if(len(l3)==0):
    print("No common elements")
else:
    print("Common elements are: "+ str(l3))