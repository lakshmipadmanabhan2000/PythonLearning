#polymorphism
class Shape:
    def calculate_area(self,l,b):
        return  l*b
class Rectangle(Shape):
    def calculate_area(self,l,b):
        return l*b
class Square(Shape):
    def calculate_area(self,a):
        return a*a
class Circle(Shape):
    def calculate_area(self,r):
        return 3.14*(r**2)
c=Circle()
print("Area of circle is : "+ str(c.calculate_area(2)))
r=Rectangle()
print("Area of rectangle is : "+str(r.calculate_area(3,5)))
sq=Square()
print("Area of square is : "+str(sq.calculate_area(4)))
f=Shape()
print("Area of share is " +str(f.calculate_area(4,5)))