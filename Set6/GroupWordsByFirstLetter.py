#Group words by first letter in a sentence
sent=input("Enter sentence: ")
lis=sent.split(' ')
dict={}
for i in lis:
    k=i[0].upper()
    if(k not in dict.keys()):
        dict[k]=[]
    dict[k].append(i)
print(str(dict))