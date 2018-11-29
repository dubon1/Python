#!/usr/bin/python3

with open("bitbucket_may") as f1, open("bitbucket_email.txt", 'w') as f2:
  for each_line in f1:
   array=each_line.strip().split(",")
   f2.write(array[2] +  ',')
 # print(array[2])

