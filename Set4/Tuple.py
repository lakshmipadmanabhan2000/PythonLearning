#Create tuple and access elements
user_inp=input("Enter elements in tuple separated by space: ")
tup=tuple(map(str,user_inp.split()))
#display user input as tuple
print(str(tup))
#display element wise 
for i in tup:
    print(i)
#display user input as tuple
print("First element in tuple is: "+tup[0])
print("Last element in tuple is: "+tup[-1])
if(len(tup)>1):
    print("First 2 elements in tuple is: "+str(tup[0:3]))
    print("Last 4 elements in tuple is: "+str(tup[-1:-5:-1]))
