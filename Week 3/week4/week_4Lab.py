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

word = input('Enter a word: ')

for i in range(1 , len(word) - 1,) :
    result += word[i]

print(f"Output = {result}")



