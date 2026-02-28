user_inp1=input("Enter elements in tuple separated by spaces: ")
t1=tuple(map(str,user_inp1.split()))
(item1,*items)=t1
print(item1)
print(items)