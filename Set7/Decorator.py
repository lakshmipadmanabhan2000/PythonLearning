#Simple decorator to title case string
def titleCase(my_fn):
    def innerFn():
        return my_fn().title()
    return innerFn
@titleCase
def my_fn():
    inp=input("Enter string: ")
    return inp
print(my_fn())