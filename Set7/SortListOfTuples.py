# Sort list of tuples
def sort(lT):
    lT.sort(key=lambda x:x[1])
    print("Sorted list is: "+str(lT))
tupList=[('Physics',100),('English',74),('Maths',97),('History',80),("Chemisty",77)]
sort(tupList)