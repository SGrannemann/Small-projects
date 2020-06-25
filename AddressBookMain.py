#!/usr/bin/env python3

#import csv


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








#myOutputFile = csv.writer(open("ListOfPathsAndIDs.csv", "w"))
#for key, value in path_ID_dict.items():
    #myOutputFile.writerow([key, value])


if __name__ == "__main__":

    print("Hello and welcome to the address book. ")
    while True:
        while True:
            user_input = input("Select an option: \n (a)dd new information, \n (r)eview existing information \n (d)elete information \n (q)uit?. \n")
            if user_input in ['a', 'r', 'd', 'q']:
                break
            else:
                print("Please select one of the available options.")
                continue
        if user_input == 'q':
            break
        elif user_input.lower() == 'a':
            addInformation()
        elif user_input.lower() == 'r':
            reviewInformation()
        elif user_input.lower() == 'd':
            deleteInformation()
        else:
            die()
