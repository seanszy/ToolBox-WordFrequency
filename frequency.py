""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    #Opens and reads the file that is saved in the folder
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    #The while loop below searches through the book until it finds the string and then starts analyzing the book from there
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        #it ends the loop and changes the loop to start from there forward
        curr_line += 1
        lines = lines[curr_line+1:]
        words = ""
        for items in lines:
            #makes a string of all the words and converts them to lower case
            words = words + items.lower()
        words = words.split()
    return words


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    #initializes a dictionary to store all the words in and some other lists
    word_dictionary = dict()
    most_frequent = []
    word_list2 = []
    #goes through the word list and puts all items in the dictionary under the key
    #that corresponds to the number of times it occurs
    for word in word_list:
        word_occurances = word_dictionary.get(word, 0)
        word_dictionary[word] = word_occurances + 1
    #converts the dictionary to a list of tuples iwth the key and value
    for key in word_dictionary:
        word_list2 .append((word_dictionary[key], key))
    #sort the list from highest to lowest
    word_list2.sort(reverse = True)
    #take the top 25 highest occuring and put them in a list
    for top_25 in range(n-1):
        current_item = word_list2[top_25]
        most_frequent.append(current_item[1])
        #print (current_item[1] + ":" + str(current_item[0]))
    print(most_frequent)
    #return the most requently occuring words
    return most_frequent


if __name__ == "__main__":
    #calls the first function and uses its output to call the second
    word_list = get_word_list("pg32325.txt")
    get_top_n_words(word_list, 25)
