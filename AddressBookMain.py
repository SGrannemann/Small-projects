#!/usr/bin/env python3

import csv
import re
import collections
import pyinputplus as pyip
import pprint
import datetime




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
    name = pyip.inputStr(phrase.format('name'),
                         blockRegexes=[(r'\d+',
                                        "Names should contain only letters.")])
    data['Name'] = name

    surname = pyip.inputStr(phrase.format('surname'),
                            blockRegexes=[(r'\d+',
                                          "Names should contain only letters.")])
    data['Surname'] = surname

    age = pyip.inputDate(phrase.format('Birthday') + 'Blank to skip.', blank=True)
    print(type(age))
    if type(age) == datetime.date:
        data['Birthday'] = str(age.day) + '.' + str(age.month) + '.' + str(age.year)
    pprint.pprint(data)

    street = pyip.inputRegex(streetRegEx,
                             prompt=phrase.format('street and housenumber'))
    street_dict = streetSplitter(street, streetRegEx)
    data['Street'] = street_dict['Street']
    data['Housenumber'] = street_dict['Housenumber']

    print(street_dict)


    city = pyip.inputRegex(cityRegex, prompt=phrase.format('zipcode and city'))
    #city_dict = citySplitter(city, cityRegex)
    #data['zipcode'] = city_dict['zipcode']
    #data['city'] = city_dict['city']
    data['zipcode'], data['city'] = citySplitter(city, cityRegex)
    print(data)
    # for key, value in path_ID_dict.items():
    #    myOutputFile.writerow([key, value])


def streetSplitter(street, regexString):
    streetRegExObject = re.compile(regexString)
    mo = streetRegExObject.search(street)
    dict = {}
    dict['Street'] = mo.group(1)
    dict['Housenumber'] = mo.group(3)

    return dict


def citySplitter(city, regexString):
    # does not correctly work for Porta Westfalica
    cityCheckerRegExObject = re.compile(regexString)
    mo = cityCheckerRegExObject.search(city)

    if mo.group(4):
        return (mo.group(1), mo.group(2)+mo.group(3)+mo.group(4))
    return (mo.group(1), mo.group(2))


def reviewInformation():
    print("reviewInformation was activated.")


def deleteInformation():
    print("deleteInformation was activated.")


def updateInformation():
    print("updateInformation was activated.")


phrase = 'Please provide the {}. \n'
streetRegEx = r'([a-zA-Z]+(\s|-)?)+\s(\d{1,3})'
cityRegex = r'(\d{5})\s([a-zA-Z]+)(\s|-)?([a-zA-Z]+)?'

# for key, value in path_ID_dict.items():
# myOutputFile.writerow([key, value])

###############################################################################
if __name__ == "__main__":
    myOutputFile = csv.writer(open("AddressBook.csv", "w"))
    print("Hello and welcome to the address book. ")
    # while True:
    #     while True:
    #         user_input = input("Select an option: \n (c)reate an entry, \n (r)ead existing information \n (u)pdate information \n (d)elete information \n (q)uit?. \n")
    #         if user_input.lower() in ['c', 'r', 'u', 'd', 'q']:
    #             break
    #         else:
    #             print("Please select one of the available options.")
    #             continue
    #     if user_input == 'q':
    #         break
    #     elif user_input.lower() == 'c':
    #         createEntry()
    #     elif user_input.lower() == 'r':
    #         reviewInformation()
    #     elif user_input.lower() == 'u':
    #         updateInformation()
    #     elif user_input.lower() == 'd':
    #         deleteInformation()
    #     else:
    #         die()

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
