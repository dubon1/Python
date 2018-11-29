"""
Lab Assignment #4
Daniel Wang (ID #20333426)

This class is responsible for letting the user compare 2 or more country
languages, but with the following additional features:
    1. Ask the user for a letter, then print the list of country names starting
    with that letter and print a corresponding counting number, one for each
    country name.

    2. Ask the user to choose a number (which means the user indirectly chooses
    a corresponding name)

    3.  Keep running the previous 2 steps until you get at least 2 valid names
    and the user has entered a newline only (Enter key) to stop.

    4. Print the common language among the chosen countries, and print all
    languages from the chosen countries
"""

from languages import Languages


class LanguageUI(Languages):
    def __init__(self):
        super().__init__()
        self.sortedDict = {}


    def compare(self):
        """This method """
        if len(self.sortedDict) == 0:
            self.sortedDict = self.sortDict(self.country_languages)

        countries_already_chosen = []

        print("\nCompare languages")

        while len(countries_already_chosen) < 2:
            print("Need at least 2 countries")
            letter = self.__getLetter()

            while letter != "":
                print("Country names starting with " + letter.upper())
                starting_countries = self.sortedDict[letter.upper()]

                for i in range(len(starting_countries)):
                    print(str(i + 1) + " " + starting_countries[i])

                country_num = self.__chooseNum(starting_countries)
                chosen_country = starting_countries[country_num - 1]

                print(chosen_country + " chosen")
                countries_already_chosen.append(chosen_country)

                if len(countries_already_chosen) < 2:
                    print("Need at least 2 countries")

                letter = self.__getLetter()

        country_set_list = []

        for country in countries_already_chosen:
            country_set_list.append(self.country_languages[country])

        common_langs = set.intersection(*country_set_list)
        all_langs = set.union(*country_set_list)

        if len(common_langs) == 0:
            print("No common language")

        else:
            print("Common language: ", end="")

            for lang in common_langs:
                print(lang, end=" ")

            print()

        print("All languages: ", end="")

        for lang in sorted(all_langs):
            print(lang, end=" ")

        print()


    def __getLetter(self):
        """This method asks the user for a letter, then prints the list of
        country names starting with that letter and prints a corresponding
        counting number , one for each country name."""

        letter = input("Enter first letter of country name: ")

        if letter == "":
            return letter

        while len(letter) != 1 or not letter.isalpha():
            letter = input("Enter first letter of country name: ")

        return letter


    def __chooseNum(self, countries_starting_with_letter):
        """This method prompts the user to choose a number which corresponds
        to a country name that will be added to the list of countries that
        will be compared against each other."""

        num = input("Enter a number corresponding to a country name: ")

        while not num.isnumeric() or not (int(num) in range(1,
                                    len(countries_starting_with_letter) + 1)):
            if not num.isnumeric():
                print("Input is not a number")
                num = input("Enter a number corresponding to a country name: ")

            elif not (int(num) in range(1, len(
                    countries_starting_with_letter) + 1)):
                print("number is not within range")
                num = input("Enter a number corresponding to a country name: ")

        country_num = int(num)

        return country_num