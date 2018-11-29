#!/usr/bin/python3

# working  
class Crop_Ratio:

 def __init__(self):

   self._crops={}
   self._total_weight=0

 def add(self, name, crop_weight): 

   if not name in self._crops:
      self._crops[name] = crop_weight 
   else: 
      self._total_weight+=crop_weight

 def proportion(self, name):

 # print(self._crops[name])
 # print(self._total_weight)
   return self._crops[name]/self._total_weight



crop_ratio = Crop_Ratio()
crop_ratio.add('Wheat', 4)
crop_ratio.add('Wheat', 5)
crop_ratio.add('Rice', 1)

print('Wheat ratio is ', crop_ratio.proportion('Wheat'))
print('Rice ratio is ', crop_ratio.proportion('Rice'))


