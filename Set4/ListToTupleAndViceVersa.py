#Convert list to tuple and vice versa
user_tup=input("Enter elements in tuple separated by space: ")
tup=tuple(map(str,user_tup.split()))
my_list=list(tup)
print("List is: "+str(my_list))
user_lis=input("Enter elements in list separated by space: ")
my_lis2=list(map(str,user_lis.split()))
my_tup=tuple(my_lis2)
print("Tuple is: "+str(my_tup))