import json
import csv

with open('response.json') as f:
    jsonResponse = json.load(f)

headers = ['Beschreibung', 'von', 'bis']
rows = []

for entry in jsonResponse['items']:
    row = []
    row.append(entry['summary'])
    try:
        row.append(entry['start']['dateTime'].replace("T", " ").replace("Z", " "))
    except:
        row.append(entry['start']['date'])
    try:
        row.append(entry['end']['dateTime'].replace("T", " ").replace("Z", " "))
    except:
        row.append(entry['end']['date'])
    rows.append(row)

with open('output.csv', 'w', newline='') as file:
    write = csv.writer(file, delimiter=';')
    write.writerow(headers)
    for row in rows:
        write.writerow(row)
