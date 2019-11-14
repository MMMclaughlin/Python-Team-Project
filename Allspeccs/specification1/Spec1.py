import matplotlib.pyplot as plt
import os
# opens text.txt with the utf-8 encoding so that it can deal with the weird encoding of the text file
def Spec1(filelocation):
    print(os.path.realpath(__file__))
    if filelocation:
        streamreader = open((filelocation), "r", encoding="utf-8")
    else:
        print("please give a text files location")
    characters = {}
    dictionary = {}
    amount_of_values = 0
    word = ""
    file = ""
    for line in streamreader:
        for character in line:
            # sets all characters to lower case so they can be analysed and so that a word with a capital letter isn't
            # counted separately to the same word without the capital letter
            character.lower()
            # checks the character being looked at is a letter
            if ord(character) > 96 and ord(character) < 123:
                # if the character being looked at is already in the characters list
                if character in characters:
                    # increments the count of the relevant character
                    characters[character] = str(int(characters[character]) + 1)
                else:
                    # creates a new instance in the characters dictionary and sets the value to 1
                    characters[character] = "1"
            # if the character being looked at is the end of a word
            if character in [" ", ".", "!", "?", ":", ";"]:
                # makes sure that the word variable isnt empty
                if not word == "":
                    # compares the new word to the dictionary of all recorded words
                    if word in dictionary:
                        # creates a copy of the amount of instances of that word as a dictionary value cant be converted to
                        # type int so i would otherwise be unable to increment the value
                        current_count = dictionary[word]
                        # increments the value associated to the word
                        dictionary[word] = str(int(current_count) + 1)
                        # go through the entire file
                    else:
                        # creates the new key value pair in the dictionary
                        dictionary[word] = "1"
                        # adds the new key value pair to the file and creates a new line
                        file += word + ", 1 \n"
                    word = ""
                    amount_of_values += 1
            elif character == "\n":
                word = word
            else:
                word += character
    # closes the streamreader as only so many can be handled by the OS at once
    streamreader.close()
    # writes the file string into the text file csv using the utf-8 encoding otherwise the strange characters found in the
    # file cause the program to crash
    streamwriter = open("csv.csv", "w", encoding="utf-8")
    streamwriter.write(dictionary.__str__())
    streamwriter.close()
    character_total = 0
    other_total = 0
    characters_to_remove = []
    # for every character found
    for i in characters:
        # adds the amount of that character that was found to the total count of characters found
        character_total += int(characters[i])
    # for every character found
    for i in characters:
        # makes sure that the amount of characters is a reasonable size as otherwise the pie chart looks awful
        if int(characters[i]) < character_total / 500:
            # if the character count is too small adds the character to a list of characters to be removed outside the loop
            # as loops dont like the thing they are looping off changing size within the loop
            characters_to_remove.append(i)
    # removes every character that was set to be removed from the dictionary characters
    for i in characters_to_remove:
        characters.pop(i)
    # creates a pie chart
    figure = plt.subplot()
    # plots all of the values into the pie function
    plt.pie(characters.values(), labels=characters.keys(), autopct='%1.1f%%', shadow=False, startangle=90)
    # makes sure that the pie chart is drawn as a circle
    figure.axis('equal')
    # shows the pie chart
    plt.show()
    streamwriter = open("analysis.md", "w", encoding="utf-8")
    streamwriter.write("Here is the analysis of the words found in the inputted file")
    # for every line in the csv file
    streamwriter.write(dictionary.__str__())
    streamwriter.write("\n \n \n  this is the analysis of the characters found in the inputted file\n \n")
    # writes a string representation of the characters dictionary
    streamwriter.write(characters.__str__())
