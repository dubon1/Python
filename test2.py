#!/usr/bin/python3

import numpy as np

def transpose(lst):
    newlist = []
    i = 0
    while i < len(lst):
        j = 0
        colvec = []
        while j < len(lst):
            colvec.append(lst[j][i])
            j = j + 1
        newlist.append(colvec)
        i = i + 1
    return newlist

def xyz(l):
 maxCol = len(l[0])
 for row in l:
    rowLength = len(row)
    if rowLength > maxCol:
        maxCol = rowLength
 lTrans = []
 for colIndex in range(maxCol):
     lTrans.append([])
     for row in l:
        if colIndex < len(row):
            lTrans[colIndex].append(row[colIndex])
     return(lTrans)

l = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

print(list(map(list, np.transpose(l))))

#print(transpose(l))
#print(list(map(list, zip(*l))))
