#Multiplication Table of n
n=float(input("Enter an number : "))
for i in range(1,11):
    print(str(n)+" x "+str(i)+ "= "+str(round(n*i,2)))