import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

first_record = texts[0]
last_record = calls[len(calls)-1]

text_incoming = first_record[0]
call_incoming_number = last_record[0]
text_answering = first_record[1]
call_answering_number = last_record[1]
call_during = last_record[2]
text_time = first_record[2][11:20]
call_time = last_record[3]

print('First record of texts, {0} texts {1} at time {2}'.format(*texts[0])) 
print('Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds'.format(*calls[-1]))
