x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

#print(x[1:4])
#for i in range(0,5):
#    print(x[i])

#print(x)
#x.append('Saturday')
#x.append('Sunday')
#print(x)
#x = 'Wednesday'
#print(x[3:6])
#print(x[4])
#x[4] = 'Funday'

#print(x)



#x = 'apple'
#y = x
#print(x)
#print(y)

#x = 'banana'
#print(x)
#print(y)

#mutable object 
#workDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
#y = x   

#print(x)
#print(y)
#print(workDays)
#workDays[4] = 'Funday'
#print(workDays)

#immutable object
#workDays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
#print(workDays)

#write a function that takes a string as an argument, and returns a list containing 
#all of the words in that string.


word = 'Peter piper picked a peck of pickled peppers'
result = ['Peter', 'piper','picked', 'a' 'peck', 'of' , 'pickled', 'peppers.']

def string_to_list(words):
    words = []
    #collect a word
    built_word = ''
    for letter in word:
        if letter == ' ':
            #add built word into the list
            words.append(built_word)
            built_word = ''
        else:
            built_word += letter
           

    #once we have a full word, let's add it to the list of words.


    return words
print(string_to_list(word))


    










