#!/usr/bin/python3 

import collections
class FileOwners:

 def group_by_owners(files):

    new_dict={}
    for k, values in files.items():
        new_dict.setdefault(values, []).append(k)

    for k, v in new_dict.items():
      print('author : ', k,  ' files owns : ', v)
     


files={'Input.txt'  :   'Randy',
       'Code.py'    :   'Stanford',
       'Output.txt' :   'Randy'
} 

print(FileOwners.group_by_owners(files))

  
