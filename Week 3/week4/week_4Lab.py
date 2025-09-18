#William Tauferner
#1 Ask the user for two integers named larger and smaller. Determine (and output) how many times
#larger can be halved while still be greater than smaller
'''
larger_num = int(input('Enter the larger Number: '))
smaller_num = int(input('Enter the Larger Number : '))

num = 0 
while larger_num > smaller_num:
    larger_num /= 2 
    num += 1

print(f'Number of times halved: {num}')

'''
#2
'''''
word = input('Enter a word: ')
result = ''
# First start point, Ending point, step size
for i in range(1 , len(word) - 1,2) :
    result += word[i]

print(f"Output = {result}")
'''
#3 
#Using a loop, write a program that prints every even number between 37 and 1050 (inclusively)
'''''
x = 37 
y = 1050
for num in range (x, y)
    x += 1
    print(x)
'''''
#4 
''''
word = ''
while True:
    #Read the user input
    user_in = input('Enter a letter: ')
    #if the user typed 'done' we stop
    if user_in == 'done':
        break
    else:
        #Else lets add letter into the word
        word += user_in
#print out the final word
print(f'The final word is {word}')
'''

#5 Using a loop, write code to calculate the sum of all odd numbers between 50 and 517. Print the result
sum = 0 
for i in range(51, 517, 2):
    sum += i
print(sum)
