'''
import random 


#define the file, quizint.txt and 'w' which is write as txt_file
with open('week 13 /QuizInts.txt','w') as txt_file:
    #iterate through 0 - 100
    for i in range(100):
        num = random(50,200)
        # write to the txtfile
        txt_file.write(str(num + '\n'))
import random 
with open('QuizInts.txt', 'w') as f:
    for i in range(100):
        num = random.randint(50,200)
        f.write(str(num) + '\n')
'''
#2
with open('thisFile.txt', 'r') as in_file, open('thatFile.txt', 'w') as out_file:
    for index, line in enumerate(in_file):
        if index % 2 == 0:
            out_file.write(line)
'''
#3
with open('MyName.txt', 'w') as f:
    f.write('William Tauferner')
with open('MyName.txt', 'r') as f:
    name = f.read().strip()
for ch in name:
    print(ch)
#4
words = []

with open('MyWords.txt', 'r') as f:
    words.append(line.strip())

with open('MyWordsOut.txt', 'w') as out:
    for i in range(0, len(words), 5):
        group = words{i:i+5}
        out.write(''.join(group) + '\n')
#5
total_lunches = 0 

with open('LunchData.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
    parts = line.strip()
    lunches = int(parts[-1])
    total_lunches += lunches
print('total lunches served:', total_lunches)
#7 
total_visitor = 0
num_of_days = 0

with open('week 13/LibraryVisits.csv', 'r') as lib_visits:
    for _row in lib_visits:
        values = _row.split(',')
        total_visitor += int(values[1])
        num_of_days += 1 

print(f'Average visitors over {num_of_days} days is { total_visitor / num_of_days}')
#8
max_calories = None
max_day = None

with open("CaloriesBurnedData.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        date_str = parts[0]
        calories = int(parts[1])

        if (max_calories is None) or (calories > max_calories):
            max_calories = calories
            max_day = date_str

if max_day is not None:
    print("Day with highest calories:", max_day, "with", max_calories, "calories")
else:
    print("No data.")
#9
total_visitors = 0

with open("ScienceFairVisitors.txt", "r") as f:
    next(f)  # skip header
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        # last part is visitors
        visitors = int(parts[-1])
        total_visitors += visitors

print("Total visitors:", total_visitors)
#10
pages_per_member = {}

with open("PagesRead.csv", "r") as f:
    next(f)  # skip header
    for line in f:
        line = line.strip()
        if not line:
            continue
        name, pages_str = line.split(",")
        pages = int(pages_str)

        if name not in pages_per_member:
            pages_per_member[name] = 0
        pages_per_member[name] += pages

for name, total_pages in pages_per_member.items():
    print(name, "read", total_pages, "pages")
'''