#write code to determine how many letters are in a word
'''''
word = input('pick a word')

count = 0
for letter in word:
    if letter != ' ':
        count+=1
print(count)
'''

#write code to determine how many vowels are in a given word
#word1 = hello world
#word2 = apples and bananas 
#word3 = happy times
#aeiouy
'''''
def vowel_counter(passed_word):
    count = 0
    for vowel in passed_word:
        if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u' or vowel == 'y':
            count+=1
    print(f'the vowel count in {passed_word} is {count} :')

vowel_counter('hello world')
vowel_counter('apples and bananas')
vowel_counter('happy times')
'''
'''word1 = 'hello world'
word2 = 'apples and bananas'
word3 = 'happy times'
count = 0
for vowel in word1:
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u' or vowel == 'y':
        count+=1
print(f'the vowel count in {word1}{count} is:')

for vowel in word2:
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u'or vowel == 'y':
        count+=1
print(f'the vowel count in {word2}{count} is:')

for vowel in word3:
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u'or vowel == 'y':
        count+=1
print(f'the vowel count in {word3}{count} is:')
'''
#write a function that takes an int adds two, multiplies by 4, prints the result
''''
def my_function(number):
    number += 2 
    number *= 4
    return(number)

def add_ten(number):
    number += 10
    return result

result = 10

for number in range(0,100):
    result = my_function(result)
#print(result)

#starting with the value 10, add 2, then multiply it by 4. Take the result and add two to it, then multiply by 4 again.
#call the function my fctn 10 times
#call the function my_fctn 100 times


#write a function that return the product of two arguments
def product(num1, num2,num3):
    product = num1 * num2 *num3
    return product
print(product(4,3,10))
'''
#List 
#In python, a list starts with [and ends with]
x = [] #This is a lsit with nothing in it.

lyst = ['apple', 'banana', 3, False, 4.5, 'grapes']

#print the element of the lyst in position 1 
#print(lyst[1])
#print everything that is not a string

print(lyst[2:5])
'''
x = 'appl'
print(x)

x += 'e'
print(x)
'''
#lyst.append(element) will add the element to the end of the lyst.
print(lyst)
lyst.append(12)
print(lyst)

