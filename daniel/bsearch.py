#!/usr/bin/python3


def binary_search(item_list, item):
     first = 0
     round=0
     last = len(item_list)-1  # index information
     print(' 1st = ', first, '  last ', last)
     found = False
     while( first<=last and not found):
      mid = (first + last)//2
      round+=1
      if item_list[mid] == item :
         found = True
      else:
          if item < item_list[mid]:
             last = mid - 1
          else:
             first = mid + 1	
     print('at least round ', round)
     return found
	
print(binary_search([1,2,3,5,8, 10, 13, 16, 18, 20, 25, 30, 33, 38, 39, 40, 56], 16))
print(binary_search([1,2,3,5,8], 5))

