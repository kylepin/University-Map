import csv
import json

with open('universities.csv', mode='r') as infile:
    reader = csv.DictReader(infile,delimiter=",", quotechar='"')
    dictionaries = []
    for row in reader:
        dictionaries.append({'INSTNM':row["INSTNM"], 'LONGITUD':float(row["LONGITUD"]), 'LATITUDE': float(row["LATITUDE"])})

with open("universities.json", 'w') as outfile:
    json.dump(dictionaries, outfile)