#Create student class that returns Grade
import numpy as np
class Student:
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
        self.marks=[]
    def add_mark(self,mark):
        self.marks.append(mark)
    def avg_marks(self):
        avg=np.mean(self.marks)
        return avg
    def compute_grade(self):
        avg=self.avg_marks()
        if(avg>=90):
            return 'A'
        elif(avg>=80):
            return 'B'
        elif(avg>=70):
            return 'C'
        elif(avg>60):
            return 'D'
        elif(avg>=45):
            return 'Pass'
        else:
            return 'Fail'
s1=Student("Lakshni",1)
s1.add_mark(89)
s1.add_mark(97)
s1.add_mark(94)
print(f"Grade of {s1.name} is: {s1.compute_grade()}")

s2=Student("X",2)
s2.add_mark(40)
s2.add_mark(70)
s2.add_mark(60)
print(f"Grade of {s2.name} is: {s2.compute_grade()}")