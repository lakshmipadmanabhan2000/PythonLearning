#Create a dictionary from two lists
keys=['a','b','c']
values=[10,20,30]
#approach1
d={k:v for k,v in zip(keys,values)}
print(d)
#approach2
d1={}
for i in range(len(keys)):
    d1[keys[i]]=values[i]
print(d1)
