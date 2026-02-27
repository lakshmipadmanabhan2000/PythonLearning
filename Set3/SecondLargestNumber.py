#Find second largest element in a list
inp=input("Enter list of numbers separated by spaces: ")
list_inp=list(map(int,inp.split()))
list_inp.sort()
print(list_inp[len(list_inp)-2])
