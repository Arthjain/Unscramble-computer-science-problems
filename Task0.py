import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


print('First record of texts, {0} texts {1} at time {2}'.format(*texts[0])) 
print('Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds'.format(*calls[-1]))
