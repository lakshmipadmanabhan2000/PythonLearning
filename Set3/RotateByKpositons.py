#Rotate list by k positions
user_inp=input("Enter list of items separated by ,: ")
my_list=list(map(str,user_inp.split(',')))
pos=int(input("Enter by what postion : "))
n=len(my_list)
k=pos%n
new_lis=my_list[k:]+my_list[0:k] #first k elements at last

print(str(new_lis))

new_lis2=my_list[-k-1:]+my_list[0:-k] #last k elements at first

print(str(new_lis2))