#Check if two strings are Anagrams
def is_Anagram(a,b):
    s1= sorted(a.lower().replace(" ",""))
    s2=sorted(b.lower().replace(" ",""))
    return s1==s2
a=input("Enter first string: ")
b=input("Enter second string: ")
if(is_Anagram(a,b)):
    print("{} and {} are Anagrams".format(a,b))
else:
    print("%s and %s are not Anagrams"%(a,b))