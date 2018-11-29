"""
Lab Assignment #4
Daniel Wang (ID #20333426)

This class is responsible for reading data from the lab3.txt input file and
storing the data in the appropriate data structures. Moreover, this class
provides any common methods for the derived classes LanguageStats and LanguageUI.
"""

import collections

class Languages:
    def __init__(self):
        self.country_languages = {}
        self.frequency = collections.defaultdict(int)
        self.readInputFile()


    def readInputFile(self):
        """This method reads data from the lab3.txt input file and stores it
        in the appropriate data structures."""

        try:
            file = "lab4.txt"

            with open(file) as infile:
                for line in infile:
                    # Split each line using ',' as a delimiter
                    split_line = [x.strip() for x in line.split(",")]

                    country = split_line[0]
                    languages = set(split_line[1:])

                    for language in languages:
                        self.frequency[language] = self.frequency.get(language, 0) + 1

                    self.country_languages[country] = languages

        except IOError:
            print("Can't open " + file + ". Terminating program.")

            raise SystemExit


    def sortDict(self, dictionary):
        """This method sorts the dictionary"""
        sortedDict = {}

        for key in dictionary.keys():
            firstChar = key[0].upper()

            if firstChar not in sortedDict:
                sortedDict[firstChar] = [key]
            else:
                sortedDict[firstChar].append(key)

        for key in sortedDict:
            l = sortedDict[key]
            sortedDict[key] = sorted(l)

        return sortedDict


    def printAll(self):
        """This method prints all the data in the data structures, for testing
        purposes."""

        print("Country languages dictionary:", self.country_languages)
        print("Frequency dictionary", self.frequency)
