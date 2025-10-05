#5
#Given a positive integer n, the following rules will always create a sequence that ends with 1, called
#Hailstone Sequence:
#(a) If n is even, divide by 2
#(b) If n is odd, multiply by 3 and add 1 (i.e. 3n + 1)
#(c) Continue until n is 1
#Write a function that returns a list with the hailstone sequence starting at n. The argument to the
#function will be n (the integer to start the sequence from).
'''
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
'''
#10
#There’s a great war between the even and odd numbers. Many numbers already lost their lives in this
#war and it’s your task to end this. You have to determine which group sums larger: the evens or the
#odds. The larger group wins.
#Write a function that takes a list of integers named numbers, sums the even numbers and odd numbers
#separately, then returns which of the two sums is larger.
'''
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
'''
#11
#Write a function named add lists that takes two lists lyst1 and lyst2 and adds the first element in lyst1
#with the first element in lyst2, the second element lyst1 with the second element lyst2, etc. Return a
#new list containing the corresponding sums of the list1 and list2. You may assume both lists have the
#same length
'''
def add_lists(lyst1,lyst2):
    new_list = []
    for i in range(len(lyst1)):
        new_list.append (lyst1[i] + lyst2[i])
    return new_list


list1 = [1,2,3,4,5]
list2 = [10,9,8,7,6]
print(add_lists(list1,list2))
'''
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
'''
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
    '''