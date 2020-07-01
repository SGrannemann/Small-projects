#!/usr/bin/env python3

import csv
import re
import collections


def die():
    """Function used for debugging purposes.


    Call it in all conditional branches that should never be evaluated.
    Prints to the command line and makes a clean exit."""
    print("this should not be evaluated.")
    exit(0)


def createEntry():
    # list_of_keys = ['Name', 'Surname', 'Age', 'Street', 'Housenumber', 'ZIP',
    #                'City']
    data = collections.OrderedDict()
    print("createEntry was activated.")
    while True:
        name = input(phrase.format('name'))
        if name.isalpha():
            data['Name'] = name
            break
    while True:
        surname = input(phrase.format('surname'))
        if surname.isalpha():
            data['Surname'] = surname
            break
    while True:
        try:
            age = int(input(phrase.format('age')))
            data['Age'] = str(age)
            break
        except ValueError:
            print('Please enter a number.')
            continue
    while True:
        street = input(phrase.format('street and housenumber'))
        street_dict = streetChecker(street)
        if street_dict:
            data['Street'] = street_dict['Street']
            data['Housenumber'] = street_dict['Housenumber']
            break
        print('Please enter the street and housenumber in a valid format.')
    print(street_dict)

    while True:
        city = input(phrase.format('zipcode and city'))
        city_dict = cityChecker(city)
        if city_dict:
            break
        print(' Please enter the zip code and city in a valid format.')
    print(city_dict)

    print(data)
    # for key, value in path_ID_dict.items():
    #    myOutputFile.writerow([key, value])


def streetChecker(street):
    streetRegExObject = re.compile(r'([a-zA-Z]+(\s|-)?)+\s(\d{1,3})')
    mo = streetRegExObject.search(street)
    dict = {}
    if mo:
        print('correct street entered.')
        dict['Street'] = mo.group(1)
        dict['Housenumber'] = mo.group(3)
    else:
        print('no regex match found.')
    return dict


def cityChecker(city):
    # does not correctly work for Porta Westfalica
    cityCheckerRegExObject = re.compile(r'(\d{5})\s([a-zA-Z]+(\s|-)?)+')
    mo = cityCheckerRegExObject.search(city)
    dict = {}
    if mo:
        print('correct city entered.')
        dict['zipcode'] = mo.group(1)
        dict['city'] = mo.group(2)
    else:
        print('no regex match found.')
    return dict


def reviewInformation():
    print("reviewInformation was activated.")


def deleteInformation():
    print("deleteInformation was activated.")


def updateInformation():
    print("updateInformation was activated.")


phrase = 'Please provide the {}. \n'
names = []
surnames = []
ages = []
addresses = []
emails = []
phone_numbers = []


# for key, value in path_ID_dict.items():
# myOutputFile.writerow([key, value])

###############################################################################
if __name__ == "__main__":
    myOutputFile = csv.writer(open("AddressBook.csv", "w"))
    print("Hello and welcome to the address book. ")
    while True:
        while True:
            user_input = input("Select an option: \n (c)reate an entry, \n (r)ead existing information \n (u)pdate information \n (d)elete information \n (q)uit?. \n")
            if user_input.lower() in ['c', 'r', 'u', 'd', 'q']:
                break
            else:
                print("Please select one of the available options.")
                continue
        if user_input == 'q':
            break
        elif user_input.lower() == 'c':
            createEntry()
        elif user_input.lower() == 'r':
            reviewInformation()
        elif user_input.lower() == 'u':
            updateInformation()
        elif user_input.lower() == 'd':
            deleteInformation()
        else:
            die()
