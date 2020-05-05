#!/usr/bin/env python3

# TODO: implement an commandline argument for the word list file.
# TODO: build a scraper to expand the word list


import os
import random
import sys


def die():
    """Function used for debugging purposes.


    Call it in all conditional branches that should never be evaluated.
    Prints to the command line and makes a clean exit."""
    print("this should not be evaluated.")
    exit(0)


def maskWord(word, list_guessed_letters):
    """Function that creates a string where letters are replaced by a '*'.

    Input: a string, list of letters (a list of strings)
    Return: word/string with replacement.

    Whitespaces are not replaced.
    Letters that have already been guessed correctly will not be replaced.
    The string is printed out."""

    for char in word:
        if char in list_guessed_letters or char == ' ':
            continue
        elif char != ' ' and char not in list_guessed_letters:
            word = word.replace(char, '*')
        else:
            die()
    print('-' * 30)
    print("The word you are trying to guess is: \n")
    print(word)
    print('-' * 30)
    return word


def selectWord(filename):
    """Opens a file, reads it line by line and randomly selects a word.

    Input: filename
    Returns: randomly selected word"""
    # get file path
    abs_path = os.path.abspath(filename)
    # create file object
    word_file = open(abs_path, 'r')
    # make a list of words where each line of the file is one element
    list_of_words = word_file.read().splitlines()
    # randomly select word
    word_to_guess = random.choice(list_of_words)
    return word_to_guess


def gameOver():
    """Prints a game over message.
    """

    print("You used all your guesses!")
    print("Game Over!\n")


def playAgain():
    """Asks the player if he wants to play again.

    If yes, restarts the script, if no makes a clean exit."""

    print("Do you want to play again?")
    string_to_display = 'Press N to quit or any other button to play again.'
    choice = input(string_to_display).lower()
    if choice == 'n':
        print("Goodbye and thank you for playing!")
        exit(0)
    else:  # restart the script
        print("That was a good choice. Restarting...")
        os.execv(sys.executable, ['python'] + sys.argv)


def directSolve(word):

    print("Do you want to solve?")
    input_direct_solve = input("Press S to solve.").lower()
    if input_direct_solve == 's':
        solved_word = input('What is your solution?')
        if solved_word == word:
            winner()
        else:
            print("That was not correct.")


def winner():
    """Prints a 'you won' message and exits.
    """
    print('*' * 30)
    print("Congratulations. You won!")
    print('*' * 30)
    exit(0)


def letterGuessing(guessed_letters):
    while True:
        print("You have already guessed the following letters:\n")
        print(guessed_letters)
        guessed_letter = input("What letter do you choose?")
        if guessed_letter.isalpha() and len(guessed_letter) == 1:
            if guessed_letter in guessed_letters:
                print("You already tried that letter!")
                continue
            else:
                guessed_letters.append(guessed_letter)
                break
        else:
            print("Please enter a single letter.")
            continue

    return guessed_letter

###############################################################################
# set the number of guesses in global variable


script, filename = sys.argv

number_of_guesses = 10
# initialize list to collect all correct guesses
already_guessed_letters = []

# generate word
word_to_guess = selectWord(filename)

# mask the word
masked_word = maskWord(word_to_guess, already_guessed_letters)

i = 0
while True:
    # check if game Over
    if i == number_of_guesses:
        gameOver()
        playAgain()

    # ask the player whether he wants to solve
    if i > 0.5 * number_of_guesses:
        directSolve(word_to_guess)

    # let the player guess a letter
    guessed_letter = letterGuessing(already_guessed_letters)

    if guessed_letter in word_to_guess:
        print("Correct guess!\n")
        masked_word = maskWord(word_to_guess, already_guessed_letters)

    else:
        print("Wrong guess!")

    if '*' not in masked_word:
        winner()

    i += 1

    print(str(number_of_guesses - i) + " tries remaining.")
