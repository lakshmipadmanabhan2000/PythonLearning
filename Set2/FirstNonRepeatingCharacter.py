#First non repeating character in a string
a=input("Enter string: ")
dict={}
for i in a:
    if(i in dict):
        dict[i]+=1
    else:
        dict[i]=1
for key in dict:
    if(dict[key]==1):
        print("First non-repeating character is %s" %(key))
        break