#!/usr/bin/env python3

import csv
import re
import collections
import pyinputplus as pyip
import pprint
import datetime
from pathlib import Path




def die():
    """Function used for debugging purposes.


    Call it in all conditional branches that should never be evaluated.
    Prints to the command line and makes a clean exit."""
    print("this should not be evaluated.")
    exit(0)


def createEntry():

    data = collections.OrderedDict()
    print("createEntry was activated.")
    name = pyip.inputStr(phrase.format('name'),
                         blockRegexes=[(r'\d+',
                                        "Names should contain only letters.")])
    data['Name'] = name

    surname = pyip.inputStr(phrase.format('surname'),
                            blockRegexes=[(r'\d+',
                                          "Names should contain only letters.")])
    data['Surname'] = surname

    birthday = pyip.inputDate(phrase.format('Birthday') + 'Blank to skip.',
                              blank=True)

    if type(birthday) == datetime.date:
        data['Birthday'] = str(birthday.day) + '.' + str(birthday.month) + '.' + str(birthday.year)
    else:
        data['Birthday'] = 'Null'

    street = pyip.inputRegex(streetRegEx,
                             prompt=phrase.format('street and housenumber'))
    data['Street'], data['Housenumber'] = partition_street(street, streetRegEx)

    city = pyip.inputRegex(cityRegex, prompt=phrase.format('zipcode and city'))
    data['zipcode'], data['city'] = partition_city(city, cityRegex)


    print(data)
    fieldnames = list(data.keys())
    path = Path.cwd()/'AddressBook.csv'
    if not path.is_file():
        file = open("AddressBook.csv", "a+", newline='')
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)
    else:
        file = open("AddressBook.csv", "a+", newline='')
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(data)
    file.close()



def partition_street(street, regexString):
    streetRegExObject = re.compile(regexString)
    mo = streetRegExObject.search(street)
    # group 1 is name of the street, group 2 is the housenumber
    return (mo.group(1), mo.group(2))


def partition_city(city, regexString):
    cityCheckerRegExObject = re.compile(regexString)
    mo = cityCheckerRegExObject.search(city)
    # group 1 is the zip code, group 2 is the city name
    return (mo.group(1), mo.group(2))


def reviewInformation():
    print("reviewInformation was activated.")


def deleteInformation():
    print("deleteInformation was activated.")


def updateInformation():
    print("updateInformation was activated.")


phrase = 'Please provide the {}. \n'
streetRegEx = r'([a-zA-Z-\s]+)\s(\d{1,3})$'
cityRegex = r'^(\d{5})\s([a-zA-Z-\s]+)'

# for key, value in path_ID_dict.items():
# myOutputFile.writerow([key, value])

###############################################################################
if __name__ == "__main__":
    #myOutputFile = csv.writer(open("AddressBook.csv", "w"))
    print("Hello and welcome to the address book. ")

    user_input = pyip.inputMenu(['create an entry', 'read existing information',
                                'update information', 'delete information',
                                 'quit'], numbered=True)
    if user_input == 'quit':
        print('Quitting program...')
        exit(0)
    elif user_input == 'create an entry':
        createEntry()
    elif user_input == 'read existing information':
        reviewInformation()
    elif user_input == 'update information':
        updateInformation()
    elif user_input == 'delete information':
        deleteInformation()
