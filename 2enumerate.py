#!/usr/bin/python3

choices=['pizza', 'pasta', 'salad', 'nachos']
for idx, item in enumerate(choices, start=3):
 print (idx, item) 
print(" ")

for i in range(5):
  print(i, "  ")
print(" ")
print(" ")

ints=[8, 20, 4, 19, 56]
for i, num in enumerate(ints, start=101):
 print (i, num) 
print(" ")
print(" ")

myList=[1, 2, 3, 4, 5, 6, 7, 8]
myList[2]=103
print(myList[2])
print(myList[:2])
print(myList[2:5])
print(" ")
print(" ")

OneList=[i for i in range(10)]
for i, num in enumerate(OneList, start=101):
  print(i, num)
print(" ")
print(" ")
newList=[OneList[i] for i in range(1,8)]
for j, xxx in enumerate(newList, start=201):
  print(j, xxx)
