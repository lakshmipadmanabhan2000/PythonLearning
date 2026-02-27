#Flatten Nested List
import numpy as np
n=int(input("Enter number of sub lists: "))
main_list=[]
for i in range(n):
    user_inp=input(f"Enter {i+1}th sublist: ")
    sub_list=list(map(int,user_inp.split()))
    main_list.append(sub_list)
print("Your nested list is "+ str(main_list))
required_list=np.concatenate(main_list).tolist()
print("Flattened list is " + str(required_list))
