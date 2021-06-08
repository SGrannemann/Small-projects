"""Simple Address Book that only the command line. Single module. Writes and reads to a csv file.
"""
import csv
import re
import datetime
from pathlib import Path
import pyinputplus as pyip



def gather_input():
    """Gathers input for creation of new entry. returns dict with data.

    Uses RegEx patterns to distinguish street and housenumber as well as zip code and city name.


    :returns: The data, including name, surname, birthday, street, housenumber, zipcode, city name
    :rtype: dictionary
    """
    data = {}
    name = pyip.inputStr(PHRASE.format(' first name'),
                            blockRegexes=[(r'\d+',
                                        "Names should contain only letters.")])
    data['Name'] = name

    surname = pyip.inputStr(PHRASE.format('surname'),
                            blockRegexes=[(r'\d+',
                                            "Names should contain only letters.")])
    data['Surname'] = surname

    birthday = pyip.inputDate(PHRASE.format('Birthday') + 'Blank to skip.',
                                blank=True)

    if isinstance(birthday, datetime.date):
        data['Birthday'] = str(birthday.day) + '.' + str(birthday.month) + '.' + str(birthday.year)
    else:
        data['Birthday'] = 'Empty'

    street = pyip.inputRegex(STREET_REGEX,
                                prompt=PHRASE.format('street and housenumber'))
    data['Street'], data['Housenumber'] = partition_street(street, STREET_REGEX)

    city = pyip.inputRegex(CITY_REGEX, prompt=PHRASE.format('zipcode and city'))
    data['Zipcode'], data['City'] = partition_city(city, CITY_REGEX)

    return data


def check_duplicates(list_of_entries, name, surname):
    """Checks if an entry is already present in the saved file or the memory. Returns boolean.

    :param list_of_entries: A list of dicts that have already been entered in the session.
    :type list_of_entries: list
    :param name: the name of the person for which the existence of an entry should be checked
    :type name: str
    :param surname: the surname of the person for which the existence of an entry should be checked
    :type surname: str
    :returns: a Boolean (true if duplicate is found)
    :rtype: bool
    """
    aux_list = [name, surname]
    if path.is_file():
        try:
            file = open("AddressBook.csv", "r", newline='')
            filereader = csv.DictReader(file)
        except IOError:
            print('File not found.')
        for row in filereader:
            if all(any(entered == value.lower() for value in list(row.values())) for entered in aux_list):
                file.close()
                return True
        file.close()
    else:
        for dictionary in list_of_entries:
            if all(any(entered == value.lower() for value in list(dictionary.values())) for entered in aux_list):
                return True
    return False

def create_entry():
    """Gathers input, checks for duplicates and then creates an entry. Returns None.
    """
    # collect all dicts created in a list
    list_of_entries = []
    while True:
        # create a new dict
        data = gather_input()
        # check if an entry for the name and surname exists. if yes, get rid of the new one.
        if check_duplicates(list_of_entries, data['Name'].lower(), data['Surname'].lower()):
            print('An entry for this person already exists.')
            data.clear()
        else:
            list_of_entries.append(data.copy())

        input_for_break = pyip.inputMenu(['Enter new entry', 'Save and quit'],
                               numbered=True)
        if input_for_break == 'Enter new entry':
            continue
        if input_for_break == 'Save and quit':
            break
    # if there is data that was not a duplicate, append it to the file (or create a new file.)
    if list_of_entries:

        fieldnames = list(list_of_entries[0].keys())
        if not path.is_file():

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


def partition_street(street, regex_string):
    """Checks if string is valid combination of street and housenumber.
    Returns tuple of strings: 1 is the street, 2 the housenumber.

    :param street: String that should be checked.
    :type street: str
    :param regex_string: RegEx pattern for street/housenumber.
    :type regex_string: str
    :returns: a string for the street and a string for the housenumber
    :rtype: tuple of strings
    """
    street_regex_object = re.compile(regex_string)
    match_object = street_regex_object.search(street)
    # group 1 is name of the street, group 2 is the housenumber
    return match_object.group(1), match_object.group(2)


def partition_city(city, regex_string):
    """Checks if string is valid combination of ZIP code and city name.
    Returns tuple of strings: 1 is the ZIP, 2 the city name.

    :param street: String that should be checked.
    :type street: str
    :param regex_string: RegEx pattern for zip/city.
    :type regex_string: str
    :returns: a string for the ZIP code and a string for the city name.
    :rtype: tuple of strings
    """
    city_regex_object = re.compile(regex_string)
    match_object = city_regex_object.search(city)
    # group 1 is the zip code, group 2 is the city name
    return (match_object.group(1), match_object.group(2))


def review_information():
    """Lets the user decide between all content, single entry and all entries matching a condition.
    """
    try:
        file = open("AddressBook.csv", "r", newline='')
    except IOError:
        print("File not found.")
    filereader = csv.DictReader(file) # fieldnames=fieldnames)


    entry = pyip.inputMenu(['show all content', 'show a single entry',
                           'show all entries that match a condition'],
                           numbered=True)
    if entry == 'show all content':
        for row in filereader:
            print(row)
    if entry == 'show a single entry':
        single_entry(filereader)
    if entry == 'show all entries that match a condition':
        filter_entries(filereader)
    file.close()


def single_entry(filereader, updating=False):
    """Prints or returns an entry. Use updating flag to switch between printing and returning.

    :param filereader: a filereader object from which an entry should be printed or returned.
    :type filereader: filereader object
    :param updating: flag that switches between returning and print. Default = False = printing.
    :type updating: bool
    :returns: entry that matches with the name and surname asked for.
    :rtype: dict
    """
    name = pyip.inputStr(PHRASE.format('first name'),
                         blockRegexes=[(r'\d+',
                                        "Names should contain only letters.")])
    surname = pyip.inputStr(PHRASE.format('surname'),
                            blockRegexes=[(r'\d+',
                                          "Names should contain only letters.")])
    list1 = [name.lower(), surname.lower()]
    count = 0
    for row in filereader:

        if all(any(entered == value.lower() for value in list(row.values())) for entered in list1):
            print('found entry.')
            if not updating:
                print(row)
                count += 1
            if updating:
                count += 1
                return row
    if count == 0:
        print("Entry not found.")


def filter_entries(filereader):
    """Prints only those entries that match a condition. Returns None.

    :param filereader: the file reader object to be searched for entries that match the condition.
    :type filereader: filereader object.
    """
    user_input = input('Enter a name, surname, street or city for which you want to display all matching entries.\n')
    count = 0
    for row in filereader:
        if any(user_input.lower() in value.lower() for value in list(row.values())):
            print(row)
            count += 1
        if count == 0:
            print("No matching entry found.")


def delete_information():
    """Lets the user select if all content or a single entry shall be deleted. Returns None.
    Either deletes the complete file or asks for input to identify the entry to be deleted.
    """
    entry = pyip.inputMenu(['delete all content', 'delete a single entry',
                           ],
                           numbered=True)

    if entry == 'delete all content':
        try:
            file = open('AddressBook.csv', 'w', newline='')
        except IOError:
            print('File not accessible.')
        file.close()

    if entry == 'delete a single entry':
        list_of_entries = []
        try:
            file = open("AddressBook.csv", "r", newline='')
        except IOError:
            print('File not accessible.')
        filereader = csv.DictReader(file)
        for row in filereader:
            list_of_entries.append(row)
        file.close()
        name = pyip.inputStr(PHRASE.format('first name'),
                         blockRegexes=[(r'\d+',
                                        "Names should contain only letters.")])
        surname = pyip.inputStr(PHRASE.format('surname'),
                            blockRegexes=[(r'\d+',
                                          "Names should contain only letters.")])
        delete_entry(list_of_entries, name, surname)

def delete_entry(list_of_entries, name, surname):
    """Deletes a single entry from AddressBook.csv. Returns None.

    :param list_of_entries: a list of dicts that have been read in from the .csv file.
    :type list_of_entries: list
    :param name: name for the entry to be deleted.
    :type name: str
    :param surname: surname for the entry to be deleted.
    :type surname: str
    """
    fieldnames = list(list_of_entries[0].keys())
    list1 = [name.lower(), surname.lower()]
    for dictionary in list_of_entries:
        if all(any(entered == value.lower() for value in list(dictionary.values())) for entered in list1):
            list_of_entries.remove(dictionary)
    try:
        file = open("AddressBook.csv", "w+", newline='')
    except IOError:
        print('Writing to file not possible.')

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for entry in list_of_entries:
        writer.writerow(entry)
    file.close()

def update_information():
    """Lets user select an entry to update and than supply the new data.
    """
    list_of_entries = []
    try:
        file = open("AddressBook.csv", "r", newline='')
    except IOError:
        print("File not found.")
    filereader = csv.DictReader(file)
    for row in filereader:
        list_of_entries.append(row)
    print(list_of_entries)
    file.close()

    file = open("AddressBook.csv", "r", newline='')
    filereader = csv.DictReader(file)
    print('Which entry do you want to update?')
    data = single_entry(filereader, updating=True)
    file.close()

    delete_entry(list_of_entries, data['Name'], data['Surname'])

    print('Update the information as required:')
    name = pyip.inputStr(PHRASE.format(' first name')+ 'Blank to skip.',
                             blockRegexes=[(r'\d+',
                                            "Names should contain only letters.")],
                                  blank=True)
    if name != '':
        data['Name'] = name

    surname = pyip.inputStr(PHRASE.format('surname')+ 'Blank to skip.',
                                blockRegexes=[(r'\d+',
                                              "Names should contain only letters.")],
                                  blank=True)
    if surname != '':
        data['Surname'] = surname

    birthday = pyip.inputDate(PHRASE.format('Birthday') + 'Blank to skip.',
                                  blank=True)

    if isinstance(birthday, datetime.date):
        data['Birthday'] = str(birthday.day) + '.' + str(birthday.month) + '.' + str(birthday.year)
    else:
        data['Birthday'] = 'Empty'

    street = pyip.inputRegex(STREET_REGEX,
                                 prompt=PHRASE.format('street and housenumber')+ 'Blank to skip.',
                                  blank=True)
    if street != '':
        data['Street'], data['Housenumber'] = partition_street(street, STREET_REGEX)

        city = pyip.inputRegex(CITY_REGEX, prompt=PHRASE.format('zipcode and city')+ 'Blank to skip.',
                                  blank=True)
        if city != '':
            data['Zipcode'], data['City'] = partition_city(city, CITY_REGEX)

    try:
        file = open("AddressBook.csv", "a+", newline='')
    except IOError:
        print('Writing to file not possible.')

    fieldnames = list(data.keys())
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writerow(data)
    file.close()


path = Path.cwd()/'AddressBook.csv'
PHRASE = 'Please provide the {}. \n'
STREET_REGEX = r'([a-zA-Z-\s]+)\s(\d{1,3})$'
CITY_REGEX = r'^(\d{5})\s([a-zA-Z-\s]+)'

###############################################################################
if __name__ == "__main__":

    print("Hello and welcome to the address book. ")

    user_main_input = pyip.inputMenu(['create an entry', 'read existing information',
                                'update information', 'delete information',
                                 'quit'], numbered=True)
    if user_main_input == 'quit':
        print('Quitting program...')
        exit(0)
    elif user_main_input == 'create an entry':
        create_entry()
    elif user_main_input == 'read existing information':
        review_information()
    elif user_main_input == 'update information':
        update_information()
    elif user_main_input == 'delete information':
        delete_information()
