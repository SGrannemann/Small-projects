#!/usr/bin/env python3

import csv


def die():
    """Function used for debugging purposes.


    Call it in all conditional branches that should never be evaluated.
    Prints to the command line and makes a clean exit."""
    print("this should not be evaluated.")
    exit(0)


def addInformation():
    print("addInformation was activated.")


def reviewInformation():
    print("reviewInformation was activated.")


def deleteInformation():
    print("deleteInformation was activated.")

def updateInformation():
    print("updateInformation was activated.")


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
            addInformation()
        elif user_input.lower() == 'r':
            reviewInformation()
        elif user_input.lower() == 'u':
            updateInformation()
        elif user_input.lower() == 'd':
            deleteInformation()
        else:
            die()
