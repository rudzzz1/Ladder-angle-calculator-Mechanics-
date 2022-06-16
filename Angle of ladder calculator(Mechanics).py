from tkinter import *
from tkinter.messagebox import *

window = Tk()
window.title("Mechanics IA - 2")

photo1 = PhotoImage(file ="2.png")
Label (window, image = photo1, bg = "black"). grid(row =0, column = 0, sticky = E)

class ladder:
    
    def __init__(self, LengthOfLadder, AngleWithTheWall, StaticFrictionWall, StaticFrictionGround, WeightOfMan, WeightOfLadder):
        self.LengthOfLadder = LengthOfLadder
        self.AngleWithTheWall = AngleWithTheWall
        self.StaticFrictionWall = StaticFrictionWall
        self.StaticFrictionGround = StaticFrictionGround
        self.WeightOfMan = WeightOfMan
        self.WeightOfLadder = WeightOfLadder
    
    def get_LengthOfLadder(self):
        self.LengthOfLadder = float(input("\nEnter the length of the ladder in meters, \n l = "))
        return self.LengthOfLadder
         
    def get_AngleWithTheWall(self):
        self.AngleWithTheWall = float(input("Enter the angle which the ladder makes with the wall in degrees, \n a = "))
        return self.AngleWithTheWall
    
    def get_StaticFrictionWall(self):
        self.StaticFrictionWall = float(input("Enter the static friction between the ladder and the wall, \n x = "))
        return self.StaticFrictionWall
        
    def get_StaticFrictionGround(self):
        self.StaticFrictionGround = float(input("Enter the static friction between the ladder and the ground, \n y = "))
        return self.StaticFrictionGround
    
    def get_WeightOfLadder(self):
        self.WeightOfLadder = float(input("Enter the weight of ladder in Newtons, \n Wl = "))
        return self.WeightOfLadder
        
    def get_WeightOfMan(self):
        self.WeightOfMan = float(input("Enter the weight of man climbing on the ladder in Newtons, \n W = "))
        return self.WeightOfMan
    
    
Problem = ladder(1, 1, 1, 1, 1, 1)

Problem.get_LengthOfLadder()
Problem.get_AngleWithTheWall()
Problem.get_StaticFrictionWall()
Problem.get_StaticFrictionGround()
Problem.get_WeightOfLadder()
Problem.get_WeightOfMan()

Problem.AngleWithTheWall = Problem.AngleWithTheWall * 3.14/180

x = Problem.WeightOfLadder + Problem.WeightOfMan
y = Problem.StaticFrictionGround * Problem.StaticFrictionWall
y += 1

# Here,
# N2 - Problem.StaticFrictionGround * N1 = 0
# N2 = Problem.StaticFrictionGround * N1
# Also,
# N2 * Problem.StaticFrictionWall + N1 - Problem.WeightOfLadder - Problem.WeightOfMan = 0
# Substituting for N2,
# Problem.StaticFrictionGround * N1 * Problem.StaticFrictionWall + N1 - Problem.WeightOfLadder - Problem.WeightOfMan = 0
# Problem.WeightOfLadder + Problem.WeightOfMan = N1(Problem.StaticFrictionGround * Problem.StaticFrictionWall + 1)
# Thus, N1 = x / y

N1 = x / y
N2 = Problem.StaticFrictionGround * N1

import numpy as np

a = N2 * Problem.LengthOfLadder * np.cos(Problem.AngleWithTheWall)
b = Problem.StaticFrictionWall * N2 * Problem.LengthOfLadder * np.sin(Problem.AngleWithTheWall)
c = Problem.WeightOfLadder * Problem.LengthOfLadder/2 * np.sin(Problem.AngleWithTheWall)
d = Problem.WeightOfMan * np.sin(Problem.AngleWithTheWall)

# Let P be the length climbed on the ladder after which it slips thus,
# - (N2 * Problem.LengthOfLadder * np.cos(Problem.AngleWithTheWall)) - (Problem.StaticFrictionWall * N2 * Problem.LengthOfLadder * np.sin(Problem.AngleWithTheWall)) + (Problem.WeightOfLadder * Problem.LengthOfLadder/2 * np.sin(Problem.AngleWithTheWall)) +  (Problem.WeightOfMan * P * np.sin(Problem.AngleWithTheWall)) = 0
# Thus,
# - a - b + c + (Problem.WeightOfMan * P * np.sin(Problem.AngleWithTheWall)) = 0
# a + b - c = dp

m = a + b - c
p = m/d

q = "meters"
print("\nThe length till which man can climb on ladder and it wouldn't slip is : ", (round(p,3)), q)

