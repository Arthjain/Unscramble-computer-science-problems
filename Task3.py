import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Part A
called_numbers = []
for i in range(len(calls)):
    if calls[i][0][:5] == '(080)':
        if calls[i][1][0] == '(':
            par_index = calls[i][1].find(')')
            called_numbers.append(calls[i][1][:par_index+1])
        elif calls[i][1][:3] == '140':
            called_numbers.append('140')
        else:
            called_numbers.append(calls[i][1][:4])

l = len(called_numbers)
count = called_numbers.count('(080)')
called_numbers = sorted(set(called_numbers))
print("The numbers called by people in Chennai have codes:")
for code in called_numbers:
    print(code)

# Part B
percent = count * 100 / l
print("{} percent of calls from fixed lines in Chennai are calls to other fixed lines in Chennai.".format(round(percent, 2)))
