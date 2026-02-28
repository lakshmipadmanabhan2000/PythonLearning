#Find number of occurence of element in tuple
user_inp=input("Enter elements in tuple separated by space: ")
tup=tuple(map(str,user_inp.split()))
k=input("Enter element for which index needs to be found: ")
try:
    ind=tup.index(k)
except Exception as e:
    print(e)
    print("Element not found")
else:
    print("Element found at index: "+str(ind))
finally:
    print("End of program")