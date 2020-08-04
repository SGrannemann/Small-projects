#!/usr/bin/env python3

import csv
import re
import pyinputplus as pyip
import pprint
import datetime
from pathlib import Path




def createEntry():
    # TODO: add check if entry already exists

    print("createEntry was activated.")
    list_of_entries = []
    while True:
        name = pyip.inputStr(phrase.format(' first name'),
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
            data['Birthday'] = 'Empty'

        street = pyip.inputRegex(streetRegEx,
                                 prompt=phrase.format('street and housenumber'))
        data['Street'], data['Housenumber'] = partition_street(street, streetRegEx)

        city = pyip.inputRegex(cityRegex, prompt=phrase.format('zipcode and city'))
        data['Zipcode'], data['City'] = partition_city(city, cityRegex)

        if path.is_file():
            try:
                file = open("AddressBook.csv", "r", newline='')
                filereader = csv.DictReader(file)
            except IOError:
                print('File not found.')
            list1 = [name.lower(), surname.lower()]
            for row in filereader:
                if all(any(entered == value.lower() for value in list(row.values())) for entered in list1):
                    print('An entry for that person already exists.')
                    data.clear()
                else:
                    list_of_entries.append(data.copy())
            file.close()
        else:
            list_of_entries.append(data.copy())

        inputForBreak = pyip.inputMenu(['Enter new entry', 'Save and quit'],
                               numbered=True)
        if inputForBreak == 'Enter new entry':
            continue
        if inputForBreak == 'Save and quit':
            break
    if data:
        fieldnames = list(data.keys())
        if not path.is_file() :

            try:
                file = open("AddressBook.csv", "a+", newline='')
            except IOError:
                print('Writing to file not possible.')

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for entry in list_of_entries:
                writer.writerow(entry)
        else:
            try:
                file = open("AddressBook.csv", "a+", newline='')
            except IOError:
                print('Writing to file not possible.')

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            for entry in list_of_entries:
                writer.writerow(entry)
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
    # TODO: Add exception handling for file not available
    # TODO:
    print("reviewInformation was activated.")



    file = open("AddressBook.csv", "r", newline='')
    filereader = csv.DictReader(file) # fieldnames=fieldnames)


    entry = pyip.inputMenu(['show all content', 'show a single entry',
                           'show all entries that match a condition'],
                           numbered=True)
    if entry == 'show all content':
        for row in filereader:
            print(row)
    if entry == 'show a single entry':
        singleEntry(filereader)
    if entry == 'show all entries that match a condition':
        filterEntries(filereader)
    file.close()





def singleEntry(filereader):
    name = pyip.inputStr(phrase.format(' first name'),
                         blockRegexes=[(r'\d+',
                                        "Names should contain only letters.")])
    surname = pyip.inputStr(phrase.format('surname'),
                            blockRegexes=[(r'\d+',
                                          "Names should contain only letters.")])
    list1 = [name.lower(), surname.lower()]
    for row in filereader:

        if all(any(entered == value.lower() for value in list(row.values())) for entered in list1):
            print(row)


def filterEntries(filereader):
    userInput = input('Enter a name, surname, street or city for which you want to display all matching entries.\n')
    for row in filereader:
        if any(userInput.lower() in value.lower() for value in list(row.values())):
            print(row)


def deleteInformation():
    # TODO: add exception handling for file
    print("deleteInformation was activated.")
    file = open("AddressBook.csv", "r", newline='')
    filereader = csv.DictReader(file)
    for row in filereader:
        print(row)
    list_of_entries = [dict for row in filereader]
    print(list_of_entries)
    #data = prepareDict()
    # TODO: add option to delete all entries / empty the AddressBook
    # TODO: add a boolean option to function single entry that allows you to
    # switch between displaying an entry and deleting

def deleteEntry(filereader):
    name = pyip.inputStr(phrase.format(' first name'),
                         blockRegexes=[(r'\d+',
                                        "Names should contain only letters.")])
    surname = pyip.inputStr(phrase.format('surname'),
                            blockRegexes=[(r'\d+',
                                          "Names should contain only letters.")])
    list1 = [name.lower(), surname.lower()]
    for row in filereader:
        if all(any(entered == value.lower() for value in list(row.values())) for entered in list1):
            pprint.pprint(row)


def updateInformation():
    print("updateInformation was activated.")


path = Path.cwd()/'AddressBook.csv'
phrase = 'Please provide the {}. \n'
streetRegEx = r'([a-zA-Z-\s]+)\s(\d{1,3})$'
cityRegex = r'^(\d{5})\s([a-zA-Z-\s]+)'
data = {}


###############################################################################
if __name__ == "__main__":

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
