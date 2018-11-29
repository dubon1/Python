"""
Lab Assignment #4
Daniel Wang (ID #20333426)

This class is responsible for printing 5 statistics of the countries and
languages listed in the lab3.txt input file.
    1. Number of countries
    2. List of all country names
    3. Number of languages
    4. List of all languages
    5. List of the most common languages
"""

from languages import Languages

class LanguageStats(Languages):
    def __init__(self):
        super().__init__()


    def numCountries(self):
        """This method returns the number of countries."""

        return len(self.country_languages)


    def numLanguages(self):
        """This method returns the number of languages."""

        return len(self.frequency)


    def listAll(self, info):
        """This method lists all of the country names/languages. Each line of
        the string is one letter of the alphabet, starting with 'A' and ending
        with 'Z'. The country names on each line are in alphabetical order and
        are separated by comma. The lines of data are separated by a blank
        line."""

        sortedDict = {}

        assert info == "countries" or info == "languages", \
                        "Wrong input string for listAll"

        if info == "countries":
            whatToPrint = self.country_languages
            print("\nList of countries:")

        elif info == "languages":
            whatToPrint = self.frequency
            print("\nList of languages:")

        sortedDict = self.sortDict(whatToPrint)

        for k in sorted(sortedDict.keys()):
            names = sortedDict[k]

            for i in range(len(names)):
                name = names[i]

                if i != len(names) - 1:
                    print(name + ",", end=" ")
                else:
                    print(name)
            print()


    def topLanguages(self):
        """This method prints the list of most common languages (a language
        that's spoken by 10 or more countries."""

        sorted_freq = [(k, self.frequency[k]) for k in sorted(self.frequency,
                        key=self.frequency.get, reverse=True)]

        print("\nThe most common languages")
        print("Language    Num of countries")

        for lang_freq in sorted_freq:
            language = lang_freq[0]
            num_countries = lang_freq[1]

            if language == "other":
                continue
            if num_countries < 10:
                break

            # Center the text, lined up in column format
            line_width = 22 - len(language)
            print(language + "{:>{width}}".format(str(num_countries),
                                                  width=line_width))