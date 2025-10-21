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
print(find_winner('rock', 'paper'))

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
    






