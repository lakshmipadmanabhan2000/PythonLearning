#Remove duplicates from a list
user_input=input("Enter integer items separated by spaces: ")
my_list=list(map(int,user_input.split()))
print(set(my_list))
