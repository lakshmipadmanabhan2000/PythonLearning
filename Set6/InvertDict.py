#Invert keys and values in a dictionary
dict1={'a':1,'b':2,'c':3,'d':4,'e':5,'f':5}
keys=list(dict1.keys())
values=list(dict1.values())

dict2={}
for k,v in zip(keys,values):
    if(v not in dict2.keys()):
        dict2[v]=[]
    dict2[v].append(k)
print("Reverted dictionary is: "+str(dict2))