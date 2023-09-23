import os
from dotenv import load_dotenv

class Robot :
    def __init__(self,name,color,weight):
        self.name = name
        self.color = color
        self.weight = weight
        self.staring = None
    
    def introduce(self):
        return 'Hello my name is '+self.name

r1 = Robot("jerry","blue",40)
r2 = Robot("Tom","red",50)
r3 = Robot("Dave","black",70)
r4 = Robot("Kevin","green",30)
r1.staring = r2
r2.staring = r3
r3.staring = r4
r4.staring = r1

class Person : 
    def __init__(self,name,personality,is_sitting,robot_owned):
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting
        self.robot_owned = robot_owned
    def sit_down(self):
        if self.is_sitting == False :
            self.is_sitting = True
            print(self.is_sitting)
    def stand_up(self):
        if self.is_sitting == True :
            self.is_sitting = False
            print(self.is_sitting)

p1 = Person("Alex","aggresive",False,r2)
p2 = Person("Becky","Talkative",True,r1)
print(r1.staring.name)