import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
non_fraud_numbers = set()
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
fraud_numbers = set()
for row in calls:
    non_fraud_numbers.add(row[1])
    fraud_numbers.add(row[0])
for row in texts:
    non_fraud_numbers.add(row[0])
    non_fraud_numbers.add(row[1])
print("These numbers could be telemarketers: ")
total=fraud_numbers-non_fraud_numbers
total_new=sorted(total)
for i in total_new:
    print(i)
