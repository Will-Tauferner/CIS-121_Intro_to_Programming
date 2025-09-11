#Created by William Tauferner on 9/11/2025

standards = int(input('Enter your standards: '))

if standards >= 53:
    print('A')
elif standards >= 51:
    print('A-')
elif standards >= 49: 
    print('B+')
elif standards >= 47:
    print('B')
elif standards >= 43:
    print('C+')
elif standards >= 40:
    print('C')
elif standards >= 35:
    print('D')
elif standards < 35:
    print('F')