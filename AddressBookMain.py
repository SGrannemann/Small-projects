#!/usr/bin/env python3

import csv
import re


def die():
    """Function used for debugging purposes.


    Call it in all conditional branches that should never be evaluated.
    Prints to the command line and makes a clean exit."""
    print("this should not be evaluated.")
    exit(0)


def createEntry():
    print("createEntry was activated.")
    name = input(phrase.format('name'))
    surname = input(phrase.format('surname'))
    while True:
        try:
            age = int(input(phrase.format('age')))
            break
        except ValueError:
            print('Please enter a number.')
            continue
    while True:
        street = input(phrase.format('street and housenumber'))
        if streetChecker(street):
            break
    while True:
        city = input(phrase.format('zipcode and city'))
        if cityChecker(city):
            break


def streetChecker(street):
    streetRegExObject = re.compile(r'([a-zA-Z]+(\s|-)?)+\s\d{1,3}')
    if streetRegExObject.findall(street):
        print('correct street entered.')
        return True
    else:
        print('no regex match found.')
        return False


def cityChecker():
    print("checking the city.")


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



#for key, value in path_ID_dict.items():
    #myOutputFile.writerow([key, value])



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
