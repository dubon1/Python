#!/usr/bin/python3

def check(first_last):
    ufile=open('d3.txt')
    yahoo="miss"
    for eline in ufile:
      a4=eline.split("|")
      if first_last in eline:
         yahoo=a4[1]
         break
    return yahoo

with open("user_tab1.csv", encoding="ISO-8859-1") as f1, open("match_user_tag.txt", 'w') as f3:
  next(f1)
  f3.write("First Name|Last Name|User Name|Job Title|Department|Teamcenter Role|Teamcenter Group|")
  f3.write("Office|Computer Name|Catia Integration|Computer Name" + '\n')
  for ea in f1:
    a2=ea.strip().split("\t")

    google=check(a2[2].lower())
    if "miss" in google:
       f3.write(a2[0] + '|' +a2[1] + '|' + a2[2] + '|' + a2[3] + '|' + a2[4] + '|' + a2[5] + '|' + a2[6] + '|' + a2[7] + '|' + 'MISS' + '\n')
    else:
       f3.write(a2[0] + '|' +a2[1] + '|' + a2[2] + '|' + a2[3] + '|' + a2[4] + '|' + a2[5] + '|' + a2[6] + '|' + a2[7] + '|' + google)

