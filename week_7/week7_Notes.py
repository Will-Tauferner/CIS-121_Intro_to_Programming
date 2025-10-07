def letter_counter(word):
    letter_dictionary = {}
    for letter in word:
        if letter in letter_dictionary:
            letter_dictionary[letter] = letter_dictionary[letter] + 1
            #add in key value pair. What are key and value?
        else: #key is NOT in dictionary.
            letter_dictionary[letter] = 1

    return letter_dictionary

my_word = 'peter piper picked a peck of pickled pepprs'
letter_dict = letter_counter(my_word)

for letter in letter_dict:
    print(letter, letter_dict[letter])

#result...
#d = {'p:9,'e':???}