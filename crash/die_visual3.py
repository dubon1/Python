#!/usr/bin/python3

from die import Die
import pygal

die_1=Die()
die_2=Die(10)
results=[]
for roll_num in range(50000):
 result=die_1.roll() + die_2.roll()
 results.append(result)

#print(results)
frequencies=[]
max_result=die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
 frequence=results.count(value)
 frequencies.append(frequence)

#print(frequencies)
hist=pygal.Bar()
hist.title="Results of rolling one D6 and D10 50,000 times"
hist.x_labels=['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title="Result"
hist.y_title="Frquency of result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual3.svg')



