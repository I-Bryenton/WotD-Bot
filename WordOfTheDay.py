from numpy import random
import datetime
import sys
import os


def getWordOfTheDay():
    # Tries to open the file and creates an empty one if it doesn't exist
    try:
        date_file = open("Word of the Day.txt")
    except FileExistsError:
        date_file = open("Word of the Day.txt", 'x')

    date_and_wotd = []
    date = datetime.datetime.now()
    day = date.strftime("%w")

    # Checks if the file is empty. If it isn't then it checks to see if the day matches the one in the .txt file
    if os.stat("Word of the Day.txt").st_size != 0:
        for line in date_file:
            date_and_wotd.append(line)

        if day == date_and_wotd[0].strip():
            return date_and_wotd[1]  # Prints out the wotd since the wotd has been updated for this day
        else:
            date_file.close()  # Since the day didn't match the day in the file,the file will close and be updated later

    entries = []  # Holds the words and their definitions
    used_entries = []  # Used to check if a word has been used before cycling through all words
    word_file = open("Words.txt")
    used_words = open("Used Words.txt")

    for line in used_words:
        x = line.split()
        used_entries.append(x)

    used_words.close()

    for line in word_file:
        word_and_definition = line.split(' - ')

        for word in word_and_definition:
            entries.append(word)

    word_file.close()

    x = True
    length = len(entries) - 1
    num_wotd = random.randint(length)
    wotd = ""
    definition = ""

    while x:
        # If the randomly generated number for the wotd matches one in the file, then generate a new number
        if str(num_wotd) == used_words:
            num_wotd = random.randint(length)
        # Else, check if the randint is an even/odd number; odd is definition, even is word
        else:
            if num_wotd % 2 == 1:
                definition = entries[num_wotd]
                num_wotd -= 1
                wotd = entries[num_wotd]
            else:
                wotd = entries[num_wotd]
                num_wotd += 1
                definition = entries[num_wotd]

            x = False

    wotd = wotd + " - " + definition

    # Updates the .txt file for today so that the other files won't need to be opened and sorted
    # through in the case of the program being run again
    date_file = open("Word of the Day.txt", 'w')
    date_file.write(day)
    date_file.write("\n")
    date_file.write(wotd)

    return wotd
