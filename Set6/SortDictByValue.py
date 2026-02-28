#Sort a dictionary by its value
import numpy as np
dict1={'a':100,'b':20,'c':13,'d':5,'e':7}
for k,v in dict1.items():
    print (str(k) +" : "+str(v))

print("Sorted dictionary is: ")

k=list(dict1.keys())
v=list(dict1.values())
idx=np.argsort(v)
print(idx)
result={k[i]:v[i] for i in idx}
print("Result is : "+str(result))

#Display key with largest value
max_key=list(result.keys())[-1]
max_value=result[max_key]
print("Key with max value is: "+str(max_key)+" and value is:"+ str(max_value))