#Find number of occurence of element in tuple
user_inp=input("Enter elements in tuple separated by space: ")
tup=tuple(map(str,user_inp.split()))
k=input("Enter element for which count needs to be found: ")
c=tup.count(k)
print("No: of occurences: "+str(c))