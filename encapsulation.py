class Car:
    def __init__(self):
        self.__updatesoftware() #private class
    def drive(self):
        print("car is driving")
    def __updatesoftware(self):
        print("carb is updated")

blackcar=Car() #private class cannot be called outside the class
blackcar.drive()

#chaging private variables within the class
class car:
__maxspeed =0
__name=""

def __init__(self):
    self.__maxspeed=100
    self.__name="Supercar"

def drive(self):
    print("car is driving")


