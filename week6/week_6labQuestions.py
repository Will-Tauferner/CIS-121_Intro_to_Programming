#1 
#Write a function that loops through a word and returns a list with every other letter of the word
#starting with the first letter. The function will take a single argument word (a string representing the
#word to process).

def ever_other_letter(word):
    result = []
    for i in range(0,len(word),2):
        result.append(word[i])
    return result
print(ever_other_letter('hello this is me'))

#2 
#Write a function that loops through a word and returns a list with every other letter of the word
#starting with the second letter. The function will take a single argument word (a string representing
#the word to process

def every_other_letter(word):
    result = []
    for i in range(1,len(word),2):
        result.append(word[i])
    return result
print(every_other_letter('hello'))

#3
#Write a function that loops through and returns a list with every even number between two integers
#(inclusive). The arguments to the function will be smaller num and larger num.

def even_num(smallNum,largeNum):
    evens = []
    for i in range(smallNum,largeNum +1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(even_num(2,10))

#4
#Write a function that loops through and returns a list with every odd number between two integers
#(inclusive). The arguments to the function will be smaller num and larger num

def odd_num(smallNum,largeNum):
    odds = []
    for i in range(smallNum,largeNum):
        if i % 2 == 1:
            odds.append(i)
    return odds
print(odd_num(1,10))



#5
#Given a positive integer n, the following rules will always create a sequence that ends with 1, called
#Hailstone Sequence:
#(a) If n is even, divide by 2
#(b) If n is odd, multiply by 3 and add 1 (i.e. 3n + 1)
#(c) Continue until n is 1
#Write a function that returns a list with the hailstone sequence starting at n. The argument to the
#function will be n (the integer to start the sequence from).

def hailstone_seq(n):
    output_list = []
    while n != 1:
        if n % 2 == 0:
            n = n / 2 
        else:
            n = (3 * n) + 1

        output_list.append(n)        
    return output_list

print(f'{hailstone_seq(25)}')

#6
#Write a function that returns a list with the factors of a given integer. The argument of the function
#will be num (integer to find factors for).
def factors(num):
    factors_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors_list.append(i)
    return factors_list
#7
#Write a function that takes 3 numbers as arguments, num 1 (first number), num 2 (second number),
#and num 3 (third number). Return a list of the integers in ascending order. You may not use the
#built-in functions max (), min(), sort(), or sorted ()

def order_numbers(num1, num2, num3):
    # Start by assuming num1 is the smallest, middle, and largest
    if num1 <= num2 and num1 <= num3:
        smallest = num1
        if num2 <= num3:
            middle = num2
            largest = num3
        else:
            middle = num3
            largest = num2
    elif num2 <= num1 and num2 <= num3:
        smallest = num2
        if num1 <= num3:
            middle = num1
            largest = num3
        else:
            middle = num3
            largest = num1
    else:
        smallest = num3
        if num1 <= num2:
            middle = num1
            largest = num2
        else:
            middle = num2
            largest = num1

    return [smallest, middle, largest]

#8
#Write a function that takes 3 numbers as arguments, num 1 (first number), num 2 (second number),
#and num 3 (third number). Return a list of the integers in descending order. You may not use the
#built-in functions max (), min(), sort(), or sorted ()

def order_numbers_desc(num1, num2, num3):
    # Start by putting them in a list
    nums = [num1, num2, num3]
    if nums[0] < nums[1]:
        nums[0], nums[1] = nums[1], nums[0]
    if nums[1] < nums[2]:
        nums[1], nums[2] = nums[2], nums[1]
    if nums[0] < nums[1]:
        nums[0], nums[1] = nums[1], nums[0]

    return nums





#9
#Write a function that takes a list called cards, counts the number, and returns it from the list of
#cards provided

def count(cards):
    sum = 0
    for i in range(len(cards)):
        if cards[i] in [2,3,4,5,6]:
            sum += 1 
        elif cards[i] in [10,'j','q','k','a']:
            sum -= 1
        else:
            continue
    return sum
deck2 = ['a',2,3,4]
deck1 = [5,'j','k']
print(f'Total Count : {count(deck1)}')
print(f'Total Count : {count(deck2)}')

#10
#There’s a great war between the even and odd numbers. Many numbers already lost their lives in this
#war and it’s your task to end this. You have to determine which group sums larger: the evens or the
#odds. The larger group wins.
#Write a function that takes a list of integers named numbers, sums the even numbers and odd numbers
#separately, then returns which of the two sums is larger.

def numWars(numbers):
    even_sum = 0
    odd_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num

        else:
            odd_sum += num
    if even_sum > odd_sum:
        return 'Even Numbers is greater!'
    elif odd_sum > even_sum:
        return 'Odd Numbers is greater!'
    else:
        return 'Odd Numbers is greater!'
print(numWars([1,2,4,6,7,8,9,5]))
print(numWars([2,4,6,8]))

#11
#Write a function named add lists that takes two lists lyst1 and lyst2 and adds the first element in lyst1
#with the first element in lyst2, the second element lyst1 with the second element lyst2, etc. Return a
#new list containing the corresponding sums of the list1 and list2. You may assume both lists have the
#same length

def add_lists(lyst1,lyst2):
    new_list = []
    for i in range(len(lyst1)):
        new_list.append (lyst1[i] + lyst2[i])
    return new_list

#12
#Write a function that finds the largest even number in a list numbers. Return -1 if not found. You
#may not use the built-in functions max (), min(), sort(), or sorted ()
def largest_even(numbers):
    largest = -1  
    for num in numbers:
        if num % 2 == 0:             
            if num > largest:         
                largest = num
    return largest


#15
#To train for an upcoming marathon, Samuel goes on one long-distance run each Saturday. He wants
#to track how often the number of miles he runs fall short of the previous Saturday. This is called a
#lag day. Write a function that takes in a list of miles run every Saturday and returns Samuel’s total
#number of lag days


def lag_days(miles):
    lag_count = 0
    for i in range(1, len(miles)):
        if miles[i] < miles[i - 1]:
            lag_count += 1
    return lag_count


list1 = [1,2,3,4,5]
list2 = [10,9,8,7,6]
print(add_lists(list1,list2))

#16
#Create Youtube dislike and like buttons
def like_or_dislike(events):
    state = "nothing"  # start with no selection
    for event in events:
        if event == state:
            state = "nothing"  # pressing same button undoes it
        else:
            state = event      # pressing other button switches state
    return state


#17
#Write a function that takes two arguments, a list and an item. The function should return the indices
#of all occurrences of the item in the list

def integers(list,item):
    new_list = []
    for i in range(len(list)):
        if list[i] == item:
            new_list.append(i)
    return new_list

list = [1,2,5,4,5]
item = 5

print(integers(list,item))

#18
# Write a function that takes two numbers as arguments num and length and returns a list of multiples
#of num until the list length reaches length

def multiples(num,length):
    new_list = []
    for i in range(1,length+1):
        new_list.append(num * i)
    return new_list

num = 6
length = 4
print(multiples(num,length))

#19 
#Write a function that finds the largest odd number in a list numbers. Return -1 if not found.

def largest_even(list):
    maxnum = -1
    for i in range(len(list)):
        if list[i] % 2 == 0:
            if list[i] > maxnum:
                maxnum = list[i]
    return maxnum

list = [1]
print(largest_even(list))

#20
#Write a function that finds the largest odd number in a list numbers. Return -1 if not found

def largest_odd(list):
    maxnum = -1
    for i in range(len(list)):
        if list[i] % 2 == 1:
            if list[i] > maxnum:
                maxnum = list[i]
    return maxnum

list = [0]
print(largest_odd(list))


#

#My own
#Compute summation value

def summation(startnum,endNum):
    total = 0
    for i in range(startnum,endNum+1):
        total += i
    return total
    
print(summation(1,6))








#19
#Let s be a string and words be a list of strings. The string s is considered an acronym of words if
#it can be formed by concatenating the first character of each string in words in order. For example,
#"ab" can be formed from ["apple", "banana"], but it can’t be formed from ["bear", "aardvark"].
#Write a function that takes a string s and a list of strings words, and returns True if s is an acronym
#of words, and False otherwise


#How can I iterate through each word, and extract the first letter of each word
#combine the extracted letters and compare with string s
#For word in words:
#Combine the extracted letters and compare iwht string s
#s += letter

# is length of s is different from the length of words , false
#len(s) == len(words)

def is_acronym(s, words):
    #if length of s is not != words > false
    if len(s) != len(words):
        return False
    
    #iterate through each word
    for i in range(0,len(words)):
         #if word == '' ---> False
        current_word = words[i]
        if s[i] != words[i][0]:
            return False 
        #if word[0] == s[i]
    return True

s = 'abc'
words = ['alice', 'bob', 'Charlie']

print(f'{is_acronym(s, words)}')
