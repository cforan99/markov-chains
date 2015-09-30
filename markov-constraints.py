import sys
from random import choice

filename = sys.argv[1]  

def open_and_read_file(filename):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_string = open(filename).read()

    return file_string


def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    
    all_words = text_string.split()

    for i in range(len(all_words)-3):
        first_word = all_words[i]
        second_word = all_words[i+1]
        following_word = all_words[i+2]

        if chains.get((first_word, second_word)) is None:
            chains[(first_word, second_word)] = [following_word]
        else:
            chains[(first_word, second_word)].append(following_word)
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = []

    #randomly choose a key from chains
    keys_list = chains.keys()
    capital_keys = [key for key in keys_list if key[0].istitle()]
    new_key = choice(capital_keys)

    text.extend([new_key[0], new_key[1]])

    while new_key in chains:
        next_word = choice(chains[new_key])
        text.append(next_word)
        new_key = (new_key[1], next_word)

    random_text = " ".join(text)
        
    return random_text


#input_path = "black.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(filename)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
