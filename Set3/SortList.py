#sort list without and with sort()
user_inp=input("Enter numbers in the list ")
my_list=list(map(int,user_inp.split()))
#print(sorted(my_list)) -->doesnt change my_list
#my_list.sort() -->changes my_list, .sort() returns none
# print(my_list)
n=len(my_list)
#Bubble sort
for i in range(n):
    for j in range(0,n-1-i):
        if(my_list[j]>my_list[j+1]):
            my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
print("Sorted list is "+str(my_list))