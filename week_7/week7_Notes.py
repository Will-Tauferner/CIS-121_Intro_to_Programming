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



#a function is a data type with 2 operators.
#1. assignment = 
#2. invoking ()
#In python all names defined in a program are organized into namespaces.
#These are the names avaiable when the program is executed.
#By default, python loads (_ _builtin_ _) and _ _ main _ _ .
#When a function is invoked, Python creates a local namespace corresponding to the function itself



def add_three(x):
    y = x + 3
    return y

var0 = 7
var1 = add_three(var0)

print(add_three)






