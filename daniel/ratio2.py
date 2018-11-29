#!/usr/bin/python3

# NG
class Crop_Ratio:

 def __init__(self, crop, weight):

   self._crop=crop
   self._weight=weight

 def add(self, name, crop_weight): 

      self._crops = name 
      self._weight = crop_weight


 def proportion(self, name):

   total_weight_specific_crop=0
   match_crop=0

   for each in self._crop:
     print('crop name is ',each._crops)
     print('the weight is ', each._weight)

   # if each == name:
   #    total_weight_specific_crop+= self._weight
   #    match_crop+=1
        
   print(total_weight_specific_crop)
   print(match_crop)
#  return total_weight_specific_crop/match_crop
   return 5


crop_ratio = Crop_Ratio('',1)
crop_ratio.add('Wheat', 4)
crop_ratio.add('Wheat', 5)
crop_ratio.add('Rice', 1)

print('Wheat ratio is ', crop_ratio.proportion('Wheat'))
print('Rice ratio is ', crop_ratio.proportion('Rice'))


