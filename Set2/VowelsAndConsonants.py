#Count Vowels and consonants 
str1=input("Enter string: ")
vowels=['a','e','i','o','u']
vow=0
cons=0
for a in str1:
    if(a in vowels):
        vow+=1
    else:
        cons+=1
print("Number of vowels: "+ str(vow))
print("Number of consonants: "+str(cons))
