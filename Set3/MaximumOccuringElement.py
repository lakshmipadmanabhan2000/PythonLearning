#Find maximum occuring element in list
user_inp=input("Enter list of strings: ")
my_list=list(map(str,user_inp.split()))
dict={}
for i in my_list:
    if(i in dict):
        dict[i]+=1
    else:
        dict[i]=1
r=sorted(dict,key=dict.get,reverse=True)[0]
print(str(dict))
print(max(dict)) # returns i ..find largest key
print(max(dict,key=dict.get)) #returns h..finds key with highest value

