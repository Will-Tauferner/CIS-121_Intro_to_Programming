#William Tauferner
#1 Ask the user for two integers named larger and smaller. Determine (and output) how many times
#larger can be halved while still be greater than smaller
'''
larger_num = int(input('Enter the larger Number: '))
smaller_num = int(input('Enter the Larger Number: '))

num = 0 
while larger_num > smaller_num:
    larger_num /= 2 
    num += 1

print(f'Number of times halved: {num}')


#2 Write a program that asks the user for a word and then, using a loop, prints every other letter of the
#word starting with the second letter

word = input('Enter a word: ')
result = ''
# First start point, Ending point, step size
for i in range(1 , len(word) - 1,2) :
    result += word[i]

print(f"Output = {result}")
'''
#3 
#Using a loop, write a program that prints every even number between 37 and 1050 (inclusively)

x = 37 
y = 1050
for num in range (x, y)
    x += 1
    print(x)

#4 Write a program to create a word one letter at a time. You should prompt the user to enter a single
#letter one at a time until they type done. Done they type done, output their newly created word.
#For example

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

#5 Using a loop, write code to calculate the sum of all odd numbers between 50 and 517. Print the result
sum = 0 
for i in range(51, 517, 2):
    sum += i
print(sum)

#6 
#Write a program that repeatedly asks the user for integers until a negative integer is given.
#The program should keep track of the sum of the numbers and print the sum at the end
#(not including the negative number).

sum = 0 
while True:
    user_in = int(input('Please enter a integer'))
    if user_in < 0:
        break
    else:
        sum += user_in
        print(sum)


#7 Given a positive integer n, the following rules will always create a sequence that ends with 1, called Hailstone Sequence:
#(a) if n is even, divide by 2
#(b) if n is odd, multiply by 3 and add 1 (i.e 3n + 1)
#(c)Continue until n is 1
#write a program that prints the hailstone sequence starting at n = 25

n = 25

while n != 1: 
    if n % 2 == 0: 
        n = n // 2
    else:
        n = 3 * n + 1
#8 Write code that asks the user for an integer and then prints each number that is a factor of the input.
# Problem 8

num = int(input("Enter a number: "))

print("Factors are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)

#9 you are the newest rug fashion designer on the scene, but you’re running out of ideas. Write a program
#that will help you design rugs. The program should ask for a width, a length, and pattern, and then
#create a rug consisting of that pattern and dimensions.

width = int(input("Enter a width: "))
length = int(input("Enter a length: "))
pattern = input("Enter a pattern: ")

print("Your rug is:")
for i in range(length): #deciding rows 
    print(pattern * width) #deciding how many patters in the row

#10 Write a program that repeatedly asks the user for integers until a negative integer is given.
#Report back the largest even number the user entered (not including the negative number).
#If the user didn’t enter any even numbers report back −1.
# Problem 10

largest_even = -1

while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    if num % 2 == 0 and num > largest_even:
        largest_even = num

print("Largest even number entered:", largest_even)

#11 Write a program that asks the user for an integer. Calculate (and then print) the sum of all square
#numbers up to and including the user’s number.

# Ask for input
num = int(input("Enter a number: "))
sum_of_squares = 0
for i in range(1, num + 1):
    if i * i <= num:
        sum_of_squares += i * i
print(f"The sum of all square numbers up to", {num}, "is:", {sum_of_squares})

