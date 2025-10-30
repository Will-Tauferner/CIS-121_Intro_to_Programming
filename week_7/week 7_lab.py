'''
#1
#An isogram is a word that has no duplicate letters. Write a function that takes a string word and
#returns either True or False depending on whether or not it’s an isogram.
def is_isogram(word):
    letter_counts = {}
    for letter in word:  # go through each character exactly as given
        if letter in letter_counts:  # if we’ve seen it before
            return False
        letter_counts[letter] = 1   # mark as seen
    return True
print(is_isogram('machine'))

#2
#In each input list, every number repeats at least once, except for one. Write a function that takes an
#array numbers and returns the single unique number.

def unique_num(my_array):
    my_dict = {}
    for num in my_array:
        print(my_dict)
        if num in my_dict:
            my_dict[num] += 1
        else:
            my_dict[num] = 1
    for key in my_dict:
        if my_dict[key] == 1:
            return key
print(unique_num([1,1,2,2,3,3,4]))


#3
#In each input list, every number repeats at least once, except for two. Write a function that takes an
#array numbers and returns the two unique numbers

def two_unique_numbers(numbers):
    count = {}  # Dictionary to count occurrences

    for num in numbers:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # Collect numbers that appear only once
    result = []
    for num in count:
        if count[num] == 1:
            result.append(num)

    return result



#4
#Write a function that takes a dictionary called names of tech ids and student names as key-value
#pairs, and returns a list containing just the student names
'''
'''
def get_names(my_dict):
    names = []

    for key in my_dict:
        print('key:', key)
        print('value:', my_dict[key])
        names.append(my_dict[key]) 

    return names
names_dict = {'12345': 'Will', '56473': ''}
print(get_names(names_dict))
'''
def get_names(student_techid_name_dict):
    names = []
    for techid in student_techid_name_dict:
        print('value',student_techid_name_dict[techid])
        names.append(student_techid_name_dict[techid])
    return names

my_dict = {'12434': 'Will', '56437': 'Steve'}

#5
#Write a function that takes a dictionary, called people, containing the names and ages of a group of
#people, and returns the name of the oldest person

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
def string_word(word):
    count_dict = {}
    for letter in word: 
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    return count_dict

print(string_word('mississippi'))



#7
#Write a function that takes a dictionary, called exams, containing the course grades of a student, and
#returns the name of the course with the minimal grade

def lowest_grade_course():
    exams = { 'Math': 85, 'Physics': 78,'Chemistry': 92,'History': 80 }
    lowest_course = None
    lowest_grade = None
    for course, grade in exams.items():
        if lowest_grade is None or grade < lowest_grade:
            lowest_grade = grade
            lowest_course = course
    return lowest_course
print(lowest_grade_course)

#8
#Write a function that takes a dictionary, called people, containing the names and ages of a group of
#people, and returns the name of the youngest person

def youngest_person(people):
    people = {'Matthew': 60, 'Mark' : 24, 'Anna': 26}
    youngest_name = None
    youngest_age = None
    for name, age in people.items():
        if youngest_age is None or age < youngest_age:
            youngest_age = age
            youngest_name = name
    return youngest_name
print(youngest_person(people))

#9
#Below is a receipt from my recent lunch order.
#(a) Initialize an empty dictionary named receipt, and then add the contents of the receipt as key-value
#pairs.
#(b) Using the dictionary you created in part a, write code that prints the total cost of all the items
#on the receipt. The code should work regardless of the contents of the receipt. (meaning don’t
#write print(6+12+3))

receipt = {}
receipt['Side Salad'] = 6
receipt['Chicken Parm'] = 12
receipt['Cookie'] = 3

total = 0
for price in receipt.values():
    total += price
print("Total cost:", total)

#10
#Below is the menu from my favorite restaurant.
#(a) Initialize an empty dictionary named menu, and then add the contents of the menu as key-value
#pairs.
#(b) Using the dictionary you created in part a, write code that prints each of the items on the menu
#as key-value pairs. The code should work regardless of the contents of the receipt. (meaning don’t
#write print

menu = {}
menu['burger'] = 10
menu['fries'] = 4
menu['soda'] = 3

for item, price in menu.items():
    print(item, "cost", price)

#11
#Write a function that takes a list, called elements, and returns a dictionary detailing how many times
#each element is repeated.

def count_elements(elements):
    element_counts = {}
    for item in elements:
        if item in element_counts:
            element_counts[item] += 1
        else:
            element_counts[item] = 1
    return element_counts
elements = ['cat', 'dog', 'cat', 'bird', 'dog', 'cat']
print(count_elements(elements))

#12
#Write a function that takes a dictionary, called store, representing items and their prices, and an
#integer, called wallet, representing the amount of money you have. The function should return a list
#of items you can afford. If you cannot afford anything, return an empty list.

def affordable_items(store, wallet):
    can_afford = []
    for item, price in store.items():
        if price <= wallet:
            can_afford.append(item)
    return can_afford
store = {
    "burger": 10,
    "fries": 4,
    "soda": 3,
    "steak": 25
}
wallet = 8
print(affordable_items(store, wallet))

#13
#Write a function that takes a dictionary, called sales, where the keys are product names and the
#values are the number of units sold. The function should return the total number of products sold

def total_units_sold(sales):
    total = 0
    for units in sales.values():
        total += units
    return total
sales = {
    "apples": 30,
    "bananas": 45,
    "oranges": 25
}

print(total_units_sold(sales))

x = 3
y = 7

# Your code here
temp = x
x = y
y = temp

print("x =", x)
print("y =", y)

temp = x
x = y
y = temp
print('x =',x)
print('y =',y)
# Ask for user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Output a greeting
print("Hello, " + first_name + " " + last_name + "! Welcome!")


# Ask for user input
color = input("Enter your favorite color: ")
animal = input("Enter your favorite animal: ")

# Output their pick using an f-string
print(f"Your favorite combination is a {color} {animal}!")





