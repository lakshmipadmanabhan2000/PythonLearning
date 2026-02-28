#Remove duplicates in a list using Set
user_inp=input("Enter list elements separated by spaces: ")
lis=list(map(str,user_inp.split()))
set1=set(lis)
print("Set is "+str(set1))