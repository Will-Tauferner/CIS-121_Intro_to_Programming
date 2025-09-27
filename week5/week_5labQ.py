#Written By William Tauferner
#1
'''
def v_of_pyramid(base, height):
    volume = (base**2 * height) /3
    return(v_of_pyramid)
'''
#print(f'The volume of the pyramid is {v_of_pyramid(3,4)}')


#2

#3
# you are counting points for a basketball game. Write a function that calculates the final points for
#the team and returns the value. The arguments for the function will be two pointers (number of
#two-pointers scored) and three pointers (number of three-pointers scored).

def total_points(two_pointers, three_pointers):
    total_points = (two_pointers * 2) + (three_pointers * 3)
    return total_points
print(total_points(2,5))




#4

#5

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

def access_rights(user_role):
    if user_role == 'admin':
        return 'full access'
    elif user_role == 'user':
        return 'limited access'
    elif user_role == 'guest':
        return 'view only access'
''' 
#12 
#In an Ancient Kingdom, the currency consists of bronze coins, silver coins, and gold coins. There are
#20 bronze coins in one silver coin and 15 silver coins in one gold coin. Write a function that will return
#a converted amount of bronze coins into the fewest amount of coins possible. Only return a string with
#the non-zero values, meaning don’t return something similar to “0 silver coins”. The argument for the
#function will be bronze coins (how many bronze coins to convert)
'''
def convert(bronze_coins):
   gold_coins = bronze_coins // 300 
   silver_coins = (bronze_coins % 300) // 20 
   bronze_coins = bronze_coins
   answer = ''
   if gold_coins > 0:
       
   if silver_coins > 0:
       '''
#
      




''''
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


def is_fever(temperature):
#How can we extract the F and C ?
    unit = temperature[-1]
#If it is F > 98.6 is a fever
    if unit == 'F':
        # '99F' -> '99'
        if temperature > 98.6: 
            return True
        else:
            return False
#If it is a C -> 37 is a fever 
    if unit == 'C':
        if temperature > 37:
            return True
        else:
            return False
# Input and print shoyld be outside of the function 
user_input = input('Enter a temperature in F or C ')
print(f'is fever ? {is_fever(user_input)}')
'''

#15 
#Write a function that returns the number of copies of the same number. The arguments for the
#function will be num 1 (first number), num 2 (second number), and num 3 (third number)
#count duplicates(2, 3, 2) →” You entered the same number 2 times”

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