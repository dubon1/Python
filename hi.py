#!/usr/bin/python3
import time
import datetime

def world():
 print("Today is ", datetime.datetime.now().strftime("%Y-%m-%d %A  %H:%M")) 

shark="Dallas"

class Octopus:
 def __init__(self, name, color):
   self.color=color
   self.name=name
 def tell_me_about_the_octopus(self):
   print("This Octopus is " + self.color + ".")
   print(self.name + " is my pet's name.")
