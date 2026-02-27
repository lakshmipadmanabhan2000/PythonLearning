#Title case a sentence
sent=input("Enter sentence: ")
list=sent.split(' ')
w=""
for word in list:
    w=w+word.capitalize()+" "
print("Title cased w/0 title: "+w)
print("Title cased w/ title: "+sent.title())