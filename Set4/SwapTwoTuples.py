#Swap two tuples.
user_inp1=input("Enter elements in first tuple separated by spaces: ")
user_inp2=input("Enter elements in second tuple separated by spaces: ")
t1=tuple(map(int,user_inp1.split()))
t2=tuple(map(int,user_inp2.split()))
print("First tuple: "+str(t1))
print("Second tuple: "+str(t2))
t1,t2=t2,t1
print("After swapping: ")
print("First tuple: "+str(t1))
print("Second tuple: "+str(t2))