# lab 4: driver code for country and language look up
# Name: Clare Nguyen

from languageStats import LanguageStats
from languageUI import LanguageUI

def main() :
    s = LanguageStats()
    print("\nThere are", s.numCountries(), "countries in the database")
    s.listAll("countries")
    print("\nThere are", s.numLanguages(), "major languages in the database")
    s.listAll("languages")
    s.topLanguages()    
    
    # uncomment the following line in one of your test runs:
    # s.listAll("nothing")
    
    # it should produce an assertionError simmilar to this:
    #Traceback (most recent call last):
    #File "C:\Users\ ... \lab4.py", line 39, in <module>
    #main()
    #File "C:\Users\ ... \lab4.py", line 15, in main
    #s.listAll("nothing")  
    # ... other error messages
    #AssertionError: Wrong input string for listAll
    #Process terminated with an exit code of 1
    

    s = LanguageUI()
    answer = 'y'
    while answer == 'y' :
        s.compare()
        answer = input("\nMore comparison? y/n: ").lower()
    
    
main()
