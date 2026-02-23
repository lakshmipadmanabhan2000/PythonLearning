#Garding system
marks= float(input("Enter total marks:  "))
if(marks>=90):
    print("Outstanding")
elif(marks>=85):
    print("A+")
elif(marks>=80):
    print("A")
elif(marks>=75):
    print("B+")
elif(marks>=70):
    print("B")
elif(marks>=45):
    print("Pass")
else:
    print("Fail")