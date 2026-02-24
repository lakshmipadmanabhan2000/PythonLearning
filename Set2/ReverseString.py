#Reverse a string and Also check if its a palindrom
def find_Reverse(str1):
    rev=""
    for a in str1:
        rev=a+rev
    print("Reverse :"+rev)
    return rev

inpStr=input("Enter a string: ")
str2=find_Reverse(inpStr.lower())
if(inpStr==str2):
    print("Palindrome String")
else:
    print("Not a Palindrome")
