import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

dict_calllogs = {}
for item in calls:
    if item[2][3:10] == '09-2016':
        if item[0] not in dict_calllogs:
            dict_calllogs[item[0]] = int(item[3])
        else:
            dict_calllogs[item[0]] += int(item[3])
        if item[1] not in dict_calllogs:
            dict_calllogs[item[1]] = int(item[3])
        else:
            dict_calllogs[item[1]] += int(item[3])
max_in= max(dict_calllogs , key=dict_calllogs.get)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_in,dict_calllogs[max_in]))
