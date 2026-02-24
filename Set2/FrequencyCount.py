#Frequency of each letter in a string
a=input("Enter string: ")
dict={}
for i in a:
    if(i in dict):
        dict[i]+=1
    else:
        dict[i]=1
for key in dict:
    print("Frequency of {} is {}".format(key,dict[key]))