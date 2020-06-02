import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
def only_phone_count(calls):        
    total_ph = []
    
    for call in calls: 
        outgoing_calls, incoming_calls = call[0], call[1]
        total_ph.append(outgoing_calls)
        total_ph.append(incoming_calls)

    for text in texts:
        outgoing_texts, incoming_texts = text[0], text[1]
        total_ph.append(outgoing_texts)
        total_ph.append(incoming_texts)
    
    return len(set(total_ph))

only_phone_count(calls) # 570
count = only_phone_count(calls) 
print('There are', count, 'different telephone numbers in the records.')
