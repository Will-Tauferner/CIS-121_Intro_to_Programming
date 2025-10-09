#4
#Write a function that takes a dictionary called names of tech ids and student names as key-value
#pairs, and returns a list containing just the student names
'''
def get_names(my_dict):
    names = []

    for key in my_dict:
        print('keys :' + key)
        print('value :' + my_dict[key])
    name = my_dict[key]

    names.append(name)
    return names

names_dict = {'12345': 'Will', '56473': ''}
print(get_names(names_dict))
'''
#5
#Write a function that takes a dictionary, called people, containing the names and ages of a group of
#people, and returns the name of the oldest person
'''
def people(names_dict):
    oldest_name = ''
    max_age = -1
    for name in names_dict:
        age = names_dict[name]
        if age >= max_age:
            max_age = age 
            oldest_name = name
    return oldest_name
names_dict = {'Matt': 10, 'Matthew,': 11, 'Evan' : 12}
print(people(names_dict))

#6
#Write a function that takes a string word and returns a dictionary containing the count of each letter
#in the word

def string_word(dict):
    count_dict = {}
    for letter in count_dict():
        count_dict[letter] += 1
    else:
        count_dict[letter] += 1
    return count_dict

print(letter_count('missisippi'))
            
#my own question
def flip_flop(word):
    mid = (len(word // 2))
    first_half = word[:mid]
    second_half = word[mid:]
    return(second_half + first_half)
print(flip_flop('abcd'))
'''
def highway_directions(highwayNum):
    if 0 <= int(highwayNum) <= 99:
        if highwayNum // 2 == 0:
            return 'East/West'
        elif highwayNum // 2 == 1:
            return 'North/South'
    if 200 == int(highwayNum):
        return 'invalid highway number'
    if 100 <= int(highwayNum) <= 999:
        if highwayNum // 2 == 0:
            return 'East/West'
        elif highwayNum // 2 == 1:
            return 'North/South'
print(highway_directions(5))



