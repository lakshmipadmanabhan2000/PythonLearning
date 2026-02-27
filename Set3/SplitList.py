#split list to even and odd number lists
user_inp=input("Enter numbers in the list ")
my_list=list(map(int,user_inp.split()))
list_odd=[]
list_even=[]
for i in my_list:
    if(i%2==0):
        list_even.append(i)
    else:
        list_odd.append(i)
print("Even list is "+str(list_even))
print("Odd list is "+str(list_odd))