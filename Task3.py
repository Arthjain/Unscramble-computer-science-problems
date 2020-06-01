import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
numbers_called = []
for n in range(len(calls)):
    if calls[n][0][:5] == '(080)':
        if calls[n][1][0] == '(':
            par_index = calls[n][1].find(')')
            numbers_called.append(calls[n][1][:par_index+1])
        elif calls[n][1][:3] == '140':
            numbers_called.append('140')
        else:
            numbers_called.append(calls[n][1][:4])
l = len(numbers_called)
count = numbers_called.count('(080)')
numbers_called = sorted(set(numbers_called))
print("The numbers called by people in Bangalore have codes:")
for n in numbers_called:
    print(n)
percent = count * 100 / l
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(percent, 2)))
