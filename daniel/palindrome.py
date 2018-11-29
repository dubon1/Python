#!/usr/bin/python3

def is_palindrome(s):
  s_reverse=s[::-1] 

  if s.lower() == s_reverse.lower(): 
     return(True)
  else:
     return(False)

print(is_palindrome('Deleveled'))
  
    






