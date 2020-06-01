import csv
from datetime import datetime
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def Recordofparticulardate(calls):
    new_lists = {}
    for item in calls:
        if item[2][3:10] == '09-2016':
            if item[0] not in new_lists:
                new_lists[item[0]] = int(item[3])
            else:
                new_lists[item[0]] += int(item[3])
            if item[1] not in new_lists:
                new_lists[item[1]] = int(item[3])
            else:
                new_lists[item[1]] += int(item[3])
        
    return new_lists
phoneno = Recordofparticulardate(calls)
max_in= max(phoneno, key=phoneno.get)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_in,phoneno[max_in]))
