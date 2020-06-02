import csv
import numpy as np 
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
fixed_lines_calls = []

for n in range(len(calls)):
    if '(080)' in calls[n][0][0:5]:
        if '140' in calls[n][1][0:3]:
            fixed_lines_calls.append('140')
        elif '(' in calls[n][1][0]:
            j= calls[n][1].find(')')
            fixed_lines_calls.append(calls[n][1][0:j+1])
        else:
            fixed_lines_calls.append(calls[n][1][0:4])

l = len(fixed_lines_calls)
count = np.char.count(fixed_lines_calls,'(080)')
count=sum(count)
fixed_lines_calls.sort()
f=np.unique(fixed_lines_calls)
print("The numbers called by people in Bangalore have codes:")
for i in f:
    print(i)
percent = count * 100 / l
print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percent))
