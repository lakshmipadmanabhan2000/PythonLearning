#Create vehicle class that implements Inheritence and Method overriding
class Vehicle:
    def __init__(self,name,mileage):
        self.name=name
        self.mileage=mileage
    def getMileage(self):
        return self.mileage
    def displayMsg(self):
        print("From Vehicle")
class Car(Vehicle):
    def start(self):
        print("Started "+self.name)
    def run(self):
        print('Running')
    def stop(self):
        print("Stopped "+self.name)
    def displayMsg(self):
        print("From Car")
v1=Car('Maruti',20)
print(v1.mileage)
v1.start()
v1.run()
v2=Car('VolksWagon',10)
print(v2.mileage)
v2.start()
v2.run()

v1.stop()
v2.stop()
v1.displayMsg()
c1=Vehicle('X',60)
c1.displayMsg()