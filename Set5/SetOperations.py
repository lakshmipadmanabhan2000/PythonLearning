#Perform different set operations
user_inp1=input("Enter elements in first set separated by spaces: ")
user_inp2=input("Enter elements in second set separated by spaces: ")
set1=set(map(str,user_inp1.split()))
set2=set(map(str,user_inp2.split()))
#display sets
print("Set 1: "+str(set1))
print("Set 2: "+str(set2))
#Union
set3=set1.union(set2)
print("Union is Set3: "+ str(set3))
#Intersection
set4=set1.intersection(set2)
print("Intersection is Set4: "+ str(set4))
#Difference
set5=set1.difference(set2)
print("Difference is Set5: "+str(set5))
#Check if set1 is a subset of set2
if(set1.issubset(set2)):
    print("Set1 is a Subset of Set2.")
else:
    print("Set1 is not a Subset of Set2.")
#Check if set4 is a subset of set1
if(set4.issubset(set1)):
    print("Set4 is a Subset of Set1.")
else:
    print("Set4 is not a Subset of Set1.")

set6=set1.symmetric_difference(set2)
print("Symmetric Difference is Set5: "+str(set6))

elem=input("Enter element to be removed from set1: ")
try:
    #Remove element from Set
    set1.remove(elem)
except Exception as e:
    print(e)
    print("Element no present")
else:
    print("Set1 updated: "+str(set1))
finally:
    #Add element to Set
    set1.add('DONE')
    print("Set Operations Done")    
    print(str(set1))