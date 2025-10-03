#Written By William Tauferner
#1

def v_of_pyramid(base, height):
    volume = (base**2 * height) /3
    return(v_of_pyramid)

print(f'The volume of the pyramid is {v_of_pyramid(3,4)}')


#2

#3
# you are counting points for a basketball game. Write a function that calculates the final points for
#the team and returns the value. The arguments for the function will be two pointers (number of
#two-pointers scored) and three pointers (number of three-pointers scored).
'''
def total_points(two_pointers, three_pointers):
    total_points = (two_pointers * 2) + (three_pointers * 3)
    return total_points
print(total_points(2,5))

'''


#4
#You are counting points for a tennis match. Write a function that calculates the total points for a
#player and returns the value. The arguments for the function will be aces (each ace is worth 2 points)
#1
#and winning shots (each winning shot is worth 1 point).
'''
def counting_point(aces,winning_shot):
    counting_point = (aces * 2) + (winning_shot * 1)
    return counting_point
print(counting_point(4,3))
      '''

#5
#Write a function that counts the total number of legs in the farmer’s land and returns the value. The
#arguments for the function will be chickens (number of chickens farmer has), cows (number of cows
#farmer has), and pigs (number of pigs farmer has) 
#Pigs has 4 legs
#Cow has 4 legs
#chicken has 2 legs
'''
def legCounter(chickens,cows,pigs):
    legCounter = (chickens * 2) + (cows * 4) + (pigs * 4)
    return legCounter
print(f'the amount of legs is:{legCounter(1,2,3)}')
'''
#6
#Write a function that counts the total number of batteries needed for the toy store and returns the
#value. The arguments for the function will be e dolls (number of electronic dolls toy store has), rc cars
#(number of remote-controlled cars toy store has), and robo dogs (number of robot dogs toy store has).
'''
def battery_counter(edolls,rcCars,robodogs):
    battery_counter = (edolls * 2) + (rcCars * 4) + (robodogs * 6)
    return battery_counter
print(f'the amount of batterys is:{battery_counter(1,2,3)}')
'''

#7
#The table below show what your resting heart rate should be based on age and athleticism. Write
#a function that returns what the resting heart rate of the user should be. The arguments for the
#function will be age (how old the user is) and athl goal (athletic goal of user)

def resting_heartrate(age,athl_goal):
    if 20 <= age <= 39:
        if athl_goal == "Above Average":
            return('Your heart rate will be 47-72')
        elif athl_goal == "Below Average":
            return('Your heart rate will be 73-93')
    elif 40 <= age <=59:
        if athl_goal == "Above Average":
            return('Your heartrate will be 46-71')
        elif athl_goal == 'Below Average':
            return('your heartrate will be 72-94')
    elif 60 <= age <= 79:
        if athl_goal == "Above Average":
            return('Your heart rate will be 45-70')
        elif athl_goal == 'Below Average':
            return('YOur heart rate will be 71-97')
    return('age not supported')
age = int(input('Please select current age'))
athl_goal = input('Please select what athletic goal you want between Above Average and Below Average')

print(resting_heartrate(age,athl_goal))

'''
#8 
'''
def pool_times(grade, time):
    # Convert K >>> 0)
    pool_time = ''
    if grade == 'k':
        grade = 0
    if (0 < int(grade) <= 3):
        if(time == 'Morning'):
            pool_time = '9 AM'
        else:
            pool_time = '10 PM'
    elif grade == (4 <= int(grade) <= 8):
        if(time == 'Morning'):
            pool_time = '10 AM'
        else:   
            pool_time = '2 PM'
    elif grade == (9 <= int(grade) <= 12):
        if(time == 'Morning'):
            pool_time = '11 AM'
        else:   
            pool_time = '3 PM'
    return
#print(pool_times)
#grades = input('Please pick a grade')
#time = input('Please pick a time between morning or afternoon')
'''
#9
#When driving in a car and approaching a traffic control light, green means go, yellow means yield,
#and red means stop. Write a function that returns the action that should be taken by a driver. The
#argument for the function will be light color (the current color of the traffic control light).
'''
def light_color(current_color):
    if current_color == 'green':
        return 'go'
    elif current_color == 'yellow':
        return 'yield'
    elif current_color == 'red':
        return 'stop'
current_color = input('Please select a color between gree, yellow, and red:')
print(light_color(current_color))

#10 
#When using a security access system, different clearance levels are assigned to users. In our system,
#admin means full access, user means limited access, and guest means view-only access. Write a function
#named access rights that takes user role (a string) as an argument and returns the access rights of a
#user
'''
'''
def access_rights(user_role):
    if user_role == 'admin':
        return 'full access'
    elif user_role == 'user':
        return 'limited access'
    elif user_role == 'guest':
        return 'view only access'
print(access_rights('admin'))
'''
#12 
#In an Ancient Kingdom, the currency consists of bronze coins, silver coins, and gold coins. There are
#20 bronze coins in one silver coin and 15 silver coins in one gold coin. Write a function that will return
#a converted amount of bronze coins into the fewest amount of coins possible. Only return a string with
#the non-zero values, meaning don’t return something similar to “0 silver coins”. The argument for the
#function will be bronze coins (how many bronze coins to convert)
'''
'''
def convert(bronze_coins):
   gold_coins = bronze_coins // 300 
   silver_coins = (bronze_coins % 300) // 20 
   bronze_coins = bronze_coins
   answer = ''
   if gold_coins > 0:

#11
def convert_knuts(knuts):
    
    #Knuts, Sickle, Galleons

    #1 for the number of knuts how many gallesons can I buy?

    galleons = knuts // (29 * 17)
    remaining_knuts = knuts - (galleons * 493)
    #2 Remaining knuts, how many sickles can i buy ?
    sickles = remaining_knuts // 29 
    #3 How many remaining knuts after buying sickles ?
    remaining_knuts = remaining_knuts - (sickles * 29)

    output = ''
    if knuts > 0:
        output += f'knuts {knuts} '
    if sickles > 0:
        output += f'Sickles {sickles}'
    if galleons > 0 :
        output += f'galleons {galleons} '
    
    
    return output

print(convert_knuts(32))
'''

#14 
'''
from random import randint 

def random_guess(user_guess):
    
    value = randint(0,9)
    output = f'{value} You guessed : {user_guess} '
    if value % 2 == 0 and user_guess == 'even':
        output += "Correct"
    elif value % 2 == 1 and user_guess == 'odd':
        output += "Correct"
    else: 
        output += "Incorrect"
    return output
print(random_guess('even'))

'''
def is_fever(temperature):
    unit = temperature[-1]
    if unit == 'F':
        if temperature > 98.6: 
            return True
        else:
            return False 
    if unit == 'C':
        if temperature > 37:
            return True
        else:
            return False 
user_input = input('Enter a temperature in F or C ')
print(f'is fever ? {is_fever(user_input)}')
'''

#15 
#Write a function that returns the number of copies of the same number. The arguments for the
#function will be num 1 (first number), num 2 (second number), and num 3 (third number)
#count duplicates(2, 3, 2) →” You entered the same number 2 times”
'''
def count_duplicates(num1, num2, num3):
    if num1 == num2 and num1 == num3:
        output = 3
    elif num1 == num2:
        output = 2
    elif num1 != num2 and num1 == num3:
        output = 2
    elif num2 == num3: 
        output = 2
    else:
        output = 1
    return f'You entered the same number{output}times' 

print(count_duplicates(1,2,1))
'''
#17
#Write a function that checks whether a letter is a vowel or consonant. The function should return
#” Vowel” if the letter is a vowel and” Consonant” if the letter is a consonant. The argument to the
#function will be letter (a single lowercase letter).
#Hint: In the English language, the letters a, e, i, o, and u are the vowels
'''
def checkletter(letter):
    if letter in ('a','e','i','o','u'):
        return'vowel'
    else:
        return'constant'
print(checkletter('z'))

#18
#at the local ice cream store they have 3 flavors, which are Vanilla, Chocolate, and Strawberry. Write
#a function that returns the selected flavor. If the chosen flavor is not available, let them know. The
#argument to the function will be selected f lavor (the user’s selected flavor).

def flavor(sel_flavor):
    if sel_flavor == 'vanilla':
        return 'Here is your vanilla icecream!'
    elif sel_flavor == 'chocolate':
        return 'Here is your chocolate icecream!'
    elif sel_flavor == 'strawberry':
        return 'Here is your strawberry icecream!'

sel_flavor = input('Please pick a flavor:vanilla, chocolate, strawberry')
print(flavor(sel_flavor))


#19

#STRINGS QUESTIONS
#1
#Zyra the code mage has hidden a mysterious cipher in reversed messages. You must help Zyra uncover
#the secrets of the digital realm. Create a function called reverse string that takes the variable word
#(a string) and returns the word in reversed order

def reverse_string(word):
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word

# Example usage
message = "sdrawkcab"
print(reverse_string(message))  # Output: "backwards"

#4
#Your task: create a function named hamming distance that takes two strings as arguments, and returns
#the hamming distance between the two strings
def hamming_distance(str1, str2):
    # Assume both strings are the same length
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    return distance

# Examples
print(hamming_distance("abcde", "bcdef"))   # → 5
print(hamming_distance("abcdef", "abcdef")) # → 0
print(hamming_distance("strong", "strung")) # → 1

#5
def is_isogram(word):
    for i in range(len(word)):
        for j in range(i + 1, len(word)):
            if word[i] == word[j]:
                return False   # found a duplicate
    return True  # no duplicates found

# Examples
print(is_isogram("lamp"))     # → True
print(is_isogram("letter"))   # → False
print(is_isogram("strong"))   # → True

#6

#9
def flip_flop(word):
    mid = len(word) // 2            # find the midpoint
    first_half = word[:mid]         # from start to middle
    second_half = word[mid:]        # from middle to end
    return second_half + first_half # flip-flop

# Examples
print(flip_flop("python"))   # → honpyt
print(flip_flop("banana"))   # → nana ba → nanaba
print(flip_flop("magic"))    # → icmag




