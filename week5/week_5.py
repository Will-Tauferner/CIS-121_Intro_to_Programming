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

def vowel_counter(passed_word):
    count = 0
    for vowel in passed_word:
        if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u' or vowel == 'y':
            count+=1
    print(f'the vowel count in {passed_word} is {count} :')

vowel_counter('hello world')
vowel_counter('apples and bananas')
vowel_counter('happy times')
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
