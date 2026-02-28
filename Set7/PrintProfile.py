#Using kwargs print user profile
def my_fn(**kwargs):
    for k,v in kwargs.items():
        print(str(k)+" : "+str(v))
    print("End")
my_fn( name='lakshmi',age=25,gender='Female',language='Python')
my_fn( name='X',age=40,gender='Male',experience=10,role="Senior")
