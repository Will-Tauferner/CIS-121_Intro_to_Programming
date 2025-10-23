#1
#Write a function that lets the user guess whether the flip of a coin results in
#heads or tails. The function randomly generates an integer 0 or 1, which represents head or tail. The
#function returns if the guess is correct or incorrect. The argument for the function will be guess (the
#guess of the user, 0 for heads and 1 for tails), if no argument is provided then the default should be
#0 for heads.
#Hint: Use the following lines of code to create the function.
#from random import randint
#value = randint(0,1) #picks a random integer. Either 0 or 1

from random import randint

def toss_coin(guess=0):
    value = randint(0, 1)  # 0 = heads, 1 = tails
    if guess == value:
        return "Correct!"
    else:
        return "Incorrect!"
print(toss_coin())

#2
#Write a function that lets the user guess whether a randomly generated number
#is odd or even. The function randomly generates an integer between 0 and 9 (inclusive) and returns
#whether the user’s guess is correct or incorrect. The argument for the function will be guess (the user’s
#guess, either” odd” or” even”), if no argument is provided then the default guess should be even.
#Hint: Use the following lines of code to create the function.
#from random import randint
#value = randint(0,9) #picks a random integer between 0-9 inclusive

from random import randint

def guess(guess="even"):
    value = randint(0, 9)  # random number between 0–9

    if (value % 2 == 0 and guess == "even") or (value % 2 == 1 and guess == "odd"):
        return "Correct!"
    else:
        return "Incorrect!"

print(guess('odd'))

#3
#Write a function that returns the number of copies of the same number. The arguments for the func-
#tion will be num 1 (first number), num 2 (second number), and num 3 (third number), if no argument
#is provided then the default for all 3 values should be 0

def copies(num1=2, num2=2, num3=0):
    count = 0
    
    if num1 == num2 == num3:
        count = 3
    elif num1 == num2 or num1 == num3 or num2 == num3:
        count = 2
    else:
        count = 0

    return count
print(copies())

#4 
#Write a function to create a game of Rock, Paper, Scissors. The function will return the winner of the
#game played by two players. The arguments to the function will be player1 (the first player’s choice)
#and player2 (the second player’s choice), if no argument is provided then the default for either player
#should be Rock

def find_winner(p1 = 'rock',p2 = 'rock'):
    
    if p1 == p2:
        return 'it is a tie'
    if (p1 == 'rock' and p2 == 'scissors'):
        return 'Player 1 wins'
    elif (p1 == 'scissors' and p2 == 'paper'):
        return 'Player 1 wins'
    elif (p1 == 'paper' and p2 == 'rock'):
        return 'Player 1 wins'
    else:
        return 'player 2 wins'
print(find_winner())

#5
#Luke Skywalker has friends and family, but he is getting older and having trouble remembering them
#all. Write a function that will return the relation defined in the table below. The arguments to
#the function will be name (name of the person related to Luke), if no argument is provided then the
#default should be nothing. That is, the empty word

def find_relation(name):
    if name == 'Darth Vader':
        return 'Father'
    elif name == 'Leia':
        return 'Sister'
    elif name == 'Han':
        return 'Brother in Law'
    elif name == 'R2D2':
        return 'Droid'
    else:
        return 'nothing'
print(find_relation('Darth Vader'))

#7
#Write a function that takes 3 numbers as arguments, num 1 (first number), num 2 (second number),
#and num 3 (third number). num 1 should be mandatory. If no arguments are provided for num 2 or
#num 3 then use 5 for num 2 and 25 for num 3. Return a list of the integers in ascending order.

def number(num1=0,num2=5,num3=35):
    if num1 > num2:
        num1, num2 = num1 , num2
    if num1 > num3:
        num1, num3 = num1, num3
    if num2 > num3:
        num2, num3 = num2, num3 
    return[num1,num2,num3]
print(number())


#8 
#Write a function that takes 3 numbers as arguments, num 1 (first number), num 2 (second number),
#and num 3 (third number). num 1 should be mandatory. If no arguments are provided for num 2 or
#num 3 then use 15 for num 2 and 5 for num 3. Return a list of the integers in descending order. You
#may not use the built-in functions

def numbers(num1 = 20,num2 = 15,num3 = 5):
    if num1 < num2:
        num1, num2 = num2, num1
    if num1 < num3:
        num1, num3 = num3, num1
    if num2 < num3:
        num2, num3 = num3, num2
    return[num1,num2,num3]
print(numbers())

#9
#Write a function that takes two arguments, a list and a value. The function should return the indices
#of all occurrences of the value in the list, if no argument is provided then the default should be to
#find 0.

def get_indices(lst, value=0):
    indices = []
    for i in range(len(lst)):
        if lst[i] == value:
            indices.append(i)
    return indices
print(get_indices([1,3,4,0,5,6]))

#10
#Write a function that returns the factors of a given integer. The argument of the function will be
#num (integer to find factors for), if no argument is provided then the default should be 36

def factors(num=36):
    factor_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            factor_list.append(i)
    return factor_list

print(factors())

#11
#Write a function that takes two numbers as arguments num and length and returns a list of multiples
#of num until the list length reaches length, if no argument is provided then the default for the list
#length should be 5.

def multiples(num, length=5):
    result = []
    for i in range(1, length + 1):
        result.append(num * i)
    return result

print(multiples(2,))

#12
def is_even(num):
    return num % 2 == 0
def report_evens(numbers):
    even_list = []
    for num in numbers:
        if is_even(num):
            even_list.append(num)
    return even_list
print (report_evens([1,2,4,5,6,7,8]))

#13
#Write a function named is vowel that returns a boolean value which determines if an letter is a vowel.
#Write a second function named report vowels that takes a string and returns a list containing all the
#vowels from the original string. Call the is vowel function as part of the report vowels function.
#Hint: In the English language, the letters a, e, i, o, and u are the vowels

def is_vowel(letter):
    return letter.lower() in ['a', 'e', 'i', 'o', 'u']

def report_vowels(text):
    vowels = []
    for ch in text:
        if is_vowel(ch):
            vowels.append(ch)
    return vowels

           # True
print(report_vowels('apple'))  # ['a', 'e']

#14. 
def is_two_digit_number(num):
    return (10 <= (num) <= 99)
def report_two_digit_numbers(numbers):
    two_digits = []
    for num in numbers:
        if is_two_digit_number(num):
            two_digits.append(num)
    return two_digits
print(is_two_digit_number(40))



#15
#Write a function named is negative that returns a boolean value which determines if an integer is
#a negative number. Write a second function named is odd that returns a boolean value which de-
#termines if an integer is odd. Write a third function named report negative odds that takes a list of
#integers and returns a new list containing all the negative odd numbers from the original list. The
#report negative odds function must call the is negative and is odd to determine if an element belongs

def isNegative(num):
    if num < 0:
        return True
    else:
        return False
def isOdd(num):
    if num % 2 == 1:
        return True
    else:
        return False
def reportNegativeOdds(lyst):
    result = []
    for num in lyst:
        if isNegative(num) and isOdd(num):
            result.append(num)
    return result

lyst = [1,2,3,-15,5,600,7]
print(reportNegativeOdds(lyst))
    






