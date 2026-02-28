#Input a dictionary from user
user_inp=input("Enter the key to proceed or quit to exit ")
dict={}
while(user_inp!='quit'):
    val=input("Enter the value ")
    dict[user_inp]=val
    user_inp=input("Enter the key to proceed or quit to exit ")
if(len(dict)>0):
    print("Dictionary is: "+str(dict))
else:
    print("Dictionary is empty")