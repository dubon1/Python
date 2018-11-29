#!/usr/bin/python3

#     grep   OK
def check(first_last):
    ufile=open('user_name.txt')
    yahoo=False
    for eline in ufile:
      if first_last in eline:
         yahoo=True
         break
    return yahoo

with open("tag_uname.txt", 'r') as f1, open("match_uname_tag.txt", 'w') as f3:
  for each_line in f1:
    line_array=each_line.split("|")
    google=check(line_array[1])
    if google:
       f3.write(line_array[0] + '|' + line_array[1])
